import numpy as np
import cv2 as cv

file = cv.imread("/home/david/Downloads/Lenna.png")
'''blur = cv.blur(file, (5, 5))
cv.imshow('blur', blur)
cv.imwrite("")
cv.waitKey(0)
'''
roi = cv.cvtColor(file, cv.COLOR_BGR2HSV)
#print(roi)
#cv.imshow("roi", roi)
#cv.waitKey(0)
'''blue_low = np.array([100, 43, 46])
blue_high = np.array([124, 255, 255])
blue_low = np.array([100, 43, 46])
blue_high = np.array([255, 255, 255])'''

purple_low = np.array([125, 43, 46])
purple_high = np.array([155, 255, 255])


mask = cv.inRange(roi, purple_low, purple_high)

res = cv.bitwise_and(file, file, mask = mask)
cv.imshow("res", res)
cv.waitKey(0)

#h_file = cv.cvtColor()