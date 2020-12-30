import cv2
import numpy as np

cap = cv2.VideoCapture(0)


while True:
    
    ret , frame = cap.read()
    
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    #threshold için en mantıklı değer resmin medyanıdır
    med_val = np.median(frame)
    
    # low ve high threshold için riteratürde şöyle bir kullanım vardır.

    low = int(max(0,(1 - 0.33)*med_val))

    high = int(min(255,(1 + 0.33)*med_val))
    
  
    frameEdges = cv2.Canny(image = frame,threshold1 = low, threshold2=high)
    
    if ret == 0:
        break
    
    
    cv2.imshow("Webcam",frameEdges)
   
    
    if cv2.waitKey(1) & 0xFF == ord("q") : break

    
cap.release()
cv2.destroyAllWindows()