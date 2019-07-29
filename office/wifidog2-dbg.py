"""
env :python 2.7.X 
desc : wifidog update 

"""

import urllib
import hashlib
#import uuid
import json
import os,stat
import datetime
import re
import ConfigParser

def LoadSetting(filepath):
    if (os.path.exists(filepath) == False):
        filepath = "/etc/log/wifilog.ini"
    conf = ConfigParser.ConfigParser()
    conf.read(filepath)
    ip = conf.get("wifidog", "ip")
    port = conf.get("wifidog","port")
    adp = conf.get("wifidog","adp")
    ver = conf.get("wifidog","ver")
    #print(ip, port,adp,ver)
    return ip,port,adp,ver

def WriteVer(filepath, ip,port,adp,ver):
    #print(filepath, ip, port, adp,ver)
    if (os.path.exists(filepath) == False):
        filepath = "/etc/log/wifilog.ini"
    conf = ConfigParser.RawConfigParser()
    #conf.read(filepath)
    conf.add_section('wifidog')
    conf.set("wifidog", "ip", ip)
    conf.set("wifidog","port", port)
    conf.set("wifidog","adp",adp)
    conf.set("wifidog","ver",ver)
    with open(filepath, 'wb') as configfile:
        conf.write(configfile)
	
def GetMac(adp):
    #mac=uuid.UUID(int = uuid.getnode()).hex[-12:].upper()
    #return "".join([mac[e:e+2] for e in range(0,11,2)])
    #return "000C298E72CB"
    if (adp == ""):
    	adp = "eth0"
    #print adp
    cmd=os.popen("ifconfig")
    data=cmd.read()
    cmd.close()
    #print data

    mat=adp+"\s*Link encap:\S*\s*HWaddr\s*\S*"
    ret=re.findall(mat,data)
    if (ret):
        mac=ret[0].split(' ')[-1].upper()
        #print("re:",mac)
        return "".join([mac[e:e+2] for e in range(0,18,3)]).lower()
    else:
        return ""

#def GetVer():
#	ver=datetime.date.today().strftime("%Y%m%d")
#	return ver[2:]

def HttpGet(url):
    print ("req url:",url)
    byt=''
    try:
        ret=urllib.urlopen(url)
        byt=ret.read()
        ret.close()
    except IOError as e:
        print("error:", format(e))
    return byt
	
def ParseJson(info):
	ret = 1
	url=''
	update=''
	md5=''
	ver=''
	print(info)
    
	data = json.loads(info, encoding='utf-8')
	try:
		for i in data.keys():
			if (i=="ret"):
				ret=data[i]
			elif (i=="update"):
				update=data[i]
			elif (i=="url"):
				url=data[i]
			elif (i=="md5"):
				md5=data[i]
			elif (i=="ep_ver"):
				ver=data[i]
			#elif (i=="msg"):
			#	print("note:",data[i])
	except KeyError:
		print ("input json format err")
#	print ret
#	print update
#	print url
#	print md5
#	print ver

	return ret,update,url,md5,ver
	
def Save2File(path,data):
	if (len(data) == 0):
		return 0
	with open(path,"wb+") as file:
		file.write(data)
		file.close()
		return 1
        
def CutURL(url):
	filename = url.split("/")[-1]
	#print(filename)
	if (len(filename) == 0):
		return "./run.bin"
	return filename
	
def CheckFileMD5(data, md5):
    ret = 0
    try:
        h = hashlib.md5()
        h.update(data)
        file=h.hexdigest()
        #print(file)
        file+='drcom'
        #print(file)
        n = hashlib.md5()
        #print (file.encode(encoding='utf-8'))
        n.update(file)
        file=n.hexdigest()
        #print "file:",file
        #print "md5 :",md5
        if (file == md5):
            ret = 1
        else:
            ret = 0
    except TypeError as e:
        print("check file md5 error:", format(e))
    return ret
	
def loadfile(filepath):
	with open(filepath, "rb") as file:
		byt = file.read()
		file.close()
		return byt
	
def DownloadFile(url, md5):
    #print(url, md5)
    if (len(url)==0):
        return 0
    data = HttpGet(url)
    filepath= CutURL(url)
#    print (data, filepath)
#    print filepath
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
    print ret,filepath
    return ret,filepath

def Runfile(path):
    os.chmod(path, stat.S_IRWXU+stat.S_IRWXU+stat.S_IXGRP+stat.S_IROTH+stat.S_IXOTH)
    os.system("./"+path)

def GetUrl():
    ip, port,adp,ver = LoadSetting("./wifidog.ini")
    urlpath="/eportal/?c=Wifidog&a=audit&mac="
    Mac=GetMac(adp)
    Ver=ver
    Mac="b8de5e54c367"
    url="http://"+ip+":"+str(port)+urlpath+Mac+"&ver="+Ver
    #print("req",url)
    return url,ip,port,adp

def main():
    req, ip, port,adp=GetUrl()
    ret=HttpGet(req)
    ret, update, url, md5,ver=ParseJson(ret)
    #print ret
    #print (update.encode("utf-8"))
    #print type(url)
    #print type(md5)
#    try:
    if (ret==0):
        if (int(update.encode("utf-8"))==0):
            #print "hello"
            if (len(url)>1 and len(md5)>1):
                #print "ready to download..."
                dl,file = DownloadFile(url, md5)
                print "download file finish..."
                if (dl==1):
                    WriteVer("./wifidog.ini",ip,port,adp,ver)
                    Runfile(file)
                    print "update finish!"
            else:
                print "The lastest version and no need to update!"
        else:
            print "already the lastest version!"
    else:
        print "update error:No authorization!"
#    except TypeError as e:
#            print ("error:",format(e))

if (__name__=="__main__"):
	main()