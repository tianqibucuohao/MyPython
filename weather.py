import urllib
import json
#from urllib.request import urllib
#http://www.weather.com.cn/data/cityinfo/101010100.html
while True:
	city=int(input('输入区号：(00=退出)\n'))
	if city == 00:
		break
	with urllib2.urlopen('http://view-source:http://www.weather.com.cn/data/cityinfo/101010100.html') as res:
		res = res.decode('utf-8')
		print(res)
		
	