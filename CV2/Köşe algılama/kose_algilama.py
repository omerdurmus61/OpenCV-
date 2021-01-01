import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("sudoku.jpg",0)
img = np.float32(img)
print(img.shape)
plt.figure(),plt.imshow(img,cmap = "gray"),plt.axis("off")

# Köşe algılama


# harris corner detection
#   = cv2.cornerHarris( resim , komşuluk boyutu , kernel size , harris detection önteminin free parametrelerinden biri)
dst = cv2.cornerHarris( img , blockSize = 2 , ksize = 3 , k = 0.04 )
plt.figure(),plt.imshow(dst,cmap = "gray"),plt.axis("off")

# tespitedilen noktaları genişlettim ( dstler genişledi)

dst = cv2.dilate(dst,None)
img[dst > 0.2*dst.max()] = 1
plt.figure(),plt.imshow(dst,cmap = "gray"),plt.axis("off")


# shi tomasi detection
img = cv2.imread("sudoku.jpg",0)
img = np.float32(img)
#   = cv2.cornerHarris(resim,kaç köşe tespit edilsin,quality level , min distance ( iki köşe arası min mesafe))
corners = cv2.goodFeaturesToTrack(img,120,0.01,10)
corners = np.int64(corners)

# tespit edilen köşelere daire çizdirdik

for i in corners:
    x,y =i.ravel()
    cv2.circle(img,(x,y),3,(125,125,125),cv2.FILLED)
    
plt.figure(),plt.imshow(img,cmap = "gray"),plt.axis("off")
