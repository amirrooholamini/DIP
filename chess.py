import cv2
import numpy as np

white = np.ones((40,40), dtype = np.uint8) * 255
black = np.zeros((40,40), dtype = np.uint8)

first_row = np.concatenate((black,white,black,white,black,white,black,white),axis=1)
second_row = np.concatenate((white,black,white,black,white,black,white,black),axis=1)

chess = np.concatenate((first_row, second_row,first_row, second_row,first_row, second_row,first_row, second_row),axis=0)


cv2.imshow("board", chess)
cv2.waitKey()