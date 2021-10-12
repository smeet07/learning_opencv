import cv2 as cv
img=cv.imread('friends.JPG')
resize=cv.resize(img,(500,500))
gray=cv.cvtColor(resize,cv.COLOR_BGR2GRAY)
haar=cv.CascadeClassifier('haar_cascade.xml')
faces=haar.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=8)
print(f'number of faces found {len(faces)}')
for (x,y,w,h) in faces:
    cv.rectangle(resize,(x,y),(x+w,y+h),(0,0,255),thickness=2)
cv.imshow('detect',resize)
cv.waitKey(0)