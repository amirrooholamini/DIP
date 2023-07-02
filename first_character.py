import cv2
import numpy as np
import os

import numpy as np

R,C = 400, 400
img = np.zeros((400, 400))

left = np.zeros((R-100, C//2))
right = np.zeros((R-100, C//2))

for i in range(left.shape[0]):
    for c in range(C//2):
        if abs(R-i - c*2) < 40:
            left[i,c] = 255
            
for i in range(left.shape[0]):
    for c in range(C//2):
        if abs(i - c*2) < 40:
            right[i,c] = 255
            
img[50:R-50,:C//2] = left
img[50:R-50,C//2:] = right

for i in range(R//2-15, R//2+15):
    img[i,130:280] = 255
        
cv2.imshow('image_1', img)
cv2.imshow('image_2', 255 - img)
cv2.waitKey()