import cv2
import numpy as np

cap = cv2.VideoCapture(0)


while True:
    
    ret , frame = cap.read()
    
    if ret == 0:
        break
    
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    corners = cv2.goodFeaturesToTrack(frame,120,0.08,10)
    
    corners = np.int0(corners)
    
    for corner in corners:
        
        x,y = corner.ravel()
        
        
        cv2.circle(frame,(x,y),5,(0,255,0),-1)
    
    cv2.imshow("webcam",frame)
 
    
    if cv2.waitKey(1) & 0xFF == ord("q") : break 

    
cap.release()
cv2.destroyAllWindows()