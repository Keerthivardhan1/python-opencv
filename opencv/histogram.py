import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('photos/person.png')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('grayperson', gray)

gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])

plt.figure()
plt.title('gray scale histogram')
plt.xlabel('bins')
plt.ylabel('no of pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()


plt.figure()

cv.waitKey(0)
