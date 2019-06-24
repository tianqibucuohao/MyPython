# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 17:37:57 2019

@author: Administrator

WiFidog-update
"""

import urllib.request,urllib.error
import json
import uuid
import hashlib
import configparser
import os,stat

def LoadSetting(filepath):
    if (os.path.exists(filepath) == False):
        filepath = "/etc/log/wifilog.ini"
    conf = configparser.ConfigParser()
    conf.read(filepath)
    ip = conf.get("wifidog", "ip")
    port = conf.get("wifidog","port")
    #print(ip, port)
    return ip,port

def GetMac():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:].upper()
    #return '%s:%s:%s:%s:%s:%s' % (mac[0:2],mac[2:4],mac[4:6],mac[6:8],mac[8:10],mac[10:])
    return "".join([mac[e:e+2] for e in range(0,11,2)])

def GetVer():
    pass

def CheckFileMD5(data, md5):
    ret = 0
    try:
        h = hashlib.md5()
        h.update(data)
        file=h.hexdigest()
        #print(file)
        file+='drcom'
        print(file)
        n = hashlib.md5()
        n.update(file.encode(encoding='utf-8'))
        file=n.hexdigest()
        print(file)
        #print(md5)
        if (file == md5):
            ret = 1
        else:
            ret = 0
    except TypeError as e:
        print("check file md5 erro:", e)
    return ret

"""
加载文件，取内容作md5校验
"""
def loadfile(filepath):
    with open(filepath, "rb") as file:
        byt = file.read()
        file.close()
        return byt

def Save2File(path,data):
    if (len(data) == 0):
        return 0
    with open(path,"wb+") as file:
        file.write(data)
        file.close()
        return 1

def Runfile(path):
    #755
    os.chmod(path, stat.S_IRWXU+stat.S_IRWXU+stat.S_IXGRP+stat.S_IROTH+stat.S_IXOTH)
    # 执行后是fork子进程 ？
    os.system(path)
    
def CutURL(url):
    filename = url.split("/")[-1]
    print(filename)
    if (len(filename) == 0):
        return "./run.bin"
    return filename
    
def DownloadFile(url, md5):
    print(url,md5)
    data = HttpGet(url)
    filepath= CutURL(url)
    ret = Save2File(filepath, data)
    #print(ret)
    if (ret == 1):
        #CheckFileMD5(data, md5)
        byt = loadfile(filepath)
        ret = CheckFileMD5(byt, md5)
        if (ret == 0):
            print("down file error:checksum value diff")
    else:
        ret = 0
        print("download file error")
    return ret,filepath

def HttpGet(url):
    byt=''
    try:
        req=urllib.request.Request(url)
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36')
        f=urllib.request.urlopen(req)
        byt=f.read()
        f.close()
    except urllib.error.URLError as e:
        print(e.reason())
    #字符数组转字符串
    #ret =repr(byt)
    return byt

def ParseJson(info):
    ret = 1
    url = ''
    update = ''
    md5 = ''
    
    try:
        data = json.loads(info, encoding='utf-8')
        #print(data['update'])
        for i in data.keys():
            if (i == "ret"):
                ret = data[i]
            elif(i == "update"):
                update = data[i]
            elif (i == "url"):
                url = data[i]
            elif (i == "md5"):
                md5 = data[i]
            elif (i == "msg"):
                print("note:", data[i])
    except TypeError as e:
        print("input json format error:",e)
    
    return ret,update,url,md5

def GetUrl(ip, port, mac):
    path = "/eportal/?c=wifidog&a=audit&mac="
    url = ip
    url += ":"
    url += port
    url += path
    url += mac
    url += "&ver="
    return url

def main():
    ip, port = LoadSetting("./wifidog.ini")
    mac = GetMac()
    url = GetUrl(ip, port, mac)
    print(url)
    #rtn = HttpGet("http://192.168.23.3:8088/getvers?ver=10.0.1")
    rtn = {"ret":0,"update":"1","url":"127.0.0.1:801/eportal/xxx","md5":"xxx","msg":"成功，但是审计包版本过低"}
    rtn = json.dumps(rtn, ensure_ascii=False)
    ret, update, url, md5 = ParseJson(rtn)
    if (ret == 0):
        #print(update, url, md5)
        if (int(update) == 0):
            print("already laster version")
        elif (int(update) == 1):
            print("need to update version")
            #test download file
            url = "http://192.168.32.235:8080/6.0.0.201610240.M.W.100373/drconfigure.zip"
            md5 = "69e7d77310c57e7b14976e99a87aa3e8"
            ret,file = DownloadFile(url, md5)
            if (ret == 1):
                Runfile(file)
        else:
            print("unkowned error version")
    else:
        print("update error:No authorization!")
    
if (__name__ == "__main__"):
    main()
