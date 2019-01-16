import requests
from bs4 import BeautifulSoup
res=requests.get('http://www.xiachufang.com/explore/')
soup=BeautifulSoup(res.text,'html.parser')
list_name=soup.find_all('p',class_='name')
list_ing=soup.find_all('p',class_='ing ellipsis')
for i in range(len(list_name)):
    print(list_name[i].text.strip())
    print(list_ing[i].text.strip())
    list_url=list_name[i].find('a')
    print('http://www.xiachufang.com'+list_url['href'])