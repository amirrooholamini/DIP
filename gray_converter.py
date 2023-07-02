import cv2
import numpy as np
import os

try:
    selection = eval(input('select 1 or 2? '))
    path = f'{selection}.jpg'
    if os.path.exists(path):
        img = cv2.imread(path)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        print('invalid input')
except:
    print('invalid input')

print("wait ... ")
img_gray[:,:] = 255 - img_gray[:,:]
        
cv2.imshow('image', img_gray)
cv2.waitKey()