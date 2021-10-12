import cv2 as cv
img=cv.imread('friends.JPG')
resize=cv.resize(img,(500,500))
gray=cv.cvtColor(resize,cv.COLOR_BGR2GRAY)
thresh,threshold=cv.threshold(gray,140,255,cv.THRESH_BINARY)
# for inverse do thresh,threshold=cv.threshold(gray,140,255,cv.THRESH_BINARY_inv) whatever values are less than 140b gets set to 255
thresh,thresh_inv=cv.threshold(gray,140,255,cv.THRESH_BINARY_INV)
cv.imshow('thresh_inv',thresh_inv)
cv.imshow('basic threshhold',threshold)
#adaptive threshholding
#it takes a block of pixels 11 by 11 finds their mean and sets that to optimal threshhold 
adaptive=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,5,0)
cv.imshow('adaptive',adaptive)
cv.waitKey(0)