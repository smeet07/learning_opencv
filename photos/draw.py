import cv2 as cv
import numpy as np
# 500 and 500 is pixel range 3 is the number of color panels ie rgb
blank=np.zeros((500,500,3),dtype='uint8')
#cv.imshow('blank',blank)
#paint certain area
#blank[200:400,400:500]=0,255,0
#cv.imshow('blank',blank)
cv.rectangle(blank,(0,0),(250,250),(0,255,255),thickness=2)
#cv.imshow('rectangle',blank)
cv.circle(blank,(250,250),40,(0,255,0))
#cv.imshow('circle',blank)
#blank[:]=0,255,255
#cv.imshow('blank',blank)

cv.line(blank,(0,0),(250,250),(0,255,255),thickness=5)
cv.imshow('lets see',blank)
blank1=np.zeros((500,500,3),dtype='uint8')
cv.putText(blank1,'hello',(0,250),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,255),2)
cv.imshow('words',blank1)
cv.waitKey(0)