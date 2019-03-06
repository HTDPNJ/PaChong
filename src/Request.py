import requests
res=requests.get("https://news.sina.com.cn/")
res.encoding='utf-8'

from bs4 import BeautifulSoup
html_sample=res.text
soup=BeautifulSoup(html_sample,'html.parser')  #指定默认解析器


soup=BeautifulSoup(html_sample,'html.parser')
header=soup.select('h1')  #使用select 找出含有h1标签的元素,,,或者a标签
# for hea in header:
#     print(hea.text)

#取得含有特定CSS属性的元素
#使用select找出含有id为title的元素（id前面需要加#）
alink=soup.select('#title')
print(alink)

#使用select 找出所有class为link的元素（class前面需加.）
for link in soup.select('.link'):
    print(link)

#使用select找出所有a tag的href连结
alinks=soup.select('a')
# for link in alinks:
#     print(link['href'])

a='<a href="#" qoo=123 abc=456> i am a link</a>'
soup2=BeautifulSoup(a,'html.parser')
print(soup2.select('a')[0]['abc'])



