import cv2

img = cv2.imread("1.png")
print(img)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edged = cv2.Canny(gray,50,200)

cv2.imshow("Edged",edged)

#kontur bulma

contoures , hierarchy = cv2.findContours(edged , cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print("Kontu sayısı:",len(contoures))

#kontur çizdirme
#bulundan konturleri resime çizdiriyoruz

cv2.drawContours(img , contoures , -1 ,(255,0,0),4)

cv2.imshow("contourse",img)



cv2.waitKey(0)
cv2.destroyAllWindows()