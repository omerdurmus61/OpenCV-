import cv2
import matplotlib.pyplot as plt

#bgr formatını rgb formatına çevirdik
img1 = cv2.imread("img1.jpg")
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img2 = cv2.imread("img2.jpg")
im21 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)


print(img1.shape)
print(img2.shape)

#aynı boyuta getirdik
img1 = cv2.resize(img1,(600,600))
print(img1.shape)

img2 = cv2.resize(img2,(600,600))
print(img1.shape)


plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

# karıştırılmış resim = alpha * img1 + beta*img2 -----> Denklemimiz

blended = cv2.addWeighted(src1 = img1, alpha = 0.5 ,src2 = img2 , beta = 0.5,gamma=0)

# alpha = 0 beta = 1 olursa img2 gözükür tamtersi olursa img1 katsayılar ile orantılı olarak birleşirler.

plt.figure()
plt.imshow(blended)


cv2.imwrite("blendedImg.jpg",blended)