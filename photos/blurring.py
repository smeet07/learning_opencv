import cv2 as cv
img=cv.imread('friends.JPG')
resize=cv.resize(img,(500,500))
#average blur or blur sets the intensity of the pixel as an average of surrounding pixels
#the more the kernel size the more the blurring will be 
avgblur=cv.blur(resize,(7,7))
cv.imshow('average', avgblur)
#gaussian blur does similar thing to average blur the difference being each surrounding pixel has a weight multiplied 
#gaussian blurr looks more natural compared to average blur
gaussian=cv.GaussianBlur(resize,(7,7),0)
cv.imshow('gaussian',gaussian)
#medianblur is used in advanced cv projects as its better at removing noises
#median is kinds like smudge tbh
median=cv.medianBlur(resize,7)
cv.imshow('median',median)
#i like the concept of bilateral because it essentially blurs the image but also retians the edges
# sigma space is the max distance of the kernel surrounding the concerned pixel which will influence the concerned kernel
# sigmas color is similar to space ,the higher the value of sigma color denotes the surrpounding colors will influence 
#the concerned pixels more
blt=cv.bilateralFilter(resize,15,50,50)
cv.imshow('billateral',blt)

cv.waitKey(0)