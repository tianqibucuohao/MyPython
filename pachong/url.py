# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 16:27:16 2018

@author: Administrator
"""

import urllib
import http.client
import os
import re

def CutString(src, begin, end=""):
    s=""
    if (len(src)==0):
            return s
    s=src
    if (len(begin)==0):
            return s
    b=src.find(begin)
    if (b == -1):
            return s
    lb=len(begin)
    #print("begin=",begin)
    #print("b=",b)
    if (len(end)==0):
            s=src[b+lb+1:]
            del b,lb
            return s
    e=src.find(end, (b+lb))
    if (e == -1):
            s=src[b+lb:]
    else:
            s=src[b+lb:e]
    del b,lb,e
    return s

def SaveToFile(path, data):
    f=open(path,mode='w+b')
    if (f):
        f.write(data)
    f.close()
    
def getTxtFromUrl(url):
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36')
    f=urllib.request.urlopen(req)
    byt=f.read()
    f.close()
    # httpcode
    print("getCode=",f.getcode())
    # request url
    print("getUrl=",f.geturl())
    # server http header info
    #info=f.info()
    #print(info)
    #info1=repr(info)
    #filename=CutString(info1, "filename=\"","\"")
    #print("filename=%s "% filename)
    print("getInfo=", f.info())
    #字符数组转字符串
    str=repr(byt)
    filename='[FHD/6.83G]GVG-216 色調P●A會長和惡小子學生會 かすみ果穂.torrent'
    SaveToFile(filename, byt)
    return str

def GetHttp(url, path):
    conn=http.client.HTTPConnection(url)
    conn.request("GET",path)
    r1=conn.getresponse()
    print(type(r1))
    print("r1:",r1)
    r2=r1.getheader("Content-Disposition")
    print("r2:",r2)
    print(type(r2))
    
def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    return new_title

def main():
    filename="[FHD/6.83G]GVG-216 色調P●A會長和惡小子學生會 かすみ果穂.torrent"
    ff=validateTitle(filename)
    #ff=filename.replace(' ','')
    SaveToFile(ff, "123")
    #GetHttp("www.rmdown.com", "/download.php?reff=722217&ref=183eae2808ae83c20cbb9fe40d7477200039a374085")
    #html=getTxtFromUrl('http://www.rmdown.com/download.php?reff=722217&ref=183eae2808ae83c20cbb9fe40d7477200039a374085')
#    if (html):
#        print(html[0:10])
#    print()

if (__name__=="__main__"):
    os.chdir("f:\python")
    main()