import re
import requests
import json
newsurl='https://news.sina.com.cn/c/xl/2019-03-05/doc-ihsxncvh0013529.shtml'
m=re.search('doc-i(.+).shtml',newsurl)
newsid=m.group(1)

commentURL='http://comment5.news.sina.com.cn\
/comment/skin/default.html?channel=gn&\
newsid=comos-{}&group=0'


# commentURL.format(newsid)
#
# news=newsurl
# def getCommentCounts(newsurl):
#     m = re.search('doc-i(.+).shtml', newsurl)
#     newsid = m.group(1)
#     comments=requests.get(commentURL.format(newsid))
#     print(comments)
# getCommentCounts(news)


