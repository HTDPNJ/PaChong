import requests
res=requests.get("https://news.sina.com.cn/")
res.encoding='utf-8'

from bs4 import BeautifulSoup
html_sample=res.text
soup=BeautifulSoup(html_sample,'html.parser')  #指定默认解析器

for news in soup.select('.main-nav'):
    if len(news.select('li'))>0:
        print(news.select('li')[0].text)

import sqlite3
import pandas as pd
with sqlite3.connect('news.sqlite')as db:  #把pandas文件存到数据库中
    pd.DataFrame.to_sql('文件名',con=db)

with sqlite3.connect('news.sqlite')as db: #存取文件到数据库中
    df2=pd.read_sql_query('SELECT * FROM news',con=db)