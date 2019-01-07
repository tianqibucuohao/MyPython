# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 17:22:07 2019

@author: Administrator

file operation

"""

def openfile(file):
    bIsUtf8 = False
    with open(file,"rb") as f:
        f1 = f.read(2)
        print(len(f1))
        ff1 = f1[0]
        ff2 = f1[1]
        print(ff1,ff2)
        # 0xff 0xfe
        if (ff1 == 0xff & ff2 == 0xfe):
            bIsUtf8 = True
    print("is utf-8:", bIsUtf8)        

def main():
    file1='../pachong/jux962.torrent'
    file2='../pachong/a2.html'
    openfile(file2)

if (__name__ == "__main__"):
    main()
