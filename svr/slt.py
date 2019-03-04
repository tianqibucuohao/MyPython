#select mode

import selectors
import socket
import json

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

class Response:
    def __init__(self):
        #不带content-length
        self.respone = "HTTP/1.0 200 OK\r\nSERVER: Dr.COM VER SERVER\r\nCONTENT-LENGTH: {}\r\nCONTENT-TYPE: {}\r\nCONECTION: CLOSE\r\n\r\n{}"
        #带content-length
        #self.respone = "HTTP/1.0 200 OK\r\nSERVER: Dr.COM VER SERVER\r\nCONTENT-TYPE: %s\r\nCONTENT-LENGTH: %d\r\nCONECTION: CLOSE\r\n\r\n"
        self.contenttype='application/json; charset=utf-8'
        obj = {"code":"001","account":"test","password":"123456","package_group_id":"1","serial_number":"20161111123433"}
        self.data = json.dumps(obj,ensure_ascii=False)
    def GetResponse(self):
        res =self.respone.format(len(self.data),self.contenttype, self.data)
        #{self.contenttype, self.data})
        return res
    
class Request:
    def __init__(self, r):
        print('Request:',r)
        try:
            #整个http内容
            self.content = r
            # GET /POST ..
            self.method = r.split(' ')[0]
            # /jojoj
            self.path = r.split(' ')[1].split('?')[0]
            # headers 
            self.header = self.GetHeaders()
            # ?ojo&wfe&wjo=wef&234
            self.pathParam=r.split()[1].split('?')[1].split('&')
            #print('path param:', self.pathParam)
            #self.param = self._parse_parmeter(self.pathParam)
            print('method=', self.method
                  ,', path=', self.path
                  ,', param=', self.pathParam)
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

    def _parse_parmeter(parameters):
        args = parameters.split('&')
        query = {}
        for arg in args:
            k, v = arg.split('=')
            query[k] = unquote(v)
        return query
    
def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    data=''
    try:
        data = conn.recv(1024)  # Should be ready
    except BlockingIOError:
        print('')
        
    if data:
        print('echoing', repr(data), 'to', conn)
        #conn.send(data)  # Hope it won't block
        req=Request(data.decode())
        print("headers:",req.GetHeaders())
        res = Response()
        print("res:",res.GetResponse())
        conn.send(bytes(res.GetResponse(), encoding='utf-8'))
        #print("body:",req.form_body())
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()
        
def dataProc(data):
    #rspHttp="HTTP/1.0 200 OK\r\nSERVER: Dr.COM VER SERVER\r\nCONTENT-TYPE: %s\r\nCONTENT-LENGTH: %d\r\nCONECTION: CLOSE\r\n\r\n"
    pass
    

sel = selectors.DefaultSelector()

sock = socket.socket()
sock.bind(('localhost', 8088))
sock.listen(100)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)

try:
    while True:
        events = sel.select()
        for key, mask in events:
            callback = key.data
            print('key:',key)
            callback(key.fileobj, mask)
except KeyboardInterrupt:
    print('key board error')
finally:
    sel.close()
