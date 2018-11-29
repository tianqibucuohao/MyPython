Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import cv2
>>> from turtle import *
>>> def switchupdown(x=0,y=0):
	if (pen()["pendown"]):
		end_fill()
		up()
	else:
		down()
		begin_fill()

		
>>> def changecolor(x=0,y=0):
	global colors
	colors = colors[1:]+colors[:1]
	color(colors[0])

	
>>> def main():
	global colors
	shape("circle")
	resizemode("user")
	sharpsize(.5)
	width(3)
	colors=["red","green","blue","yellow"]
	switchupdown()
	onscreenclick(goto,1)
	onscreenclick(changecolor,2)
	onscreenclick(switchupdown,3)
	return "EVENTLOOP"

>>> if (__name__ == "__main__"):
	msg=main()
	print(msg)
	mainloop()

	
Traceback (most recent call last):
  File "<pyshell#32>", line 2, in <module>
    msg=main()
  File "<pyshell#27>", line 5, in main
    sharpsize(.5)
NameError: name 'sharpsize' is not defined
>>> def main():
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

>>> if (__name__ == "__main__"):
	msg=main()
	print(msg)
	mainloop()

	
Traceback (most recent call last):
  File "<pyshell#39>", line 2, in <module>
    msg=main()
  File "<pyshell#34>", line 3, in main
    shape("circle")
  File "<string>", line 5, in shape
turtle.Terminator
>>> 
KeyboardInterrupt
>>> 
