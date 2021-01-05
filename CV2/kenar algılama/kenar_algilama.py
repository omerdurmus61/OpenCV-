import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("london.jpg",0)
plt.figure(),plt.imshow(img,cmap="gray"),plt.axis("off")

#Canny algoritması

edges = cv2.Canny(image = img,threshold1 = 0, threshold2=255)
plt.figure(),plt.imshow(edges,cmap="gray"),plt.axis("off")

#threshold için en mantıklı değer resmin medyanıdır
med_val = np.median(img)
print(med_val)

# low ve high threshold için literatürde şöyle bir kullanım vardır.

low = int(max(0,(1 - 0.33)*med_val))

high = int(min(255,(1 + 0.33)*med_val))

print(low)
print(high)

edges = cv2.Canny(image = img,threshold1 = low, threshold2= high)
plt.figure(),plt.imshow(edges,cmap="gray"),plt.axis("off")

 #blur işlemiden sonra kenar tespiti yapmayı deneyelim ilk önce blur sonra tekrar aynı işlemler
 
blurred_img = cv2.blur(img , ksize=(5,5))
plt.figure(),plt.imshow(blurred_img,cmap="gray"),plt.axis("off")

med_val = np.median(blurred_img)
print(med_val)

low = int(max(0,(1 - 0.33)*med_val))

high = int(min(255,(1 + 0.33)*med_val))

print(low)
print(high)

edges = cv2.Canny(image = blurred_img,threshold1 = low, threshold2= high)
plt.figure(),plt.imshow(edges,cmap="gray"),plt.axis("off")
