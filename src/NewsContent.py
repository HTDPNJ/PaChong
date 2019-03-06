import requests
res=requests.get("https://news.sina.com.cn/c/xl/2019-03-05/doc-ihsxncvh0013529.shtml")
res.encoding='utf-8'

from bs4 import BeautifulSoup
html_sample=res.text
soup=BeautifulSoup(html_sample,'html.parser')  #指定默认解析器
print(soup.select('.main-title')[0].text) #获取文章标题

time=soup.select('.date')[0].contents[0].strip(' ')  #获取时间
from datetime import datetime
dt=datetime.strptime(time,'%Y年%m月%d日 %H:%M')
dt.strftime('%Y-%m-%d')

article=[]
for p in soup.select('.article p'):
    article.append(p.text.strip())

tem=' '.join([p.text.strip() for p in soup.select('.article p')])
print(tem)

print(soup.select('.show_author')[0].text) #获取编辑
