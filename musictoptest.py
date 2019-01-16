import requests,time,bs4,json
def test(x):
    url='https://c.y.qq.com/v8/fcg-bin/fcg_v8_toplist_cp.fcg?tpl=3&page=detail&date=2019-01-10&topid=4&type=top&song_begin='+str(x)+'&song_num=30&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'
    res=requests.get(url)
    jsonres=json.loads(res.text)
    print('qq音乐巅峰磅歌单TOP100')
    f=x
    for i in range(len(jsonres['songlist'])):
        f=f+1
        music=jsonres['songlist'][i]['data']
        if len(music)!= 0:
            finaltxt=str(f)+'. 歌曲：'+music['songname']+'  歌手:'+music['singer'][0]['name']+'  时间:'+str(music['interval'])+'秒 \n'+'歌曲链接：https://y.qq.com/n/yqq/song/'+music['songmid']+'.html \n'
            #finaltxt是个字符串 写入txt文档中
            k = open('音乐巅峰榜.txt','a+',encoding='utf-8')
            for words in finaltxt:
                try:
            #尝试执行下面的内容。在学习处理异常时，我们了解过try……except……的用法
                    k.write(words)
                except:
            #出现报错，则执行：
                    pass
                #跳过。pass的意思，就是什么也不执行，通常起占位作用，保证程序格式完整
                #网络上的电子书常有乱码，会导致不能写入报错。所以我们加一个跳过异常防止意外
                continue
            #继续循环
            k.close()
            #关闭文档
        else:
            exit()
    time.sleep(2)
a=[0,30,60,90]
for x in a:
    test(x)
    