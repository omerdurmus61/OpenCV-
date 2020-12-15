import cv2
import numpy as np

def nothing(x):
    pass


img = np.zeros((512,512,3),np.uint8)

cv2.namedWindow("pencere")

cv2.createTrackbar("R","pencere",0,255,nothing)
cv2.createTrackbar("G","pencere",0,255,nothing)
cv2.createTrackbar("B","pencere",0,255,nothing)

switch = "0 : OFF , 1 : ON"

cv2.createTrackbar(switch,"pencere",0,1,nothing)

while True:

    cv2.imshow("pencere",img)
    if cv2.waitKey(1) & 0xFF == "q":
        break
 
    r = cv2.getTrackbarPos("R","pencere")
    g = cv2.getTrackbarPos("G","pencere")
    b = cv2.getTrackbarPos("B","pencere")

    s= cv2.getTrackbarPos(switch,"pencere")


    if s == 0:

        img[:]=[0,0,0]

    if s == 1:

        img[:]= [b,g,r]

cv2.destroyAllWindows()




