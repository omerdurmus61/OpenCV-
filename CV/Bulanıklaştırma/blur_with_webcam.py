import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Gürültü oluşturan fonksiyon oluşturuldu

ret,frame = cap.read()
    
def gausianNoise(image):
    
    row , col ,ch =frame.shape
    
    mean = 0
    
    var = 0.05
    
    sigma = var**0.5
    
    gauss = np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    
    noisy = image + gauss
    
    return noisy

# 



while True:
    
    
    ret,frame = cap.read()
    
    # Görüntü gürültü ile birleştirilmek için normalize edildi
    
    frame = frame / 255
    
    #Görüntüye gürültü uygulandı . Gürültülü görüntü elde edildi.
    # Karşılaştırma için gürültülü hali gösterildi
    gaussianNoisyImage = gausianNoise(frame)
    cv2.imshow("Gaussian Noisy",gaussianNoisyImage)
    
    if ret == 0:
        break
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    
    # Gürültüyü düzeltmek için bulanıklaştırma kullanıldı
    #frame = cv2.blur(frame, ksize = (3,3))
    frame = cv2.GaussianBlur(frame,ksize = (3,3),sigmaX = 7)
    #frame = cv2.medianBlur(frame, ksize = 3)
    
    
    #Bulanıklaştırma ile düzeltilen görüntü gösterildi
    cv2.imshow("With blur",frame)
    
    

cv2.destroyAllWindows()

