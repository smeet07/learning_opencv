import cv2 as cv
import numpy as np
img=cv.imread('friends.JPG')
resize=cv.resize(img,(500,500))
gray=cv.cvtColor(resize,cv.COLOR_BGR2GRAY)
lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow('lap',lap)
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
sobel=cv.bitwise_or(sobelx,sobely)
#cv.imshow('Sobel X',sobelx)
#cv.imshow('Sobel Y',sobely)
cv.imshow('sobel',sobel)
canny=cv.Canny(gray,140,170)
cv.imshow('canny',canny)
cv.waitKey(0)

