import cv2
from datetime import datetime
cap =  cv2.VideoCapture(0)

while(True):
    ret , img = cap.read()
    # print(type(img))
    cv2.imshow("myimg" , img)
    key = cv2.waitKey(10)
    if (key == ord("q")):
        break
    if (key == ord("c")):
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d--%H-%M-%S")
        print(date_time)
        name = date_time + ".png"
        cv2.imwrite("{}.png".format(date_time) , img)
        # cv2.imwrite(name , img)
        print("Saved snapshot:", "{}.png".format(date_time))


cv2.destroyAllWindows()