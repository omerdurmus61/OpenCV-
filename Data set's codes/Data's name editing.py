import os

path = os.chdir("C:/Users/Ömer/Desktop/veriler/")

i = 0

for file in os.listdir(path):
    
    new_name = f"{i}.png"
    os.rename(file , new_name)
    
    i = i + 1
    
