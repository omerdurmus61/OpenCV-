import cv2

cap = cv2.VideoCapture(0)#0 yazınca webcam kullanılır video ismi de girilebilir.

while True:

    ret , frame = cap.read()

    if ret == 0: # videolar sonsuz olmadığı için video bittiğinde ret = 0 olur video açarsak bunu koymalıyız
        break

    frame = cv2.flip(frame,1)# 1 y eksenine göre , 0 x eksenine göre simetrisini alır

    cv2.namedWindow("pc kamera",cv2.WINDOW_NORMAL)
    cv2.imshow("pc kamera",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release() #işlem durdurma

cv2.destroyAllWindows()

