import cv2
import matplotlib.pyplot as plt

img = cv2.imread("img1.jpg")

img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

plt.figure()
plt.imshow(img,cmap="gray")
plt.axis("off")
plt.title("image")
plt.show()

# eşikleme
#              = cv2.threshold(resim, min değer,max değer, eşikleme yöntemi)  
_ , thresh_img = cv2.threshold(img , thresh = 60 , maxval=255 , type = cv2.THRESH_BINARY) # 60 ile 255 arasını beyaz yapar => cv2.TRESH_BINARY = açar , beyaz yapar


plt.figure()
plt.imshow(thresh_img,cmap ="gray")
plt.axis("off")
plt.title("thresh bınary")
plt.show()

_ , thresh_img2 = cv2.threshold(img , thresh = 60 , maxval=255 , type = cv2.THRESH_BINARY_INV) # 60 ile 255 arasını siyah yapar => cv2.TRESH_BINARY_INV = kapar , siyah yapar

plt.figure()
plt.imshow(thresh_img2,cmap ="gray")
plt.axis("off")
plt.title("thresh binary inverse")
plt.show()

# adaptif eşikleme , uyarlamalı eşikleme
#ışıktan dolayı ayrı gözüken birleşik bölgelerin ayrılmamasını sağlar.

# ortalama yöntemi
#           = cv2.adaptiveThreshold(resim , max değer,eşikleme algoritması (yöntem), eşikleme yöntemi , 11(blok size) , 8 (ortalamadan gelen sabit))
thresh_img3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,8)

plt.figure()
plt.imshow(thresh_img3,cmap ="gray")
plt.axis("off")
plt.title("adaptive threshold mean")
plt.show()

# gauss yöntemi

thresh_img4 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

plt.figure()
plt.imshow(thresh_img4,cmap ="gray")
plt.axis("off")
plt.title("adaptive threshold gaussian")
plt.show()