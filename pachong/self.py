import urllib.request
import os
import re
import thread

def getTxtFromFile(file):
    ff=open(file,"r")
    len=ff.seek(0,2)
    ff.seek(0,0)
    tt = ff.read(len)
    ff.close()
    return tt

def getTxtFromUrl(url):
    f=urllib.request.urlopen(url)
    str=f.read()
    f.close()
    return str

def  saveTofile(path, stt):
    f=open(path,'wb')
    f.write(stt)
    f.close()

def saveTofile2(path, ll, host):
    f=open(path, 'w')
    if (f):
        x=0
        ls=len(ll)
        for x in range(0,ls):
            w=ll[x]
            la=len(w)
            s=w.find("\"")
            if (s):
                e=w.find("\"", s+1)
                p=w[s+1:e]
                p =host + p+ '\n'
                f.write(p)
            else:
                f.write(w)
    f.close()

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

def TT(url):
	i = 0
	while True:
		print("i=%d" % i)
		i+=1
		if (i>100):
			break


os.chdir("fD:\Python\self")
mainulr=("https://share.dmhy.org/topics/list?keyword=%E6%B5%B7%E8%B4%BC%E7%8E%8B")
host=cutUrlHost(mainulr)
if (0):
    ss=getTxtFromUrl(mainurl)
    saveTofile("a.txt", ss)
else:
    ss = getTxtFromFile("a.txt")
	
thread.thread.start()

print(len(ss))
ret=re.findall(r".<a href=\"\S*ONE_PIECE\S*", ss, re.I)
#ret=re.findall(r"*\D*#ONE\sPIECE\D*", ss)
print(len(ret))
if (ret):
    print("ok11")
    t1=ret[0]
    l=len(t1)
    s=t1.find("\"")
    if (s):
        e=t1.find("\"", s+1, l)
        print("src %s, s=%d, e=%d" % (t1, s, e))
        a=t1[s+1:e]
        print(host+a)
        ss=getTxtFromUrl(host+a)
        saveTofile("c.txt", ss)
else:
    print("error find nothing")

saveTofile2("b.txt",ret, host)

del ret