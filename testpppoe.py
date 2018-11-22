# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 13:58:28 2018

@author: Administrator
"""

import os
import shutil

def CutString(src, begin, end=""):
    s = ""
    if (len(src) == 0):
            return s
    s = src
    if (len(begin) == 0):
            return s
    b = src.find(begin)
    if (b == -1):
            return s
    lb = len(begin)
    #print("begin=",begin)
    #print("b=",b)
    if (len(end) == 0):
            s = src[b+lb+1:]
            del b,lb
            return s
    e = src.find(end, (b+lb))
    if (e == -1):
            s = src[b+lb:]
    else:
            s = src[b+lb:e]
    del b,lb,e
    return s

def UpdateConfFile(uname, pwd,eth):
    data = ""
    try:
        f = open("ppoe.txt", "r+")
        if (f):
            l = f.seek(0,2)
            f.seek(0,0)
            ss = f.read(l)
            data = (ss)
    
            #f.close()
            bb = CutString(data,"USER=", "\n")
            print("bb=", bb)
            data = data.replace(bb,uname)
            cc = CutString(data,"ETH=", "\n")
            data = data.replace(cc,eth)
            if (f):
                f.seek(0,0)
                f.write(data)
            else:
                print("write file,error")
    except ...:
        print("error")
    f.close()
    UpdateUserInfoFile("pap-secrets",uname,pwd)
    UpdateUserInfoFile("chap-secrets",uname,pwd)
    
def UpdateUserInfoFile(filename,uname, pwd):
    #os.chdir("/etc/pppd")
    f = open(filename,"r+")
    data=""
    if (f):
        lines = f.readlines()
        #print(lines)
        bfind = False
        ll = len(lines)-1
        print(ll)
        data = "\""+"web1"+"\"\t*\t\""+pwd+"\""
        for x in range(0,ll):
            old = lines[x]
            print(old)            
            if(old.find(uname) != -1):
                #print(data)
                #new=lines[x].replace(old,data)
                #print(new)
                data = data + '\n'
                lines[x] = data
                bfind = True
                break
        if (bfind == False):
            data = '\n'+data
            lines.append(data)
        f.seek(0,0)
        f.truncate()   
        #f.flush()
        f.writelines(lines)
        print(lines)
    f.close()

def Is32or64():
    un = os.system('uname -a')
    info = repr(un)
    del un
    if (info.find("x86_64") != 64):
        return 1
    else:
        return 0

def IsSetupRpPPPoE():
    cmd = 'rpm -qa | grep rp-pppoe'
    uc = os.system(cmd)

def UpdateDslprivode(usname,useth):
    os.chdir('/etc/ppp/peers')
    f = open('dsl-privode',"r")
    if (f):
        lines = f.readlines()
        ll = len(lines)
        bFind = False
        ueth="plugin rp-pppoe.so " + useth
        uname = "user \""+usname + "\""
        for x in range(0, ll):
            line = liens[x]
            if (line.find('plugin') != -1):
                lines[x]=ueth
            if (line.find('user') != -1):
                lines[x]=uname
        f.seek(0,0)
        f.truncate()
        f.writelines(lines)    
    f.close()

def main():
    usname = "web-9"#input("username:")
    uspwd = "222"#input("pwd:")
    useth = "eth2"#input("which ada used:")
    print("name", usname)
    print("pwd:",uspwd)
    #UpdateConfFile(usname, uspwd, useth)
    #UpdateUserInfoFile("pap-secrets",usname,uspwd)
    #UpdateUserInfoFile("chap-secrets",usname,uspwd)
    #print("ret ", Is32or64())
    #os.system('./pppoe-start')
    UpdateDslprivode(usname, useth)

if (__name__ == "__main__"):
    main()