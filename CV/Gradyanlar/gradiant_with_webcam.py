import cv2

cap = cv2.VideoCapture(0)



while True:
    
    
    ret,frame = cap.read()
    
    frame = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    
    #frame = cv2.Laplacian(frame,ddepth = cv2.CV_16S)
    frame = cv2.Sobel(frame,ddepth = cv2.CV_16S,dx = 0 ,dy = 1,ksize = 5 )
    
    
    if ret == 0:
        break
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    
    cv2.imshow("webcam",frame)
    
    

cv2.destroyAllWindows()
