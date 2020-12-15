import cv2

img = cv2.imread("dr_strange.jpg")
#img = cv2.imread("/home/omercandurmus/cv/dr_strange.jpg") Adres girmek için
#img = cv2.imread("dr_strange.jpg",0) #Gri şekilde okumak için

#print(img)

cv2.namedWindow("pencere",cv2.WINDOW_NORMAL)

cv2.imshow("pencere",img)

cv2.imwrite("dr_strange.jpg",img)
# cv2.imwrite("home/omercandurmus/cv/dr_strange.jpg",img)

cv2.waitKey(0)

cv2.destroyAllWindows()



