import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
img=cv.imread('friends.JPG')
resize=cv.resize(img,(500,500))
cv.imshow('resize',resize)

plt.figure()
plt.title('color histogram')
plt.xlabel('bins')
plt.ylabel('intensity')
colors=('b','g','r')
for i,col in enumerate(colors):
    hist=cv.calcHist([resize],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()
cv.waitKey(0)