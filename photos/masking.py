import cv2 as cv
import numpy as np
img=cv.imread('friends.JPG')
resize=cv.resize(img,(500,500))
#.imshow('basic',resize)
blank=np.zeros((500,500),dtype='uint8')
#cv.imshow('blank',blank)
circle=cv.circle(blank,(resize.shape[1]//2,resize.shape[0]//2),200,255,-1)
#cv.imshow('circle',circle)
btand=cv.bitwise_and(resize,resize,mask=circle)
cv.imshow('masked',btand)
cv.waitKey(0)