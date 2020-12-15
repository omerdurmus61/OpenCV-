import cv2
import numpy as np


canvas = np.zeros((512,512,3), dtype = np.uint8) + 255  # zeros iile 0 lar matrisi oluşturdum 2255 ekledim bgr kodu ile beyazı elde ettim

cv2.imshow("pencere",canvas)
cv2.waitKey(0)
v2.destroyAllWindows()