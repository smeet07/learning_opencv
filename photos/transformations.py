import cv2 as cv
import numpy as np
img=cv.imread('friends.JPG')
resize=cv.resize(img,(500,500))
def transalted(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimesions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimesions)
# positive x is moving right 
#negative x is moving left
# positive y is moving down idk why they wouldnt follow axes
#negative y is moving up

transalte=transalted(resize,100,-100)
#cv.imshow('translation',transalte)
# rotate an image
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]
    if rotPoint==None:
        rotPoint=(height//2,width//2)
    rotmatrix=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)
    return cv.warpAffine(img,rotmatrix,dimensions)
# it rotates counter clockwise
# bif you rotated it again then there will be skewed image formed because after first rotation black portions
# will be generated and second rotations will consider them too 
rotation=rotate(resize,50)
#cv.imshow('rotation',rotation)

#to flip an image
#0 means flipping vertically 
#1 means flipping horizontally
#-1 means flipping both vertically and horizontally
flipped=cv.flip(resize,0)
cv.imshow('flipped',flipped)
cv.waitKey(0)