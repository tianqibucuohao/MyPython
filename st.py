# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 15:31:37 2018

@author: Administrator
"""

from html.parser import HTMLParser
import os

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.in_div = False
    
    def handle_starttag(self, tag, attrs):
        if (tag == 'a'):
            #print("Encountered a start tag:", tag)
            #attrs=dict(attrs)
            for (name,value) in attrs:
                if (name == 'href'):
                    print(value)
            self.in_div = True

    def handle_endtag(self, tag):
      #  if (tag == 'a'):
            self.in_div = False
            #print("Encountered an end tag :", tag)
            pass

    def handle_data(self, data):
   #     if (self.in_div == True):
   #         print("Encountered some data  :", data)
       pass
    def handle_startendtag(tag, attrs):
        print("Encountered starenttag:", tag)
#    def handle_decl(decl):
        #文件头
#        pass
        
def loadFromfile(path):
    f=open(path,"r")
    str=""
    if (f):
        length=f.seek(0,2)
        f.seek(0,0)
        str=f.read(length)
    f.close()
    ret=repr(str)
    del f
    del str
    return ret

def main():
    parser = MyHTMLParser()
    parser.feed('<html><head><title>Test</title></head>'
                '<body><h1>Parse me!</h1></body></html>')
    f=loadFromfile('imgg.html')
    #parser.feed(f)
    print(f[0:20])
    

if (__name__=="__main__"):
    os.chdir("f:\python")
    main()
    