import cv2
import numpy as np

img = cv2.imread("kart.png")
cv2.imshow("orijinal",img)

width = 400
height = 500

pts1 = np.float32([[203,1],[1,472],[540,150],[338,617]])
pts2 = np.float32([[0,0],[0,height],[width,0],[width,height]])

matris = cv2.getPerspectiveTransform(pts1,pts2)
print(matris)

#nihai resim
imgOutput = cv2.warpPerspective(img,matris,(width,height))
cv2.imshow("Nihai resim",imgOutput)

cv2.imwrite("duz_hali.png",imgOutput)

cv2.waitKey(0)
cv2.destroyAllWindows()