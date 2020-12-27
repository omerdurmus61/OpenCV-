import cv2

cap = cv2.VideoCapture(0)

while True:
    
    ret,frame = cap.read()
    
    if ret == 0:
        break
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

# threshold yöntemleri
    
    #_ , frame = cv2.threshold(frame , thresh = 60 , maxval=255 , type = cv2.THRESH_BINARY)
    #_ , frame = cv2.threshold(frame , thresh = 60 , maxval=255 , type = cv2.THRESH_BINARY_INV)
    #_ ,frame = cv2.adaptiveThreshold(frame,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,8)
    #frame = cv2.adaptiveThreshold(frame,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    frame = cv2.adaptiveThreshold(frame,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

    
    cv2.imshow("webcam",frame)
    
    

cv2.destroyAllWindows()

