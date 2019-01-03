# -*- coding: utf-8 -*-

import cv2 as cv
# 加载模型
net = cv.dnn.readNetFromTorch('./models/instance_norm/the_scream.t7')
net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV);

# 读取图片
cv.namedWindow('Styled image', cv.WINDOW_NORMAL)
frame = cv.imread('TIM.png')
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

cv.imshow('Styled image', out)
