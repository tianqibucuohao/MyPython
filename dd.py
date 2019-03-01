# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 09:57:38 2018

@author: Administrator
"""

from urllib.parse import unquote, quote

pppoe_flag = b'\x08\x00\x01\x00'
keep_alive2_flag = b'\xdc'
print(type(pppoe_flag))
st=pppoe_flag.decode()
print(type(st))
print(type(repr(pppoe_flag)))
print(pppoe_flag)
print(keep_alive2_flag)

def GetHeaders(headers):
    result = {}
    for line in headers:
        k, v = line.split(':')
        print('k=',k, '***v=',v)
        if (k != "" or k != "'"):
            result[quote(k)] = quote(v)
    #print('result:',result)
    return result

tst=(b'GET /jwo/hoj/jojl/oooo?jowj=234&jowjo=9u9&ojo=&23jow=jo HTTP/1.1\r\nHost: 127.0.0.1:8088\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9\r\n\r\n')
tst = tst.decode()
method=tst.split(' ')[0]
wholepath=tst.split(' ')[1]
param=tst.split(' ')[1].split('?')[1]
httpv = tst.split(' ')[2].split('\\r\\n')[0]
headers=tst.split('\r\n\r\n')[0].split('\r\n',1)[1:]
print("method=", method,"path=",wholepath,",param=",param)
print("http ver:", httpv)
print("headers=", headers)
#hh = GetHeaders(headers)
#print(hh)
