import cv2 as cv
img=cv.imread('friends.JPG')
resize=cv.resize(img,(500,500))
#you can convert gray,rgb,hsv to bgr too but cant directly convert gray to hsv 
gray=cv.cvtColor(resize,cv.COLOR_BGR2GRAY)
hsv=cv.cvtColor(resize,cv.COLOR_BGR2HSV)
rgb=cv.cvtColor(resize,cv.COLOR_BGR2RGB)

cv.imshow('hsv',hsv)
cv.waitKey(0)