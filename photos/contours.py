#contours are like edges but only for objects  like boundaries of objects 
import cv2 as cv
import numpy as np

img=cv.imread('friends.JPG')
dimesnions=img.shape[:2]
#cv.imshow('normal',img )
resized=cv.resize(img,(500,500))
blank=np.zeros(resized.shape,dtype='uint8')
#cv.imshow('resized',resized)
gray=cv.cvtColor(resized,cv.COLOR_BGR2GRAY)
#cv.imshow('gray',gray)
canny=cv.Canny(gray,125,175)
#cv.imshow('canny',canny)
#if the intenisty of the image is greater than 125 it will set to white else zero
ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('thresh',thresh)
contour,hierarchies=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
#since we want to print all the contours thats why -1
cv.drawContours(blank,contour,-1,(255,0,0,),1)
cv.imshow('blank',blank)
print(f'{len(contour)} contours were fopund')
#if theres too many contours then you can apply gaussian blur to the iamge them pass the image to canny 
cv.waitKey(0)