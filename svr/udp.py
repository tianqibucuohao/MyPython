# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 11:23:19 2018

@author: Administrator
测试绑定udp端口
"""

import socket
import signal

def finished(signum, frame):
    print('Signal handler called with signal', signum)
    raise OSError("Couldn't open device!")

def main():
    HOST = '0.0.0.0'  
    PORT = 61440  
      
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  
    s.bind((HOST,PORT))  
    print ('...waiting for message..'  )
    while True:  
        data,address = s.recvfrom(1024)  
        print( data,address  )
        s.sendto('this is the UDP server',address)  
    s.close()  

if (__name__ == "__main__"):
    signal.signal(signal.SIGINT, finished)
    main()