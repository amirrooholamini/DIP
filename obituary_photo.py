import cv2
import numpy as np

img = cv2.imread('img.jpeg')
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

R, C= gray_img.shape

r = R//4
c = C//4


for i in range(r):
    for j in range(c):
        if (c-j >= i) and (c-j <= i + 30):
            gray_img[i,j] = 0

cv2.imshow("image", gray_img)
cv2.waitKey()