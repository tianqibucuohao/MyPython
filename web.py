# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 14:16:32 2018

@author: Administrator
"""

import webbrowser

url = 'http://www.baidu.com/'

# Open URL in a new tab, if a browser window is already open.
# ShellExecute()
#webbrowser.open_new_tab(url)

def A(a,b,c):
    return (c,b,a)

x = 0
y = 1
z = 2

x,y,z = A(x,y,z)
print(x,y,z)