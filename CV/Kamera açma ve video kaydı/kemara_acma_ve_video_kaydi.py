import cv2

# capture 
cap = cv2.VideoCapture(0) # 0 bizim default kameramız.

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(width,height)


# video kaydetme aracı

writer = cv2.VideoWriter("video_kaydı.mp4",cv2.VideoWriter_fourcc(*"DIVX"),20,(width,height)) 

# cv2.VideoWriter_fourcc(*"DIVX") = çerçeveleri sıkıştıran 4 karakterli codec kodu *"DIVX" windows için.
# 20 değeri saniyelik frame sayısı
# (width,height) çerçeve boyutu

while True:
    
    ret , frame = cap.read()
    
    cv2.imshow("Video",frame)
    #save
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q") : break

    
cap.release()
writer.release()
cv2.destroyAllWindows()