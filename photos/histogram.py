#histogram shows the the range of color pixels and the number of the pixels for each value in that range
# on x axis the values are present and on the y axis percentage 
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
img=cv.imread('friends.JPG')
resize=cv.resize(img,(500,500))
blank=np.zeros((500,500),dtype='uint8')
circle=cv.circle(blank,(resize.shape[1]//2,resize.shape[0]//2),200,255,-1)
gray=cv.cvtColor(resize,cv.COLOR_BGR2GRAY)
btand=cv.bitwise_and(gray,gray,mask=circle)
cv.imshow('masked',btand)
grayhist=cv.calcHist([gray],[0],btand,[256],[0,256])
plt.figure()
plt.title('gray histogram')
plt.xlabel('bins')
plt.ylabel('intensity')
#plt.xlim([0,256])
plt.plot(grayhist)
plt.show()
