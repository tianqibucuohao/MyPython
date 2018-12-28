# -*- coding: utf-8 -*-

import os

global idx
global infoStart
global infoLen

def GetContent(file):
    ff=open(file,"rb")
    len=ff.seek(0,2)
    ff.seek(0,0)
    tt = ff.read(len)
    ff.close()
    tt = repr(tt)
    return tt

def idxadd():
    global idx
    idx += 1
    return idx

def getInteger(content):
    ret = False
    key = ""
    global idx
    lens = len(content)
    if (content[idx] != 'i'):
        print("not integer pos:",idx)
        return ret,key
    num = -1
    neg = False
    idxadd()
    while (idx < lens):
        c = content[idx]
        if (ord(c) < ord('0') or ord(c) > ord('9')):
            if (num == -1):
                if (c != '-' or neg == True):
                    print("unexpected int at pos: %d, char:%c" % (idx, c))
                    return ret, key
                neg = True
                continue
            else:
                if ( c != 'e'):
                    print("unexpected int at pos2: %d, char:%c" % (idx, c))
                    return ret, key
                idxadd()
                break

        if (num == -1):
            num = 0
        num *= 10
        num += ord(c) - ord('0')
        idxadd()
    
    if (True == neg):
        key = -num
    else:
        key = num
    key = int(key)
    if (key != -1):
        ret = True
    return ret,key

def getByteString(content):
    ret = False
    key = ""
    lens = len(content)
    size = -1
    global idx
    while(idx < lens):
        c = content[idx]
        if (ord(c) < ord('0') or ord(c) > ord('9')):
            if (size == -1):
                print("unexpected char at pos: %d, char:%c" % (idx, c))
                return ret,key
            if (c != ':'):
                print("unexpected char at pos: %d, char:%c" % (idx, c))
                return ret,key
            idxadd()
            break
        if (size == -1):
            size = 0
        size *= 10
        size += ord(c) - ord('0')
        idxadd()
    key = content[idx:idx+size]
    idx += size
    if (size != 0):
        ret = True
#    print(key)
    return ret,key
    
def getList(content):
    global idx
    global infoStart
    global infoLen
    ret = False
    key = ""
    
    lens = len(content)
    if (content[idx] != 'l'):
        print("liset err")
        return ret,key
    tmp = []
    idxadd()
    while (idx < lens):
        if (content[idx] == 'e'):
            idxadd()
            break
        num = 0
        keys = ""
        ret = False
        dicts = dict()
        ret,num = getInteger(content)
        if (ret == True):
            tmp.append(num)
            
        ret, keys = getByteString(content)
        if (ret == True):
            tmp.append(keys)
        
        ret, tmpList = getList(content)
        if (ret == True):
            dicts[key] = tmpList
        
        ret, dicts = getDict(content)
        if (ret == True):
            print("dicts:", len(dicts))
    key = tmp
    if (len(key) != 0):
        ret = True
    return ret,key


def getDict(content):
    global idx
    global infoStart
    global infoLen
#    print(idx)
#    print(content[:10])
    ret = False
    dicts = dict()
    lens=len(content)
    if (content[idx] != 'd'):
        print("read dict error")
        return ret, dicts
    
    idxadd()
    while(idx < lens):
        if (content[idx] == 'e'):
            idxadd()
            break
        key = ""
        ret, key= getByteString(content)
        print(ret)
        print(key)
        if (False == ret):
            break
        if (key == "info"):
            infoStart = idx
            
        num = 0
        keys = ""
        tmpList = []
        tmpdict = dict()
        
        ret,num = getInteger(content)
        if (ret == True):
            dicts[key] = num
            
        ret, key = getByteString(content)
        if (ret == True):
            dicts[key] = keys
        
        ret, tmpList = getList(content)
        if (ret == True):
            dicts[key] = tmpList
            
        ret, tmpdict = getDict(content)
        if (ret == True):
            print("dicts:", len(keys))

        if (key == "info"):
            infoLen = idx - infoStart
    if (len(dicts) != 0):
        ret = True
    return ret,dicts

def parsefile(content):
    dicts = dict()
    ret = False
    ret, dicts = getDict(content)
    print(len(dicts))

def main():
    global idx
    global infoStart
    global infoLen
    idx = 2
    infoStart = 0
    infoLen = 0
    file = "fe7e1b90fc7a311ca89fc945c6aea62686799cef.torrent"
    content = GetContent(file)
    parsefile(content)
    
if (__name__ == "__main__"):
    main()
