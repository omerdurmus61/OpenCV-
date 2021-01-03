import cv2

cap = cv2.VideoCapture(0)



while True:
    
    ret , frame = cap.read()
    
    #bluring
    img_blur = cv2.medianBlur(frame,13)
    
    #gray scale
    img_gray = cv2.cvtColor(img_blur,cv2.COLOR_BGR2GRAY)

    #binary threshold
    _,img_thresh = cv2.threshold(img_gray,75,255,cv2.THRESH_BINARY)


    # kontur
    contours,hierarchy = cv2.findContours(img_thresh.copy(),cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)

    for i in range(len(contours)):
    
        if hierarchy[0][i][3] == -1:
            cv2.drawContours(frame,contours,i,(255,0,0),2)

    cv2.imshow("webcam",frame)


    
    if cv2.waitKey(1) & 0xFF == ord("q") : break

    
cap.release()
cv2.destroyAllWindows()