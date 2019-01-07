# -*- coding: utf-8 -*-

import cv2 as cv
file='1.jpg'
mo='la_muse'
svae=mo+'-'+file
model='./models/instance_norm/'+mo+'.t7'
#print(model)
# 加载模型
net = cv.dnn.readNetFromTorch(model)
net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV);

# 读取图片
cv.namedWindow(mo, cv.WINDOW_NORMAL)
frame = cv.imread(file)
(inWidth,inHeight) = frame.shape[:2]
inp = cv.dnn.blobFromImage(frame, 1.0, (inWidth, inHeight),
                          (103.939, 116.779, 123.68), swapRB=False, crop=False)

net.setInput(inp)
out = net.forward()

out = out.reshape(3, out.shape[2], out.shape[3])
out[0] += 103.939
out[1] += 116.779
out[2] += 123.68
out /= 255
out = out.transpose(1, 2, 0)

t, _ = net.getPerfProfile()
freq = cv.getTickFrequency() / 1000
print(t / freq, 'ms')

(outW,outH) = out.shape[:2]
print(outW,outH)
cv.resizeWindow(mo, outH,outW)
cv.imshow(mo, out)
#print(frame.shape)
print(out.shape)
#tmp = out.reshape(inWidth,inHeight)
#cv.imsave(svae,tmp)

