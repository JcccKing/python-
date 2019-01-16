import requests
from bs4 import BeautifulSoup
for i in range(25):
    res=requests.get('https://movie.douban.com/top250?start='+str(i*25)+'&filter=')
    soup=BeautifulSoup(res.text,'html.parser')
    lists=soup.find('ol',class_='grid_view')
    txt=lists.find_all('li')
    for i in txt:
        num=i.find('em').text
        name=i.find('span',class_='title').text.strip()
        rating_num=i.find('span',class_='rating_num').text
        quote=i.find('span',class_='inq')
        url=i.find('div',class_='hd')
        final_url=url.find('a')['href']
        print(num,name,rating_num)
        print(final_url)
        if quote!=None:
            print(quote.text)
        else:
            print('没有主题。')


