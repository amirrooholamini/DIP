import cv2
import numpy as np
import os

try:
    path = '3.jpg'
    if os.path.exists(path):
        img = cv2.imread(path)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        print('invalid input')
except:
    print('invalid input')

r,c = img_gray.shape

for i in range(r//2):
    for j in range(c):
        temp = img_gray[r-i-1, j]
        img_gray[r-i-1, j] = img_gray[i,j]
        img_gray[i,j] = temp
        
cv2.imshow('image', img_gray)
cv2.waitKey()