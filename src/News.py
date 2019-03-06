newsurl='https://news.sina.com.cn/c/xl/2019-03-05/doc-ihsxncvh0013529.shtml'
newsid=newsurl.split('/')[-1].rstrip('.shtml').lstrip('doc-i')
print(newsid)

import re
m=re.search('doc-i(.+).shtml',newsurl)
newsid=m.group(1)
print(newsid)

import requests
comments=requests.get('http://comment5.news.sina.com.cn/comment/skin/default.html\
?channel=gn&newsid=comos-hsxncvh0013529&group=0')
comments.encoding='utf-8'
print(comments.text)

