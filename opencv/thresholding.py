import cv2 as cv
import numpy as np

# convert to binarey image(image with pixels are 0 i.e black or 1 i.e white )

img = cv.imread('photos/person.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('gray',gray)

threshold , thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)

# hear thresh holds the thresholded image

cv.imshow('sample ' , thresh)

threshold, thresh_inv=cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow(" inverse ", thresh_inv)

# apative threshsholding 

cv.waitKey(0)

