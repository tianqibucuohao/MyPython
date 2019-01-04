import numpy as np
import cv2
import os
#FaceDetection,人脸检测
os.chdir("c:\python27")
faceCascade=cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')
eyeCascade=cv2.CascadeClassifier(r'haarcascade_eye.xml')
cap=cv2.VideoCapture('Happy.mp4')
ok=True
while (ok):
    ok,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5,minSize=(32,32))
    if (0 != len(faces)):
        for (x,y,w,h) in faces:
            fac_gray=gray[y:(y+h),x:(x+w)]
            result=[]
            eyes=eyeCascade.detectMultiScale(fac_gray,1.3,2)
    
        for (ex,ey,ew,eh) in eyes:
            result.append((x+ex,y+ey,ew,eh))
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        for (ex,ey,ew,eh) in result:
            cv2.rectangle(img, (ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    
        cv2.imshow('video',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()


