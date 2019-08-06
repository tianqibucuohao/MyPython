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
#from threading import Timer
import time
import signal
import logging
import thread

def GetDate():
    today=datetime.date.today().strftime("%Y%m%d")
    return today

def loginfo(info):
    path=os.getcwd()
    path = path+"/pylog/"
    if (os.path.exists(path)==False):
        os.mkdir(path)
    file = path+"py.log"
    #file not exist
    if (os.path.exists(file)==False):
        f=open(path,"w")
        f.close()
    #file size more than 10k
    bk = False
    if (os.path.getsize(file) > 10240):
        bkfile = path+"py.log.pre"
        os.rename(file,path)
        bk=True
    #file not exist
    if (bk == True):
        if (os.path.exists(file)==False):
            f=open(path,"w")
            f.close()
    logging.basicConfig(filename=path,  format="%(asctime)s %(name)s:%(levelname)s:%(message)s", datefmt="%d-%M-%Y %H:%M:%S", level=logging.DEBUG)
    logging.info(info)
    
def LoadAdpFromWfConf():
    path=os.getcwd()
    if (len(path) == 0):
        path="."
    path += "/conf/wf.conf"
    #path = "/home/zyy/wifidog/install/drac/conf/wf.conf"
    adp =''
    try:
        with open(path) as f:
            lines = f.readlines()
            lenlines = len(lines)
            for i in range(0, lenlines):
                data = lines[i]
                if (len(data)>2):
                    if (data.find('GatewayInterface') != -1):
                        #print data
                        adp = data.split(' ')[-1]
                        adp=adp.split('\n')[0]
                        break
    except IOError as e:
        loginfo("open file error,cannot get adapter")
    #print adp
    return adp


def LoadSetting():
    path=os.getcwd()
    if (len(path) == 0):
        path="."
    filepath = path + "/wifidog.ini"
    #print(filepath)
    ip=''
    port =''
    ver=''
    brand=''
    try:
        conf = ConfigParser.ConfigParser()
        conf.read(filepath)
        ip = conf.get("wifidog", "ip")
        port = conf.get("wifidog","port")
        ver = conf.get("wifidog","ver")
        brand = conf.get("wifidog", "brand")
    except ConfigParser.NoSectionError as e:
        loginfo("ini file erro")
        loginfo(format(e))
    #print(ip, port,ver)
    return ip,port,ver,brand

def WriteVer(ver):
    path=os.getcwd()
    if (len(path) == 0):
        path="."
    filepath = path + "/wifiver.ini"
    conf = ConfigParser.RawConfigParser()
    conf.add_section('wifidog')
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

def GetVer():
    ver = ''
    path=os.getcwd()
    if (len(path) == 0):
        path="."
    filepath = path + "/wifiver.ini"
    if (os.path.exists(filepath) == False):
        return ver
    try:
        #print(filepath)
        conf = ConfigParser.ConfigParser()
        conf.read(filepath)
        #ip = conf.get("wifidog", "ip")
        #port = conf.get("wifidog","port")
        #adp = conf.get("wifidog","adp")
        ver = conf.get("wifidog","ver")
        #print(ip, port,adp,ver)
    except ConfigParser.NoSectionError as e:
        ver = ''
    return ver

def HttpGet(url):
    #loginfo("req url=>")
    #loginfo(url)
    byt=''
    try:
        ret=urllib.urlopen(url)
        byt=ret.read()
        ret.close()
    except IOError as e:
        loginfo("httget error:")
        loginfo(format(e))
    return byt
	
def ParseJson(info):
	ret = 1
	url=''
	update=''
	md5=''
	ver=''
	loginfo(info)
    
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
		loginfo ("input json format err")
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
        loginfo("check file md5 error:")
        loginfo(format(e))
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
            loginfo("down file error:checksum value diff")
    else:
        ret = 0
        loginfo("download file error")
    #print ret,filepath
    return ret,filepath

def Runfile(path, brand):
    os.chmod(path, stat.S_IRWXU+stat.S_IRGRP+stat.S_IXGRP+stat.S_IROTH+stat.S_IXOTH)
    path = "./" +path
    if (len(brand)>2):
        path = path+ " "+brand
    #os.exec(path)
    loginfo("runfile :")
    loginfo(path)
    thread.start_new_thread(os.system,(path,))

def GetUrl():
    ip, port,ver,brand = LoadSetting()
    adp=LoadAdpFromWfConf()
    urlpath="/eportal/?c=Wifidog&a=audit&mac="
    Mac=GetMac(adp)
    Ver=''
    tmpver = GetVer()
    if (len(tmpver)<2):
        Ver=ver
    else:
        Ver=tmpver
    #Mac="b8de5e54c367"
    url="http://"+ip+":"+str(port)+urlpath+Mac+"&ver="+Ver
    #print("req",url)
    return url,ip,port

def RUN():
    req, ip, port=GetUrl()
    ret=HttpGet(req)
    ret, update, url, md5,ver=ParseJson(ret)
    #print ret
    #print (update.encode("utf-8"))
    #print type(url)
    #print type(md5)
    try:
        if (ret==0):
            if (int(update.encode("utf-8"))==1):
                #print "hello"
                if (len(url)>1 and len(md5)>1):
                    #print "ready to download..."
                    dl,file = DownloadFile(url, md5)
                    #loginfo( "download file finish...")
                    if (dl==1):
                        WriteVer(ver)
                        loginfo("update finish!")
                        Runfile(file, brand)
                #else:
                    #loginfo("The lastest version and no need to update!")
            else:
                loginfo( "The already the lastest version!")
        else:
            loginfo( "update error:No authorization!")
    except TypeError as e:
            loginfo("parse data error:")
            loginfo(format(e))
          
def main():
    print "start th update mod..."
    loginfo("start the update mod...")
    signal.signal(signal.SIGINT, Shutdown)
    #signal.signal(signal.SIGKILL, Shutdown)
    while (True):
        RUN()
        for i in range(0, 60):
            time.sleep(5)
            #print i
        
def Shutdown(signalnum, frame):
    loginfo("exit the update mod...")
    exit(0)

if (__name__=="__main__"):
    main()
    