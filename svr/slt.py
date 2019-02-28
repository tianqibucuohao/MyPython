#select mode

import selectors
import socket

from urllib.parse import unquote, quote
"""

"""

class Request:
    def __init__(self, r):
        print('Request:',r)
        self.content = r
        self.method = r.split()[0]
        self.path = r.split()[1]
        self.body = r.split('\r\n\r\n', 1)[1]

    def form_body(self):
        return self._parse_parameter(self.body)

    def parse_path(self):
        index = self.path.find('?')
        if index == -1:
            return self.path, {}
        else:
            path, query_string = self.path.split('?', 1)
            query = self._parse_parameter(query_string)
            return path, query

    @property
    def headers(self):
        header_content = self.content.split('\r\n\r\n', 1)[0].split('\r\n')[1:]
        result = {}
        for line in header_content:
            k, v = line.split(': ')
            result[quote(k)] = quote(v)
        return result

    @staticmethod
    def _parse_parameter(parameters):
        args = parameters.split('&')
        query = {}
        for arg in args:
            k, v = arg.split('=')
            query[k] = unquote(v)
        return query

sel = selectors.DefaultSelector()

def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    data = conn.recv(1024)  # Should be ready
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)  # Hope it won't block
        req=Request(repr(data))
        print("headers:",req.headers())
        print("body:",req.form_body())
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()

sock = socket.socket()
sock.bind(('localhost', 8088))
sock.listen(100)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)
