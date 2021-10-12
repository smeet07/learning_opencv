import cv2 as cv
import numpy as np
img=np.zeros((400,400),dtype='uint8')
rect=cv.rectangle(img.copy(),(20,20),(380,380),255,-1)
circle=cv.circle(img.copy(),(200,200),200,255,-1)
btand=cv.bitwise_and(rect,circle)
cv.imshow('and',btand)
btor=cv.bitwise_or(rect,circle)
cv.imshow('or',btor)
btxor=cv.bitwise_xor(rect,circle)
cv.imshow('xor',btxor)
btnot=cv.bitwise_not(circle)
cv.imshow('not',btnot)
cv.waitKey(0)
