# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 08:54:18 2018

@author: Administrator
"""

import os
import socket
#import asyncio 

def IcsCtrl(cmd):
    ret=os.system(cmd)
    print(ret)
    
    if (ret == 1):
        print("success :",cmd)
    else:
        print("error: ", cmd)

def BindPort():
    host = "0.0.0.0"
    port = 61440
    bp = None
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as bp:
            bp.bind((host,port))
    except OSError as msg:
        bp.close()
        bp = None
        print("erros msg:", msg.errno)    
        
    print("bind port over")

def main():
    IcsCtrl("net stop sharedaccess")
    BindPort()
    IcsCtrl("net start sharedaccess")
    print("over")

if (__name__ == "__main__"):
    main()