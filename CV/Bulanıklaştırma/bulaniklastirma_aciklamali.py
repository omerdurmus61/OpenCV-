import cv2
import matplotlib.pyplot as plt
import numpy as np # gürültü oluşturmak için

import warnings#uyarıları kapama
warnings.filterwarnings("ignore")


#blurring (detay azalır,gürültüyü engeller)

img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("orijinal"),plt.show()




# Ortalama Bulanıklaştırma 
# gezen hücrenin altındaki piksellerin ortalamasını alır merkeze yazar

dst2 = cv2.blur(img, ksize = (3,3))

plt.figure(),plt.imshow(dst2),plt.axis("off"),plt.title("Ortalama Blur"),plt.show() #opencv'de girdilere src çıktılara dst denir


# Gussian Bulanıklaştırma
# Resimdeki gauss noise varsa onu alır. Gezen gauss çekirdeğindeki x ve y yönündeki sigma değerlerine göre işlemler yapılıyor.

gb =cv2.GaussianBlur(img,ksize = (3,3),sigmaX = 7) # y yönündeki sigma yazılmaz ise direk x yönündekine eşit kabuledilir
plt.figure(),plt.imshow(gb),plt.axis("off"),plt.title("Gauss Blur"),plt.show()

# Medyan Blur
# Gezen hücrenin içindeki kutular düzleştirilir vektör elde edilir ortadaki sayı medayandır. O medyanı alıp kutumuzun merkezindeki pikselin genliğine yazılır.

mb  = cv2.medianBlur(img, ksize = 3)
plt.figure(),plt.imshow(mb),plt.axis("off"),plt.title("Medyan Blur"),plt.show()


# Noise oluşturma

def gausianNoise(image):
    
    row , col ,ch =img.shape
    
    mean = 0
    
    var = 0.05
    
    sigma = var**0.5
    
    gauss = np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    
    noisy = image + gauss
    
    return noisy




# Gürültüyü eklemek için normalize etmeliyiz
img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) / 255 # normalize ettim.

plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("Normalize edilmiş"),plt.show()



gaussianNoisyImage = gausianNoise(img)

plt.figure(),plt.imshow(gaussianNoisyImage),plt.axis("off"),plt.title("Gaussian Noisy"),plt.show()


# Gauss noise elde edildi resme uygulandı şimdi gauss blur ile onu düzeltelim.

#gauss blur


gb2 =cv2.GaussianBlur(gaussianNoisyImage,ksize = (3,3),sigmaX = 7)
plt.figure(),plt.imshow(gb2),plt.axis("off"),plt.title("With Gauss Blur"),plt.show()




# Tuz ve Karabiber gürültüsü

def saltPepperNoise(image):
    
    row,col,ch = image.shape
    
    s_vs_p = 0.5
    
    amount = 0.004
    
    noisy = np.copy(image)
    
    #salt beyaz noktalar
    
    num_salt = np.ceil(amount + image.size * s_vs_p)
    coords = [np.random.randint(0 , i-1, int(num_salt) ) for i in image.shape]
    noisy[coords] = 1


    #pepper siyah

    num_pepper = np.ceil(amount + image.size * (1-s_vs_p))
    coords = [np.random.randint(0 , i-1, int(num_pepper )) for i in image.shape]
    noisy[coords] = 0
    
    return noisy



spImage = saltPepperNoise(img)

plt.figure(),plt.imshow(spImage),plt.axis("off"),plt.title("SP Image"),plt.show()


#medyan blur ile bunu düzeltelim


mb2  = cv2.medianBlur(spImage.astype(np.float32), ksize = 3)

plt.figure(),plt.imshow(mb2),plt.axis("off"),plt.title("With Medyan Blur"),plt.show()









