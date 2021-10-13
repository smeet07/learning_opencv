import os
import cv2 as cv
import numpy as np
people=['michael scott','ronaldo','scarlett','steph curry','virat kohli']
p=[]
dir=r'C:\Users\Dell\opencv\photos\faces'
haar=cv.CascadeClassifier('haar_cascade.xml')
features=[]
labels=[]
def train_faces():
    for person in people:
        path=os.path.join(dir,person)
        label=people.index(person)
        for img in os.listdir(path):
            img_path=os.path.join(path,img)
            img_array=cv.imread(img_path)
            gray=cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            faces_rect=haar.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)
            for (x,y,w,h) in faces_rect:
                faces_roi=gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)
train_faces()
print('training done---')
features=np.array(features,dtype='object')
labels=np.array(labels)
recognizer=cv.face.LBPHFaceRecognizer_create()
recognizer.train(features,labels)
recognizer.save('face_trained.yml')
np.save('features.npy',features)
np.save('labels.npy',labels)
