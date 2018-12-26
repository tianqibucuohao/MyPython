#python获取指定网页上所有超链接的方法
import urllib.request
import re
import os

def saveHtml(filename, html):
    with open(filename.replace('/', '_')+".html", "wb") as f:
        f.write(html)
        f.close()

os.chdir("f:\python")
url="http://127.0.0.1"
html=urllib.request.urlopen(url)
