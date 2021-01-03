import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("chocolates.jpg",0)
plt.figure(),plt.imshow(img1,cmap = "gray"),plt.axis("off")

img2 = cv2.imread("nestle.jpg",0)
plt.figure(),plt.imshow(img2,cmap = "gray"),plt.axis("off")

# orb tanımlayıcısı
#köşe - kenar gibi nesneye ait özellikler
orb = cv2.ORB_create()

#anahtar tespiti
kp1 , dest1 = orb.detectAndCompute(img2,None)
kp2 , dest2 = orb.detectAndCompute(img1,None)

#bf matcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING)

#noktaları eşleştir

matches = bf.match( dest1 , dest2 )

#mesafeye göre sıralama

matches = sorted(matches , key = lambda x: x.distance)

#eşleşen resimleri görselleştirelim

plt.figure()
img_match = cv2.drawMatches(img2 , kp1 ,img1 ,kp2 , matches[:20],None,flags = 2)
plt.imshow(img_match),plt.axis("off"),plt.title("orb")


#sift tanımlayıcısı

sift = cv2.xfeatures2s.SHIFT_create()

#bf 
bf = cv2.BFMatcher()

#anahtar nokta(feature) tespiti sift ile
kp1 , des1 = sift.detectAndCompute(img2,None)
kp2 , des2 = sift.detectAndCompute(img1,None)

matches = bf.knnMatch(des1 , des2 , k = 2)

guzel_eslesme = []

for match1 , match2 in matches:
    
    if match1.distance < 0.75 * match2.distance:
        guzel_eslesme.append([match1])
        
        
plt.figure()
sift_matches = cv2.drawMatchesKnn(img2,kp1,img1,kp2,guzel_eslesme,None,flags = 2)
plt.imshow(sift_matches),plt.axis("off"),plt.title("sift")


