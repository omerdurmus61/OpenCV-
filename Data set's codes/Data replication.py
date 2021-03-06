import cv2
import os
import numpy as np

path = os.chdir("C:/Users/Ömer/Desktop/veriler/")

i = 0

#kernel size değişebilir
kernel = np.ones((2,2),dtype = np.uint8)

for file in os.listdir(path):
    
    img = cv2.imread(file)
    
    
    #Blur
    img = cv2.blur(img,ksize = (5,5))
    
    #Genişletme
    #img = cv2.dilate(img,kernel,iterations = 1)
    
    #Erozyon 
    #img = cv2.erode(img,kernel,iterations = 1)
    
    
    cv2.imwrite(f"veri{i}.png",img)
    
    i = i + 1
    
    
    
    
    

