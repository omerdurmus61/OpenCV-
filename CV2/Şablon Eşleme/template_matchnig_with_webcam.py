import cv2
import numpy as np

cap = cv2.VideoCapture(0) # 0 bizim default kameramız.

#şablonu yani tamplate aranacak resimi okuduk
template = cv2.imread("python.png",0)

# şablonun boyutlarını aldık
h , w = template.shape

while True:
    
    ret , frame = cap.read()
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    #TM_CCOEFF_NORMED template matching algoritması kullanarak şablon işlemeyi yaptık
    res = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    
    for pt in zip(*loc[::-1]):
        cv2.rectangle(frame,pt,(pt[0] + w , pt[1] + h) , (0,0,255),2)
    
    
    
    cv2.imshow("Webcam",frame)
   
    
    if cv2.waitKey(1) & 0xFF == ord("q") : 
        break

    
cap.release()
cv2.destroyAllWindows()