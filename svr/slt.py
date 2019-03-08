#select mode

import selectors
import socket
import json
import configparser
import os
from urllib.parse import unquote, quote
"""
accepted <socket.socket fd=488, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8088), raddr=('127.0.0.1', 47984)> from ('127.0.0.1', 47984)
echoing b'GET /holo?wejo=2oo&jwojo=jojo&1231 HTTP/1.1\r\nHost: 127.0.0.1:8088\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9\r\n\r\n' to <socket.socket fd=488, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8088), raddr=('127.0.0.1', 47984)>
Request: b'GET /holo?wejo=2oo&jwojo=jojo&1231 HTTP/1.1\r\nHost: 127.0.0.1:8088\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9\r\n\r\n'
Traceback (most recent call last):
  File "F:\MyPython\svr\slt.py", line 80, in <module>
    callback(key.fileobj, mask)
  File "F:\MyPython\svr\slt.py", line 62, in read
    req=Request(repr(data))
  File "F:\MyPython\svr\slt.py", line 17, in __init__
    self.body = r.split('\r\n\r\n', 1)[1]
IndexError: list index out of range

===========
accepted <socket.socket fd=476, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8088), raddr=('127.0.0.1', 57133)> from ('127.0.0.1', 57133)
echoing b'GET /jwo/hoj/jojl/oooo?jowj=234&jowjo=9u9&ojo=&23jow=jo HTTP/1.1\r\nHost: 127.0.0.1:8088\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9\r\n\r\n' to <socket.socket fd=464, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8088), raddr=('127.0.0.1', 57130)>
Request: b'GET /jwo/hoj/jojl/oooo?jowj=234&jowjo=9u9&ojo=&23jow=jo HTTP/1.1\r\nHost: 127.0.0.1:8088\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9\r\n\r\n'
content  <class 'str'> ,len= 485 ,method= GET , path= /jwo/hoj/jojl/oooo?jowj=234&jowjo=9u9&ojo=&23jow=jo
httpheader:HTTP/1.1\r\nHost: 127.0.0.1:8088\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9\r\n\r\n
"""

class DrClientConfig:
    def __init__(self):
        self.bIsOpen = False
        self.config = configparser.ConfigParser()
        self.filepath=''
        self.ver=''
    def load(self, file):
        try:
            if (self.bIsOpen == False):
                self.filepath=file
                self.config.read(file, encoding='utf-8-sig')
                self.bIsOpen = True
                self.ver = self.GetVersion()
        except IOError:
            print("open file error")
        except UnicodeDecodeError:
            print("cannot read the file")
            
    def GetVersion(self):
        if(self.bIsOpen == True):
            self.ver = self.config.get('Ver', 'version')
            #print('ver=', self.ver)
            return self.ver
        else:
            return "1.0.0"
        
    def GetTransError(self):
        dicts={}
        if (self.bIsOpen == True):
            key = self.config.options('Trans')
            #print((key))
            for i in key:
                dicts[i] = self.config.get('Trans', i)
            #print(dicts)
            #obj = json.dumps(dicts,ensure_ascii=False)
            #print("json:", obj)
        else:
            print("pls load file first")
        return dicts
                
    
    #1=版本完全相同，0需要更新文件    
    def CmpVersion(self, vers):
        #print("vCmp:", vers)
        vCmp = vers.split('.')
        #print('cmp:', vCmp)
        #print("self vers:", self.ver,"type:", type(self.ver), "self get ver:", self.GetVersion())
        vCurrent = self.ver.split('.')
        #print("vCurrent:", vCurrent)
       
        if (len(vCmp) != 3):
            print("input param vers format error")
            return -1
        if (len(vCurrent) != 3):
            print("remote version format error.Reset version.")
            self.SetVersion("1.0.0")
            vCurrent = "1.0.0"
        vMF = vCurrent[0]
        vCMF = vCmp[0]
        if (vMF == vCMF):
            vMF = vCurrent[1]
            vCMF = vCmp[1]
            if (vMF == vCMF):
                vMF = vCurrent[2]
                vCMF = vCmp[2]
                if (vMF == vCMF):
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            return 0               
        
        
    def SetVersion(self, version):
        self.config.set('Ver', 'version', version)
        
    def SetTransError(self, transKey, transData):
        pass
    
    def SaveFile(self):
        self.config.write(self.filepath)

