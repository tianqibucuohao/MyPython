# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 14:21:02 2018

@author: Administrator
"""

"""
The output of a CGI script should consist of two sections, 
separated by a blank line. 
The first section contains a number of headers, 
telling the client what kind of data is following. 
Python code to generate a minimal header section looks like this:


print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers


The second section is usually HTML, 
which allows the client software to display 
 nicely formatted text with header, in-line images, etc.
Here’s Python code that prints a simple piece of HTML:

print("<TITLE>CGI script output</TITLE>")
print("<H1>This is my first CGI script</H1>")
print("Hello, world!")


"""
# 有问题，找不到函数
import cgi
import cgitb
cgitb.enable()
# 不显示错误异常，转为保存到日志
#cgitb.enable(display=0, logdir="/path/to/logdir")
form = cgi.FieldStorage()
if "name" not in form or "addr" not in form:
    print("<H1>Error</H1>")
    print("Please fill in the name and addr fields.")
print("<p>name:", form["name"].value)
print("<p>addr:", form["addr"].value)