import bs4,requests,time,webbrowser,pyperclip,smtplib
from urllib.request import quote
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.header import Header
from email import encoders
#爬阳光电影，寻找磁力链接：
def href_movie(name):
    gbkname=name.encode('gbk')
    url='http://s.ygdy8.com/plus/so.php?typeid=1&keyword='+quote(gbkname)
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    res=requests.get(url,headers=headers)
    linkbs=bs4.BeautifulSoup(res.text,'html.parser')
    href=linkbs.select('.co_content8 b a')
    #爬网站最后页面
    finlhref='https://www.ygdy8.com/'+href[0].get('href')
    print(finlhref)
    #查电影的网站，然后寻找下载地址
    finres=requests.get(finlhref,headers=headers).content.decode('gbk')
    link=bs4.BeautifulSoup(finres,'html.parser')
    movie_href=link.select('tbody tr a')
    if len(movie_href) !=0:
        print('迅雷下载：'+movie_href[0].getText())
        if len(movie_href)!=1:
            print('磁力链接：'+movie_href[1].get('href'))
            movie_url='迅雷下载：'+movie_href[0].getText()+'\n 磁力链接：'+movie_href[1].get('href')
        else:
            movie_url='迅雷下载：'+movie_href[0].getText()+'\n '
        copy(movie_url)
    else:
        print('抱歉未找到下载地址~')
    
#爬豆瓣电影250
def page(i):
    url='https://movie.douban.com/top250?start='+str(i)+'&filter='
    headers={
        'Host': 'movie.douban.com',
        'Referer': 'https://movie.douban.com/top250?start=0&filter=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    res=requests.get(url,headers=headers)
    bs=bs4.BeautifulSoup(res.text,'html.parser')

    for x in range(25):
        link=bs.select('.grid_view li')[x]
        linkbs=bs4.BeautifulSoup(str(link),'html.parser')
        link_num=linkbs.select(' em')
        link_title=linkbs.select('.title ')
        link_rat=linkbs.select('.rating_num')
        link_inq=linkbs.select('.inq')
        name=link_title[0].getText()
        
        if len(link_inq) !=0:
            print(link_num[0].getText()+'  电影名：'+link_title[0].getText()+'  评分：'+link_rat[0].getText())
            print('主题：'+link_inq[0].getText())
            
            final=link_num[0].getText()+'  电影名：'+link_title[0].getText()+'  评分：'+link_rat[0].getText()+'\n'+'主题：'+link_inq[0].getText()+'\n'
            copy(final)
            href_movie(name)
           
        else:
            print(link_num[0].getText()+'  电影名：'+link_title[0].getText()+'  评分：'+link_rat[0].getText())
            final=link_num[0].getText()+'  电影名：'+link_title[0].getText()+'  评分：'+link_rat[0].getText()+'\n'
            copy(final)
            href_movie(name)
            
        time.sleep(1)
#写入文档中
def copy(final):   
    k=open('dbmovie.txt','a+',encoding='utf-8')
    for words in final:
        try:
            k.write(words)
        except :
            pass
        continue
    k.close()
#发送邮件 加 附件
def sendEmail(from_addr,pw):
    try:
        msg=MIMEMultipart()
        text='python测试'
        msg.attach(MIMEText(text,'plain','utf-8'))
        with open('dbmovie.txt','rb') as f:
                mime=MIMEBase('txt','txt',filename='dbmovie.txt')
                mime.add_header('Content-Disposition', 'attachment', filename='dbmovie.txt')
                mime.add_header('Content-ID', '<0>')
                mime.add_header('X-Attachment-Id', '0')
                mime.set_payload(f.read())
                # 用Base64编码:
                encoders.encode_base64(mime)
                # 添加到MIMEMultipart:
                msg.attach(mime)
        #发送的内容
        msg['From']=Header(from_addr,'utf-8')
        #发件人
        to_addr='1811797624@qq.com'
        msg['To']=Header(to_addr,'utf-8')
        #收件人
        theme='python发邮件添加附件'
        msg['Subject']=Header(theme,'utf-8')
        #主题
        
        server=smtplib.SMTP('smtp.qq.com',25)
        #qq服务器
        server.set_debuglevel(1)
        #记录详细信息
        server.ehlo() 
        #server.starttls()
        ## 调用starttls()方法，就创建了安全连接
        #server.ehlo() 
        server.login(from_addr,pw)
        #登陆
        server.sendmail(from_addr,to_addr,msg.as_string())
        #发送信息
        server.quit()
        print('加密邮件发送成功。')
    except Exception as e:
        print('发送失败。'+e)

m=input('你需要多少页的电影简介：')
for x in range(int(m)):
    i=x*25
    page(i)
print('存入文档成功。')
from_addr=input('输入邮箱账号：')
pw=input('输入邮箱密码：')
sendEmail(from_addr,pw)
