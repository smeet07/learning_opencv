import cv2 as cv
def resized(frame,scale=0.4):
    height=int(frame.shape[0] *scale)
    width=int(frame.shape[1]*scale)
    dimensions=(height,width)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
img =cv.imread('friends.JPG')
img2=resized(img)
cv.imshow('friends',img)
#to grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray2=resized(gray)
#cv.imshow('grayscale',gray2)
#question what is kernel size
#to blur 
## can increase the kernel to increase the blur but kernel size should be always odd 
blur=cv.GaussianBlur(img2,(7,7),cv.BORDER_DEFAULT)
#cv.imshow('blur',blur)
#to dtect to edges super coool
#to reduce the images pass the blurred image 
canny=cv.Canny(img2,125,175)
#cv.imshow('edges',canny)
#to dialte an image dont know what that means tho
dailted=cv.dilate(canny,(7,7),iterations=1)
#cv.imshow("dont know what this does ",dailted)
#to erode the dialations 
erode=cv.erode(dailted,(3,3),iterations=1)
#cv.imshow('dont know what this this does either ',erode)
#to resize this is much easieer but have to provide the resulting size 
resize=cv.resize(img,(500,500))
cv.imshow('using resized function',resize)
#cropping an image
cropped=resize[200:500,50:150]
cv.imshow('cropped',cropped)
cv.waitKey(0)