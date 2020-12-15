import cv2
import numpy as np
import requests

url = "http://192.168.1.21:8080//shot.jpg"

while True:

    imgResp = requests.get(url)

    imgArr = np.array(bytearray(imgResp.content), dtype=np.uint8)

    img = cv2.imdecode(imgArr,cv2.IMREAD_COLOR)

    img = cv2.resize(img,(640,480))

    cv2.namedWindow("android kamera",cv2.WINDOW_NORMAL)

    cv2.imshow("android kamera",img)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
