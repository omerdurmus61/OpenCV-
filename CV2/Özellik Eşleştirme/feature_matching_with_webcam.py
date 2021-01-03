import cv2


cap = cv2.VideoCapture(0)

img = cv2.imread("python.png",0)

# orb tanımlayıcısı
#köşe - kenar gibi nesneye ait özellikler
orb = cv2.ORB_create()

while True:
    
    ret , frame = cap.read()
    
    
    if ret == 0:
        break
    
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    #anahtar tespiti
    kp1 , dest1 = orb.detectAndCompute(img,None)
    kp2 , dest2 = orb.detectAndCompute(frame,None)
    
    #bf matcher
    bf = cv2.BFMatcher(cv2.NORM_HAMMING)
    
    
    #noktaları eşleştir

    matches = bf.match( dest1 , dest2 )
    
    #mesafeye göre sıralama

    matches = sorted(matches , key = lambda x: x.distance)
    
    img_match = cv2.drawMatches(img , kp1 ,frame ,kp2 , matches[:20],None,flags = 2)
    
    
    cv2.imshow("Webcam",img_match)
   
    
    if cv2.waitKey(1) & 0xFF == ord("q") : break

    
cap.release()
cv2.destroyAllWindows()