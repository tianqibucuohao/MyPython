import re
import os
#import html
from html.parser import HTMLParser
import urllib.request
import urllib.error
import http.client

"""
网站域名失效，不可用，找不到地址
#类解析所有标签——值
class MyHtmlParser(HTMLParser):
    def handle_start(self, tag,attrs):
            print("A start tag:",tag)

    def handle_endtag(self, tag):
            print("An end  tag:", tag)

    def handle_data(self, data):
            print("some data   :",data)
"""

class LineInfo:
    def ___init___(self):
        self.name=""
        self.pageurl=""
        self.rmurl=""
        self.torrenturl=""
    def Set(self,name, pageurl,rmurl,torurl):
        self.name=name
        self.pageurl=pageurl
        self.rmurl=rmurl
        self.torrenturl=torurl
    def SetName(self, name):
        self.name=name
    def SetPageUrl(self, pageurl):
        self.pageurl=pageurl
    def SetRMUrl(self, rmurl):
        self.rmurl=rmurl
    def SetTorrUrl(self,torurl):
        self.torrenturl=torurl
        

class WholeInfo:
    info=[]
    count=0
    #idx=0
    def __init__(self):
        self.idx=0
    def loadFromFile(filepath):
        print("wi info")
    def PushBack(self,li):
        WholeInfo.info.append(li)
        WholeInfo.count+=1
    def ResetIdx(self):
        self.idx=0
    def Get(self,i=0):
        return WholeInfo.info[i]
    def len(self):
        WholeInfo.count=len(WholeInfo.info)
        return WholeInfo.count
    
    def Begin(self):
        self.idx=0
        return WholeInfo.info[self.idx]
    def End(self):
        self.idx=WholeInfo.count
        return WholeInfo.info[self.idx+1]
    
    def Next(self,i=0):
        self.idx=i
        tmp=WholeInfo.Get(self.idx)
        self.idx+=1
        return tmp
    
"""
从文件加载页面内容，测试使用
"""
def loadFromFile(path):
    f=open(path,"r")
    ss=""
    if (f):
            len=f.seek(0,2)
            f.seek(0,0)
            ss=f.read(len)
    f.close()
    str=repr(ss)
    del f
    return str

"""
把结果列表保存到文件，测试使用
"""
def SaveToFileList(path, lit):
    f=open(path,"w")
    if (f):
            x=0
            leng=len(lit)
            for x in range(0,leng):
                    w=lit[x]
                    url=CutString(w, "<a href=\"","\"")
                    name=CutString(w, "id=\"\">","</a>")
                    if (name.find("<b>") == -1):
                            d=name+'\t'+url+'\n'
                            f.write(d)
    f.close()
"""
re转到列表
"""
def ReToList(lit):
    x=0
    global wi
    leng=len(lit)
    for x in range(0,leng):
        w=lit[x]
        url=CutString(w, "<a href=\"","\"")
        name=CutString(w, "id=\"\">","</a>")
        li=LineInfo()
        if (name.find("<b>") == -1):
                li.name=name
                li.pageurl=url
                wi.PushBack(li)
                del li
"""
保存文件 二进制
"""
def SaveToFileBit(path, data):
    print(path)
    try:
        f=open(path,'wb')
        if (f):
            f.write(data)
        else:
            print("open file error:", path)
        f.close()
    except FileNotFoundError as e:
        print(e.errno)
"""
从url获取页面内容
"""
def HttpGet(url):
    try:
        req=urllib.request.Request(url)
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36')
        o=urllib.request.urlopen(req)
        f=""
        #print("http code=",o.getcode())
        if (o.getcode()==200):
            f=o.read()
            o.close()
        return repr(f)
    except ValueError:
        return int(0)
    except urllib.error.URLError as e:
        print(e.reason)
    
"""
分割源字符串src
begin, end开始结束标志
"""
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
            

"""
页面内容来源
0=本地文件
1=远程url
"""
def GetSrc(url, i=1):
    data=""
    if (i):
        data=HttpGet(url)
    else:
        data=loadFromFile(url)
    return repr(data)

"""
列表页面信息，解所有电影链接
"""
def GetBBsPage(url):
    #列表页面
    data=GetSrc(url,0)
    global wi
    wi=WholeInfo()
    ret=re.findall(r".<a href=\"\S*htm_data\S* target=\"_blank\" id=\"\">\S*\s*\S*\s*\S*\s*\S*\s*\S*\s*\S*\s*\S*\s*\S*\s*\S*\s*\S*</a>", data, re.I)
    if (ret):
            #print(len(ret))
            SaveToFileList("1.txt",ret)
            ReToList(ret)
            #print(wi.len())
    else:
            print("GetBBsPage error")

