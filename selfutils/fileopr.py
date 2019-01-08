# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 17:22:07 2019

@author: Administrator

file operation

"""
import codecs

def openfile(file):
    bIsUtf8 = False
    with codecs.open(file,'r','utf-8') as f:
        fbom = f.read(2)
        print(len(fbom))
        ff1 = fbom[0]
        ff2 = fbom[1]
        print(ff1,ff2)
        # 0xff 0xfe
        if (ff1 == 255 and ff2 == 254):
            bIsUtf8 = True
        s=repr(f.read(200))
        print(type(s))
        if (bIsUtf8):
            print(s)
    print("is utf-8:", bIsUtf8)        

def main():
    file1='../pachong/hjd2048.com-1109ipx229-h264.torrent'
    file2='../pachong/a2.html'
    openfile(file2)

if (__name__ == "__main__"):
    help(open)
    main()
    #help(str)
