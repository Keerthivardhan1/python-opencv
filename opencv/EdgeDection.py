import cv2 as cv
import numpy as np

img = cv.imread('photos/person.png')

# def rescaleFrame(frame , scale= 0.5):
#     width=int( frame.shape[1]=scale)
#     height=int(frame.shape[0]=scale)
#     dimansions=(width,height)
#     return cv.resize(frame ,dimansions , interpolation=cv.INTER_AREA)

#fr=rescaleFrame(img)

#cv.imshow('resized',fr)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray" , gray)

lap = cv.Laplacian(gray,cv.CV_64F) 
lap= np.uint8(np.absolute(lap))

# image specific data type ----- uint8

#cv.imshow("Laplasion " , lap)


# solbel

soblex=cv.Sobel(gray,cv.CV_64F, 1 , 0)
sobley=cv.Sobel(gray,cv.CV_64F, 0, 1)
combined_sobel= cv.bitwise_or(soblex,sobley)

cv.imshow('sobelx' , soblex)
cv.imshow('sobely', sobley)
cv.imshow('combined ', combined_sobel)

 

# -----------> canny is most used it the edge dection 

#------>    canny=cv.Canny(gray,125,175)
cv.waitKey(0)