class Response:
    def __init__(self):
        #不带content-length
        self.respone = "HTTP/1.0 200 OK\r\nSERVER: Dr.COM VER SERVER\r\nCONTENT-LENGTH: {}\r\nCONTENT-TYPE: {}\r\nCONECTION: CLOSE\r\n\r\n{}"
        #带content-length
        #self.respone = "HTTP/1.0 200 OK\r\nSERVER: Dr.COM VER SERVER\r\nCONTENT-TYPE: %s\r\nCONTENT-LENGTH: %d\r\nCONECTION: CLOSE\r\n\r\n"
        self.contenttype='application/json; charset=utf-8'

    def GetResponse(self, ret, vers, trans):
        data={}
        data['ret'] = ret
        data['ver'] = vers
        data['data'] = trans
        data = json.dumps(data, ensure_ascii=False)
        print('json:', data)
        res =self.respone.format(len(data),self.contenttype, data)
        #{self.contenttype, self.data})
        return res   
    
class Request:
    def __init__(self, r):
        #print('Request:',r)
        try:
            #整个http内容
            self.content = r
            # GET /POST ..
            self.method = r.split(' ')[0]
            # /jojoj
            self.path = (r.split(' ')[1].split('?')[0])[1:]
            # headers 
            self.header = self.GetHeaders()
            # ?ojo&wfe&wjo=wef&234
            self.pathParam=r.split()[1].split('?')[1].split('&')
            #print('path param:', self.pathParam)
            #self.param = self._parse_parmeter(self.pathParam)
#            print('method=', self.method
#                  ,', path=', self.path
#                  ,', param=', self.pathParam)
            #print('headers', self.header)
    #        self.body = r.split('\r\n\r\n', 1)[1]
        except IndexError:
            print("index error")

    def GetHeaders(self):
        header_content = self.content.split('\r\n\r\n')[0].split('\r\n')[1:]
        #print('hh:',header_content)
        result = {}
        for line in header_content:
            k, v = line.split(': ')
            result[quote(k)] = quote(v)
        #print('result:',result)
        return result
    def GetPath(self):
        return self.path
    
    def GetVersion(self):
        if (self.GetPath() != 'getvers'):
            print("get path error")
            return ''
        parm = self.pathParam[0].split('=')[0]
        vers = self.pathParam[0].split('=')[1]
        if (parm != 'ver'):
            print("parm error ", parm)
            return ''
        return vers

    def _parse_parmeter(parameters):
        args = parameters.split('&')
        query = {}
        for arg in args:
            k, v = arg.split('=')
            query[k] = unquote(v)
        return query
    