"""
某一电影页面内容，解下载链接
"""
def GetRmUrl(url):
    data=""
    #print("rm url=%s" % url)
    #进入单个链接页面
    data=GetSrc(url,1)
    #ret=re.findall(r">http://rm\S*</a>",data,re.I)
    ret=re.findall(r"href=\"\S*rm\S*</a>",data,re.I)
    if (ret):
            #print(ret[0])
            #ahref=CutString(ret[0],"href=\"",">")
            #print("ahref=",ahref)
            url=CutString(ret[0],">","</a>")
            #print("url=",url)
    else:
            print("GetRmUrl error")       
    return url

"""
下载链接页面，组种子下载链接
"""
def GetLinkphp(url):
    data=""
    data=GetSrc(url)
    ret=re.findall(r"name=\"\S*\"\s*value=\"\S*\"",data,re.I)
    linkurl=""
    if (ret):
        #print(len(ret))
        #print(ret[0])
        #print(ret[1])
        p1=CutString(ret[0],"value=\"","\"")
        p2=CutString(ret[1],"value=\"","\"")
        linkurl="http://www.rmdown.com/download.php?reff="+p1+"&ref="+p2
        #print(linkurl)
    else:
        print("GetLinkphp error")
    return linkurl

def HttpDownload(url, filename):
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36')
    f=urllib.request.urlopen(req)
    byt=f.read()
    f.close()
    # httpcode
    if (200 == f.getcode()):
        #info=f.info()        
        #print(f.info())
        #a=info.getheader("filename")
        #print(a)
        #print(type(info))
        #info1=repr(info)
        #print("len,",len(info1))
        #a=info1.find("filename",0)
        #print("a,",a)
        #filename1=Cutstr(info1, "filename=\"","\"")
        #print("filename=%s "% filename1)
        #print("getInfo=", f.info())       
        SaveToFileBit(filename, byt)
        #s=repr(byt)
        #print(s[0:20])
        ret=1
    return ret
"""
下载种子文件
"""
def DownloalTorrent(tUrl, filename):
    #print("turl=%s" % tUrl)
    ret=HttpDownload(tUrl,filename)
    if (ret==1):
        print("down ok")
    else:
        print("down error=>", tUrl)
        
"""
过滤特殊字符
"""        
def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    return new_title

"""
加载各行页面
"""
def RequestPage():
    global wi
    #if (wi.len()==0):
    #    return
    x=0
    #f=open("2.txt", "w")
    for x in range(0, wi.len()):
        li=wi.Get(x)
        #print("Url=%s" % li.pageurl)
        rmurl=GetRmUrl(li.pageurl)
        #print("name=",li.name)
        li.SetRMUrl(rmurl)
        #print("rmurl=%s" % rmurl)
        torrenturl=GetLinkphp(li.rmurl)
        #print("torrenturl=%s" % torrenturl)
        li.SetTorrUrl(torrenturl)
        name=li.name+(".torrent")
        fp=validateTitle(name)
        #DownloalTorrent(li.torrenturl, fp)
        #line=li.pageurl+'\n'
        #line += li.torrenturl+'\n'
        #f.write(line)
        #print("line=>",line)
    #f.close()

def main():
    global wi
    wi = WholeInfo()
    #host="cl.ki0.xyz"
    #url="http://cl.ki0.xyz/htm_data/15/1811/3334848.html"
    url="thread0806.php.html" 
    GetBBsPage(url)
    """
    http://cl.ki0.xyz/thread0806.php?fid=15&amp;search=&amp;page=%d
    """
    RequestPage()
    # rmhost="www.rmdown.com"
    # rm="/link.php?hash=1834a70efb53cbbca0039b809715aa529c02d462220"
   # GetRmUrl("3320374.html")
    # dt="/download.php?reff=981668&ref=1834a70efb53cbbca0039b809715aa529c02d462220"
    # dthost="www.rmdown.com"
    #GetLinkphp("link.php.html")

def main2():
#    wi = WholeInfo()
#    li=lineinfo()
#    li.set("q","p", "rm", "tor")
#    l2=lineinfo()
#    l2.setname("n")
#    l2.setpageurl("pp")
#    l2.setrmurl("rmul")
#    l2.settorrurl("torrreen")
#    wi.pushback(li)
#    wi.pushback(l2)
#    print("len=",wi.len())
#    l3=wi.get(1)
#    print(l3.rmurl)
#    l3.setpageurl("qqq.com")
#    l4=wi.get(1)
#    print(l4.rmurl)
#    requestpage(wi)
    pass
    
if (__name__ == "__main__"):
    os.chdir("f:\python")
    main()
    print("ok=======")
