
import cv2 as cv

img = cv.imread('photos/person.png')

cv.imshow('person', img)

blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)

#cv.imshow('blur',blur)

canny=cv.Canny(img,125,175)

#cv.imshow('canny',canny);

blurrcanny=cv.Canny(blur,125,175)

#cv.imshow('blurrcanny ', blurrcanny)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#cv.imshow('gray',gray)

hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV_FULL)
cv.imshow('hsv',hsv)


#def rescaleFrame(frame,scale=0.75):

# capture=cv.VideoCapture('photos/video.mp4')

# while True:
#     isTrue , frame =capture.read()
#     cv.imshow('video',frame)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()


# webcam -- 0 
# first cam --1
# secound cam -- 2

cv.waitKey(0)


