from urllib import request
from html.parser import HTMLParser
from html.entities import name2codepoint
import re

class SelfHtmlParser(HTMLParser):
#	def __init__(self):
#	成员变量
	f=open("a.txt","w")
		
	def handle_starttag(self, tag, attrs):
		print("Start tag:", tag)
		for attr in attrs:
	#		if attr[0] is 'href':
	#			print("	attr:", attr)	
	#			print("	attr[0]:", attr[0])	
	#			print("	attr[1]:", attr[1])	
	#			print(" str attr[0]=", str(attr[1]))
			sb = re.search('http://*', str(attr[1]))
			print(sb)
	#		if sb:
	#			self.f.write(str(sb))
			#	self点成员变量操作
			#	self.f.write(attr[1])
			#	self.f.write('\n')
	#			print(type(str(attr[1])))
	#		print(type(attr))
	#		print(type(attr[0]))

	def handle_endtag(self, tag):
		print("End tag:", tag)
		
	def handle_data(self, data):
		print("Data 	:", data)
		
	def handle_comment(self, data):
		print("Commont	:", data)

	def handle_entityref(self, name):
		c = chr(name2codepoint[name])
		print("Name ent:", c)
		
#	def handle_charref(self, name):
#		if name.startswitch('x'):
#			c = chr(int(name[1:], 16)
#		else:
#			c = chr(int(name))
#		print("Num ent	:", c)

	def handle_decl(self, data):
		print("Decl 		:", data)
		
				
#res=request.urlopen('https://www.baidu.com/more/')
#page=res.read()

parser=SelfHtmlParser()
parser.feed('<a href="http://news.baidu.com/ns?cl=2&rn=20&tn=news&word=" wdfield="word"  onmousedown="return c({\'fm\':\'tab\',\'tab\':\'new\'})">新闻</a>')
#parser.feed(str(page))


#f=open(".\\a.html","w")
#f.write(ab)
#f.close()