#def accept(sock, mask):
#    conn, addr = sock.accept()  # Should be ready
#    print('accepted', conn, 'from', addr)
#    conn.setblocking(False)
#    sel.register(conn, selectors.EVENT_READ, read)
#
#def read(conn, mask):
#    data=''
#    try:
#        data = conn.recv(1024)  # Should be ready
#    except BlockingIOError:
#        print('')
#        
#    if data:
#        print('echoing', repr(data), 'to', conn)
#        #conn.send(data)  # Hope it won't block
#        req=Request(data.decode())
#        print("headers:",req.GetHeaders())
#        res = Response()
#        print("res:",res.GetResponse())
#        conn.send(bytes(res.GetResponse(), encoding='utf-8'))
#        #print("body:",req.form_body())
#    else:
#        print('closing', conn)
#        sel.unregister(conn)
#        conn.close()
#        
#def dataProc(data):
#    #rspHttp="HTTP/1.0 200 OK\r\nSERVER: Dr.COM VER SERVER\r\nCONTENT-TYPE: %s\r\nCONTENT-LENGTH: %d\r\nCONECTION: CLOSE\r\n\r\n"
#    pass
#

        
class CServer:
    def __init__(self):
        try:
            self.sel = selectors.DefaultSelector()
            self.sock = socket.socket()
            self.sock.bind(('0.0.0.0', 8088))
            self.sock.listen(64)
            self.sock.setblocking(False)
            self.sel.register(self.sock, selectors.EVENT_READ, self.accept)
            self.conf = DrClientConfig()
            self.conf.load('errTrans.ini')
            self.ver = self.conf.GetVersion()
            self.transdata = self.conf.GetTransError()
            self.resp = Response()
            #print("self.transdata:", self.transdata)
        except OSError as e:
            print("some error:", str(e))
        
    def accept(self, sock, mask):
        conn, addr = self.sock.accept()  # Should be ready
        #print('accepted', conn, 'from', addr)
        conn.setblocking(False)
        self.sel.register(conn, selectors.EVENT_READ, self.read) 
        
    def read(self, conn, mask):
        data=''
        try:
            data = conn.recv(1024)  # Should be ready
        except BlockingIOError:
            print('block io error')
        try:    
            if data:
                #print('echoing', repr(data), 'to', conn)
                #conn.send(data)  # Hope it won't block
                req=Request(data.decode())
                #print("vers:",req.GetVersion())
                rcv = req.GetVersion()
                #print("read self ver", self.ver)
                #print('cmp:',self.conf.CmpVersion(rcv))
                cmp = self.conf.CmpVersion(rcv)
                ret = ''
                ver = ''
                data = ''
                if (rcv == ''):
                    ret = 'e02'#请求格式错误
                elif(int(cmp) == 1):
                    ret = 'ok'
                elif(int(cmp) == 0):
                    ret = 'e01'
                    ver = self.ver
                    data = self.transdata
                resp = self.resp.GetResponse(ret, ver, data)
                conn.send(bytes(resp, encoding='utf-8'))
#                if (self.conf.CmpVersion(req.GetVersion()) == 1):
#                    #版本一致
#                    res = Response({"ret":"OK"})
#                    print("res1:",res.GetResponse('ok','','')
#                    conn.send(bytes(res.GetResponse('ok','',''), encoding='utf-8'))
#                else:
#                    res = Response(self.conf.GetTransError())
#                    #print("res2:",res.GetResponse())
#                    conn.send(bytes(res.GetResponse('e01', self.conf.GetVersion(), self.conf.GetTransError()), encoding='utf-8'))
#                    #print("body:",req.form_body())
            else:
                #print('closing', conn)
                self.sel.unregister(conn)
                conn.close()   
        except AttributeError as e:
            print('cannot read data:', str(e))
            
    def run(self):
        try:
            while True:
                events = self.sel.select()
                for key, mask in events:
                    callback = key.data
                    print('key:',key)
                    callback(key.fileobj, mask)
        except KeyboardInterrupt:
            print('key board error')
        finally:
            self.sel.close()

#sel = selectors.DefaultSelector()
#    
def main():
    svr = CServer()
    svr.run()
    
#   # global sel
#    sock = socket.socket()
#    sock.bind(('0.0.0.0', 8088))
#    sock.listen(100)
#    sock.setblocking(False)
#    sel.register(sock, selectors.EVENT_READ, accept)
#    
#    try:
#        while True:
#            events = sel.select()
#            for key, mask in events:
#                callback = key.data
#                print('key:',key)
#                callback(key.fileobj, mask)
#    except KeyboardInterrupt:
#        print('key board error')
#    finally:
#        sel.close()

if (__name__ == "__main__"):
    print(os.getcwd())
    main()
#    conf=DrClientConfig()
#    conf.load('errTrans.ini')
#    conf.GetVersion()
#    conf.GetTransError()
#    print(conf.CmpVersion("1.0.1"))
