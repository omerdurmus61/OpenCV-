import cv2

cap = cv2.VideoCapture(0)

hog = cv2.HOGDescriptor()

hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

while True:
    
    ret , frame = cap.read()
    
    (rects,weights) = hog.detectMultiScale(frame, padding = (8,8), scale = 1.05)

    for (x,y,w,h) in rects:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)


    cv2.imshow("detection",frame)

    if cv2.waitKey(1) & 0xFF == ord("q") :
        break

    
cap.release()
cv2.destroyAllWindows()