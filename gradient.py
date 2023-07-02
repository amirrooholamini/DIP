import cv2
import numpy as np

white = np.ones((255,255), dtype = np.uint8) * 255

for i in range(255):
    white[i,:] = 255 - i

cv2.imshow("board", white)
cv2.waitKey()