# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 11:35:52 2018

@author: Administrator
"""

import os.path
import re

def openfile(path):
    with open(path) as f:
        ll = f.seek(0,2)
        f.seek(0,0)
        rl = f.read(ll)
        f.close()
        rl = repr(rl)
        return rl

def FilterIncludeStr(file):
    dat = openfile(file)
    ret = re.findall(r"#include \s*\S*", dat, re.I)
    print(len(ret))
 

def main():
    print(os.getcwd())
    root=r"F:\Client\source\duodian-ver1.0.0\DrClient\include"
    os.chdir(root)
    print(os.getcwd())
    print(os.path.dirname(root))
    
    work_dir = root
    for parent, dirnames, filenames in os.walk(work_dir,  followlinks=True):
        for filename in filenames:
            file_path = os.path.join(parent, filename)
            print('文件名：%s' % filename)
            print('文件完整路径：%s\n' % file_path)
            # gbk file error
            #FilterIncludeStr(file_path)
            

if (__name__ == "__main__"):
    main()
