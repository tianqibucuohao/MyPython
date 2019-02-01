import urllib.request
import os
import re
import threading
import time

#定义类结构-文件保存格式：文件名(页面名)\t页面地址 \t 磁链1 \t磁链2
class UrlItem:
    def __init__(self):
        self.name=""
        self.url=""

#
def GetTorrentUrl(src):
    if (len(src)==0):
        return ""
    gtu = re.findall(r">magnet:\S*</a>", src, re.I)
    la=len(gtu)
    tu =""
    for i in range(0, la):
        a=cutMagnet(gtu[i])
        tu += a
        tu += '\t'
    return tu

# 返回字符串：读文件所有内容
def getTxtFromFile(file):
    ff=open(file,"r")
    len=ff.seek(0,2)
    ff.seek(0,0)
    tt = ff.read(len)
    ff.close()
    return tt
#返回字符串：加载url页面
def getTxtFromUrl(url):
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36')
    f=urllib.request.urlopen(req)
    byt=f.read()
    f.close()
    #字符数组转字符串
    str=repr(byt)
    return str
#字符串内容保存到文件路径 
def  saveTofile(path, stt):
    f=open(path,'wb')
    f.write(stt)
    f.close()

#取字符串子串
# 参数说明 : src 源字符串，s,e, 开始结束字符串标志
def Getsubstring(src, s, e=""):
    ls=len(s)
    if (ls == 0):
        return src
    start=src.find(s)
    if (start == -1):
        print("cannot find :%s" % s)
        return ""
    if (len(e) == 0):
        return src[start+ls:]
    le=start+ls+1
    end=src.find(e, le)
    if (end == -1):
        return src[le-1:] 
    return src[le-1:end]

#把lise内容改成完整url保存到文件
def saveTofile2(path, ll, host):
    f=open(path, 'a')
    if (f):
        x=0
        ls=len(ll)
        for x in range(0,ls):
            w=ll[x]
            ul = UrlItem()
            ul.name = Getsubstring(w, "</span>", "</a>")
            ul.url=host + Getsubstring(w, "<a href=\"", "\"")
            
            ss=getTxtFromUrl(ul.url)
            gg1=GetTorrentUrl(ss)

            info=ul.name + '\t' + ul.url + '\t' + gg1 + '\n'
            f.write(info)
    f.close()
#解析url取host部份，带端口没有做，默认80/433端口
def cutUrlHost(url):
        if (len(url) == 0):
            return ""
        s=url.find("https://")
        offset=8
        if (s == -1):
            s=url.find("http://")
            if (s==-1):
                return ""
            offset=7
        e=url.find("/", s+offset)
        if (e == -1):
            h = url[s:]
          #  h+= "/"
        else:
            h=url[s:e]
        return h

def cutMagnet(url):
    s=0
    s=Getsubstring(url, ">", "</")
    #print("sub url:%s" % s)
    return s
       
#正文代码
os.chdir("f:\mypython")
mainurl=("https://share.dmhy.org/topics/list?keyword=%E6%B5%B7%E8%B4%BC%E7%8E%8B")
host=cutUrlHost(mainurl)
#threadLock = threading.Lock()
i=0
if (i<5):
    if (1):
        ss = getTxtFromUrl(mainurl)
#        saveTofile("a.txt", ss)
    else:
        ss = getTxtFromFile("a.txt")

    #                 <a href=\"\S*ONE_PIECE\S*\"\s*target=\"\S*\"\s*>\s*\S*<span\sclass=\"\S*\">\S*\s*\S*\s*\S*\s*\S*
    ret=re.findall(r".<a href=\"\S*ONE_PIECE\S*\"\s*target=\"\S*\"\s*>\s*\S*\s*\S*\s*\S*\s*\S*\s*", ss, re.I)
    #ret=re.findall(r"*\D*#ONE\sPIECE\D*", ss)
    if (ret):
        print("ok!")
        print(ret[0])
    else:
        print("error find nothing")
#    ss=getTxtFromUrl(host+a)
#    saveTofile("c.txt", ss)
    saveTofile2("b.txt",ret, host)
#    #下一页 下一頁
#    ret=re.findall(r"\s*<a href=\"/topics/list\S*\"", ss, re.I)
#    print(len(ret))
#    if (ret):
#        print("ret[0]=%s" % ret[len(ret)-1] )
#        nextpage = host + Getsubstring(ret[len(ret)-1], "<a href=\"", "\"")
#        print("cuturl=%s" % nextpage)
#        mainurl=nextpage
#        i+=1
del ret