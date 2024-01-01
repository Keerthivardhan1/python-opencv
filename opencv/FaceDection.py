import cv2 as cv

img=cv.imread('photos/group2.jpg')

#cv.imshow("picture", img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray" , gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect= haar_cascade.detectMultiScale(gray , scaleFactor=1.1 , minNeighbors=1)   # This will Returen the Rectengle Cordinates of the detected faces ie it will returen the co-ordinates of x, y, w, h 

print("number of faces found = : " , len(faces_rect))


# printing the rectangle border around the faces found 
for(x,y,w,h) in faces_rect:
    cv.rectangle(img , (x,y) , (x+w , y+h), (0, 255, 0), thickness=3 )

cv.imshow("Detected face" , img)

cv.waitKey(0)

#harr cascade is not effective to use 

# for advance projects we use dealings face recognizer 
