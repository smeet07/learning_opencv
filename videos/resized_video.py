import cv2 as cv
capture=cv.VideoCapture('abhiyantriki.mp4')
def resized(frame,scale=1.5):
    height=int(frame.shape[0] *scale)
    width=int(frame.shape[1]*scale)
    dimensions=(height,width)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
while True:
    isTrue,frame = capture.read()
    newframe=resized(frame)
    cv.imshow('VIDEO', frame)
    cv.imshow('bigger video',newframe)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
# to change scale of live videos 
#def changeres(height,width):
 #   capture.set(3,width)
  #  capture.set(4,height)
    