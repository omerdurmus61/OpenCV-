import cv2
import numpy as np
from collections import deque
#tespit edilen objenin merkezini depolamak i.in deque kullanılır

buffer_size = 16
pts = deque(maxlen=buffer_size)

# mavi renk aralığı HSV
blueLower = np.array([84,98,255])
blueUpper = np.array([179,255,255])


cap = cv2.VideoCapture(0)
#kamera boyutlarını değiştirmek için
cap.set(3,1020)
cap.set(4,480)

while True:
    
    ret , imgOriginal = cap.read()
    
    if ret == 0:
        break
    
    #blur 
    blurred = cv2.GaussianBlur(imgOriginal,(11,11),0)
    
    #hsv
    
    hsv = cv2.cvtColor(blurred , cv2.COLOR_BGR2HSV)
    
    cv2.imshow("HSV Image",hsv)
    
    
    #mavi için maske
    
    mask = cv2.inRange(hsv,blueLower,blueUpper)
    
    #maskedeki gürültüyü silmek için erozyon ve genişleme uyguladık
    
    mask = cv2.erode(mask,None,iterations = 2)
    
    mask = cv2.dilate(mask,None,iterations = 2)
    
    cv2.imshow("Mask",mask)
    
    
    # kontur
    
    contours, _ = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)  
    
    center = None
    
    if len(contours) > 0 :
        
        #en büyük konturu aldım
        
        c = max(contours,key = cv2.contourArea)
        
        # dikdörtgene çevir
    
        rect = cv2.minAreaRect(c)

        ((x,y),(width,heigth),rotation) = rect
        
        
        #değişkenlerin durumunu bastırma işlemi. np.round sayı basamaklarını yuvarlar çok fazla basamak olmasın diye 
        s = "x : {} y: {} width = {} height = {} rotation = {}".format(np.round(x),np.round(y),np.round(width),np.round(heigth),np.round(rotation))
        
        print(s)
        
        
        #kutucuk rect'te elde ettiğim kordinatlarla kutucuk yapıyoruz
        box = cv2.boxPoints(rect)
        box = np.int64(box)
        
        #moment => merkezi bulmaya yaraıyor
        
        M = cv2.moments(c)
        center = ( int(M["m10"]/M["m00"]), int (M["m01"]/M["m00"]))

        
        # konturu çizdirelim

        cv2.drawContours(imgOriginal,[box],0,(0,255,255),2)
        
        #merkeze nokta çizdirelim
        
        cv2.circle(imgOriginal,center,5,(255,0,255),-1)
        
        #bilgileri ekrana yazdıralım
        
        cv2.putText(imgOriginal,s,(50,50),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,0),2)
        
    
    
    #degue
    pts.appendleft(center)
    
    
    for i in range(1,len(pts)):
        
        if pts[i-1] is None or pts[i] is None : continue
    
    
        cv2.line(imgOriginal,pts[i-1],pts[i],(0,255,0))
    
    cv2.imshow("Original Detection",imgOriginal)
    
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    
cap.release()
cv2.destroyAllWindows()