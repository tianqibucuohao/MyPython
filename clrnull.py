# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 12:37:38 2019

@author: Administrator

清理文件：空行
"""

def openfile(src):
    dst = []
    with open(src, "r",encoding="utf-8") as f:
        lls = f.readlines()
        lens=len(lls)
        print(lens)
        for i in range(0, lens):
            cur= lls[i]
            #print(i,len(cur))
            if (len(cur) > 1):
               dst.append(cur)
        f.close()          
    return dst
 
def writefile(dst, ls):
    with open(dst,"w",encoding="utf-8") as f:
        f.writelines(ls)
        f.close()

src = "C:\\Users\\Administrator\\Desktop\\new.txt"
dst = "C:\\Users\\Administrator\\Desktop\\new-new.txt"

ls=openfile(src)
writefile(dst,ls)