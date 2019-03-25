#python获取指定网页上所有超链接的方法
import urllib.request
#import re
#import os
#import RemoteDisconnected
#def saveHtml(filename, html):
#    with open(filename.replace('/', '_')+".html", "wb") as f:
#        f.write(html)
#        f.close()

#os.chdir("f:\python")
#try:
    url="http://192.168.52.149:8088/getvers?ver=1.2.1"
    html=urllib.request.urlopen(url)
    byt = html.read()
    html.close()
    print(byt)
#except RemoteDisconnected as e:
#    print(str(e))
#except ...:
#    print("error")
