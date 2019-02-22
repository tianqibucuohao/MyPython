# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 16:06:22 2019

@author: Administrator
"""

import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()