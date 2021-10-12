import  cv2 as cv
img=cv.imread('friends.JPG')
resize=cv.resize(img,(500,500))
b,g,r=cv.split(resize)
#th eparts which are more blue in color will be shown lighter and other parts will be shown darker
cv.imshow('b',b)
cv.imshow('g',g)
cv.imshow('r',r)
merged=cv.merge([b,g,r])
cv.imshow('merge',merged)
cv.waitKey(0)