import socket
import sys
import os
import ssl
import asyncore

def main():
    HOST = '127.0.0.1'    # The remote host
    PORT = 1234              # The same port as used by the server
    s = None
    for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
            s = socket.socket(af, socktype, proto)
        except OSError as msg:
            s = None
            continue
        try:
            s.connect(sa)
        except OSError as msg:
            s.close()
            s = None
            continue
        break
    if s is None:
        print('could not open socket')
        sys.exit(1)
    with s:
        s.sendall(b'Hello, world')
        data = s.recv(1024)
    print('Received', repr(data))


#ssl 
#Client socket example with default context and IPv4/IPv6 dual stack
def main1():
    hostname = 'www.baidu.com'
    context = ssl.create_default_context()

    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            print(ssock.version())

#Client socket example with custom context and IPv4:
def main2():
    hostname = 'www.python.org'
    # PROTOCOL_TLS_CLIENT requires valid cert chain and hostname
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_verify_locations('path/to/cabundle.pem')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            print(ssock.version())



class HTTPClient(asyncore.dispatcher):
    def __init__(self, host, path):
        asyncore.dispatcher.__init__(self)
        self.create_socket()
        self.connect( (host, 80) )
        self.buffer = bytes('GET %s HTTP/1.0\r\nHost: %s\r\n\r\n' %
                            (path, host), 'ascii')

    def handle_connect(self):
        pass

    def handle_close(self):
        self.close()

    def handle_read(self):
        print(self.recv(8192))

    def writable(self):
        return (len(self.buffer) > 0)

    def handle_write(self):
        sent = self.send(self.buffer)
        self.buffer = self.buffer[sent:]


def main3():
    client = HTTPClient('www.python.org', '/')
    asyncore.loop()

if (__name__=="__main__"):
    main3()