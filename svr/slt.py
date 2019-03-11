#select mode

import selectors
import socket
import json
import configparser
import os
#import logging
from urllib.parse import unquote, quote
"""

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
        vCmp = vers.split('.')
        #print('cmp:', vCmp)
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
        
    def SetVersion(self):
        vCurrent = self.ver.split('.')
        if (len(vCurrent)!=3):
            print("DrClientConfig versino error.reset version")
            vCurrent = self.ver= "1.0.0"
        if (int(vCurrent[2]) == 9):
            vCurrent[2] = 0
            if (int(vCurrent[1] == 9)):
                vCurrent[1] = int(vCurrent[2])+1
                vCurrent[0] = int(vCurrent[2])+1
            else:
                vCurrent[1] = int(vCurrent[2])+1
        else:
            vCurrent[2] = int(vCurrent[2])+1
        self.ver.format("%d.%d.%d", int(vCurrent[0]), int(vCurrent[1]), int(vCurrent[2]))
        print(self.ver)
        self.config.set('Ver', 'version', self.ver)
        
    def SetTransError(self, transKey, transData):
        pass
    
    def SaveFile(self):
        self.config.write(self.filepath)

class Response:
    def __init__(self):
        #带content-length
        self.respone = "HTTP/1.0 200 OK\r\nSERVER: Dr.COM VER SERVER\r\nCONTENT-LENGTH: {}\r\nCONTENT-TYPE: application/json; charset=utf-8\r\nCONECTION: CLOSE\r\n\r\n{}"
        #不带content-length
        #self.respone = "HTTP/1.0 200 OK\r\nSERVER: Dr.COM VER SERVER\r\nC\r\nCONTENT-TYPE: application/json; charset=utf-8\r\nCONECTION: CLOSE\r\n\r\n{}"
        #self.contenttype='application/json; charset=utf-8'

    def GetResponse(self, ret, vers, trans):
        data={}
        data['ret'] = ret
        data['ver'] = vers
        data['data'] = trans
        data = json.dumps(data, ensure_ascii=False)
        #print('json:', data)
        bylen = len(bytes(data, encoding='utf-8'))
        #print("byte len:", len(bytes(data, encoding='utf-8')))
        res =self.respone.format(bylen,data)
        #print("res GetResponse:", len(res), ", data=", res)
        return res   
    
class Request:
    def __init__(self, r):
#        print('Request:',r)
        #整个http内容
        self.content = r
        self.header = ''
        self.method = ''
        self.path = ''
        self.pathParam = ''

    def parse(self):
        try:
            # GET /POST ..
            self.method = self.content.split(' ')[0]
            self.header = self.GetHeaders()
            self.path = (self.content.split(' ')[1].split('?')[0])[1:]
            self.pathParam=self.content.split()[1].split('?')[1].split('&')
            #print('path param:', self.pathParam)
            #self.param = self._parse_parmeter(self.pathParam)
            print('method=', self.method
                  ,', path=', self.path
                  ,', param=', self.pathParam)
            #print('headers', self.header)
    #        self.body = r.split('\r\n\r\n', 1)[1]
        except IndexError:
            print("index error")
        except ... :
            return 0
        return 1

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
        
class CServer:
    def __init__(self):
        try:
            self.sel = selectors.DefaultSelector()
            self.sock = socket.socket()
            self.sock.bind(('0.0.0.0', 8088))
            self.sock.listen(64)
            self.sock.setblocking(False)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
            self.sel.register(self.sock, selectors.EVENT_READ, self.accept)
            self.conf = DrClientConfig()
            self.conf.load('errTrans.ini')
            self.ver = self.conf.GetVersion()
            self.transdata = self.conf.GetTransError()
            self.resp = Response()
#            self.log = logging.getLogger(__name__)
            #print("self.transdata:", self.transdata)
        except OSError as e:
            print("some error:", str(e))
#    def Init(self):
#        self.log.setLevel(level = logging.INFO)
#        handler = logging.FileHandler("log.txt")
#        handler.setLevel(logging.DEBUG)
#        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#        handler.setFormatter(formatter)
#        console = logging.StreamHandler()
#        console.setLevel(logging.INFO)
#        self.log.addHandler(handler)
#        self.log.addHandler(console)
        
    def accept(self, sock, mask):
        conn, addr = self.sock.accept()  # Should be ready
        #print('accepted', conn, 'from', addr)
        #print("accept mask=", mask)
        conn.setblocking(False)
        self.sel.register(conn, selectors.EVENT_READ, self.read) 
    
    """
    异步处理，暂时用不上
    """    
    def write(self, conn, mask):
        data = ''
        try:
            if (conn):
                data = conn.recv(1024)
        except BlockingIOError:
            print('write block io error')
        if (data):
            print('write recv data:', data)
        self.sel.unregister(conn)
        conn.close()
        
    def read(self, conn, mask):
        #print('read mask:', mask)
        data=''
        try:
            if (conn):
                data = conn.recv(1024)  # Should be ready
        except BlockingIOError:
            print('block io error')
        try:    
            if (data):
                req=Request(data.decode())
                req.parse()
                if (req.path == 'getvers'):
                    rcv = req.GetVersion()
                    #print("read self ver", self.ver)
                    #print('cmp:',self.conf.CmpVersio.n(rcv))
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
                    elif(int(cmp) == -1):
                        ret = 'e02'
                    resp = self.resp.GetResponse(ret, ver, data)
                    #print("resp", resp)
                    #print("response len=", len(resp))
                    senddata = bytes(resp, encoding='utf-8')
                    #print("send data", senddata)
                    #print("send data len=", len(senddata))
                    conn.send(senddata)  
                elif (req.path == 'upvers'):
                    print("upvers")
#                elif (req.method == 'POST'):
                    # 异步处理接收，暂用不上
#                    conn = self.sel.modify(conn, selectors.EVENT_WRITE, self.write)
#            else:
#                print('closing=>', conn)
#                self.sel.unregister(conn)
#                conn.close()   
        except AttributeError as e:
            print('cannot read data:', str(e))
        finally:
            if (conn):
                print('closing=>', conn)
                self.sel.unregister(conn)
                conn.close()
            
    def run(self):
        try:
            while True:
                events = self.sel.select()
                for key, mask in events:
                    callback = key.data
                    #print('key:',key)
#                    self.log.debug(key)
                    #print('evnts:',events, ', maks=', mask)
                    callback(key.fileobj, mask)
        except KeyboardInterrupt:
            print('key board error')
        finally:
            self.sel.close()
 
def main():
    svr = CServer()
    svr.run()

if (__name__ == "__main__"):
    print(os.getcwd())
#    main()
    conf=DrClientConfig()
    conf.load('errTrans.ini')
    conf.GetVersion()
    conf.GetTransError()
    conf.SetVersion()
#    print(conf.CmpVersion("1.0.1"))
