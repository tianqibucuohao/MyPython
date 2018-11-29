#Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.
import cv2
from turtle import *
def switchupdown(x=0,y=0):
        if (pen()["pendown"]):
		end_fill()
		up()
	else:
		down()
		begin_fill()

		
def changecolor(x=0,y=0):
	global colors
	colors = colors[1:]+colors[:1]
	color(colors[0])

	
def main():
	global colors
	shape("circle")
	resizemode("user")
	sharpesize(.5)
	width(3)
	colors=["red","green","blue","yellow"]
	switchupdown()
	onscreenclick(goto,1)
	onscreenclick(changecolor,2)
	onscreenclick(switchupdown,3)
	return "EVENTLOOP"

if (__name__ == "__main__"):
        msg=main()
	print(msg)
	mainloop()
