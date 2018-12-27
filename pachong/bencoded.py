# -*- coding: utf-8 -*-

import os

idx = 0
infoStart = 0
infoLen = 0

def GetContent(file):
    ff=open(file,"r")
    len=ff.seek(0,2)
    ff.seek(0,0)
    tt = ff.read(len)
    ff.close()
    tt = repr(tt)
    return tt

def idxadd():
    idx += 1
    return idx

def getInteger():
    pass
def getByteString():
    pass
def getList():
    pass
def getDict(content,dicts):
    lens=len(content)
    if (content.at(idx) != 'd'):
        print("read dict error")
        return
    tmpdict = dict()
    idx += 1
    while(idx < lens):
        if (content.at(idx) == 'e'):
            idxadd()
            break
        key = ""
        if (False == getByteString(key)):
            break
        if (key == "info"):
            infoStart = idx
        number = 0
        byteString = ""
        tmpList = []
        tmpdicts = dict()
        if (True == getInteger(number)):
            pass

def parsefile(content):
    dicts = dict()
    getDict(content,dicts)

def main():
    file = "fe7e1b90fc7a311ca89fc945c6aea62686799cef.torrent"
    content = GetContent(file)
    parsefile(content)
    
if (__name__ == "__main__"):
    main()
