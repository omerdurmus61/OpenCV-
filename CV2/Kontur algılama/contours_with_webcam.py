import cv2

cap = cv2.VideoCapture(0)


while True:
    
    ret , frame = cap.read()
    
    if ret == 0:
        break
    
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    edged = cv2.Canny(frame,50,200)
    
    #kontur bulma

    contoures , hierarchy = cv2.findContours(edged , cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    #kontur çizdirme
    
    #konturleri renkli çizebilmek için tekrar renkli görüntü yaptım
    
    frame = cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)

    cv2.drawContours(frame , contoures , -1 ,(255,0,0),2)

    cv2.imshow("contourse",frame)
    
   
 
    if cv2.waitKey(1) & 0xFF == ord("q") : break

    
cap.release()
cv2.destroyAllWindows()