import cv2
import numpy as np

cap = cv2.VideoCapture(0)


while True:
    
    ret , frame = cap.read()
    
    if ret == 0:
        break
    
    frame = cv2.flip(frame,1)
    
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lower_green = np.array([84,179,0],np.uint8)
    upper_green = np.array([179,255,255],np.uint8)
    
    
    #maske
    
    mask = cv2.inRange(hsv,lower_green,upper_green)
    
    #maskeyi kendi renginde görmek için
    
    blue = cv2.bitwise_and(frame,frame, mask = mask)
    
    
    cv2.imshow("Blue Mask",blue) 
    
    cv2.imshow("Mask",mask)    

    cv2.imshow("webcam",frame)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

cap.release()
cv2.destroyAllWindows()