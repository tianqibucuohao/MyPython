# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 16:04:56 2019

@author: Administrator

测试bs接口
"""

import urllib.request
import urllib.error
import http.client
import json
import base64
import hashlib

def UsehttpclientRequer(url):
    pass

def UseurllibRequert(url):
    pass

def main():
    username="web-09"
    host = "demo.doctorcom.com"
    port = 8080
    path = "/DrcomSrv/DrcomService?"
    dicts = dict()
    dicts['code'] = 085
    dicts["account"] = username
    dicts["realtime_flag"] = 0
    #obj = {"code" : 085,"account" : repr(username),"realtime_flag" : 0}
    #obj = {"code":"001","account":"test","password":"123456","package_group_id":"1","serial_number":"20161111123433"}
    js = json.dumps(obj,ensure_ascii=False)
    print(js)
    #eyJjb2RlIjoiMDAxIiwiYWNjb3VudCI6InRlc3QiLCJwYXNzd29yZCI6IjEyMzQ1NiIsInBhY2thZ2VfZ3JvdXBfaWQiOiIxIiwic2VyaWFsX251bWJlciI6IjIwMTYxMTExMTIzNDMzIn0=
    b64 = base64.standard_b64encode(bytes(js, encoding='utf-8'))
    print(repr(b64))
    md5 = hashlib.md5(b64).hexdigest()
    print(md5)
    param = "iusername={"+username+"}"+"&business="
    
    

if (__name__ == "__main__"):
    main()
