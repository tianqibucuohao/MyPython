# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 17:01:38 2018

@author: Administrator
"""

from ftplib import FTP
"""
FTP(host, user, passwd)
构造函数直接带user,passwd就不用再次调用 login()，已包含登录。
不带user,passwd，需要另外调用login(user,passwd)

dir(name)显示目录
delete(name)删除文件

cwd(name)切换目录

storbinary 上传文件，STOR 远程文件，读本地
retrbinary 下载到本地， RETR 远程文件，写本地
"""

def uploadfile(ftp, remotefile, localfile):
    fp = open(localfile, 'rb')
    ftp.storbinary('STOR '+remotefile, fp)
    fp.close()

def downloadfile(ftp, remotefile, localfile):
    fp = open(localfile, 'wb')
    ftp.retrbinary('RETR '+remotefile, fp.write)
    fp.close()


ftp = FTP(host='192.168.52.150')
ftp = FTP(host='192.168.52.120', user='administrator',passwd='Drcom123')
#ftp.login(user='administrator',passwd='Drcom123')
print('dir:',ftp.dir())
#ftp.set_debuglevel(2)
#dirname='./'
#ftp.cwd(dirname)
#uploadfile(ftp, 'dd.py', 'dd.py')
downloadfile(ftp, '1.txt', '1.txt')
#ftp.set_debuglevel(0)
ftp.quit()
