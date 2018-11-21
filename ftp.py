# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 17:01:38 2018

@author: Administrator
"""

from ftplib import FTP
#import cv2
#print(cv2.__version__)
ftp = FTP('192.168.54.36', 'administrator','123')
ftp.login()
ftp.dir()
ftp.quit()
