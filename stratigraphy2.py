import cv2
import numpy as np

# img = cv2.line(img, (0,90), (500,90), (255,0,0), 2)
# img = cv2.line(img, (600,90), (1021,90), (0,255,0),2)
# sobelx = cv2.Sobel(img, -1, dx=1, dy=0, ksize=3, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)
# sobelxy = sobelx + sobely
# cv2.imshow("sobelx", sobelx)
# cv2.imshow("sobelxy", sobelxy)
# #High Pass Filter "Scharr": to find edges
# scharx = cv2.Scharr(img, -1, dx=1, dy=0, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)
# schary = cv2.Scharr(img, -1, dx=0, dy=1, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)
# scharxy = sobelx + sobely
# cv2.imshow("scharx", scharx)
# cv2.imshow("schary", schary)
# cv2.imshow("scharxy", scharxy)

def nothing(x):
    pass


img = cv2.imread("UnoOnlyMountain.png")
cv2.imshow("Input", img)
Gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#median blur
median = cv2.medianBlur(img, ksize=11)
cv2.imshow("Median blur", median)

#High Pass Filter "Laplacian": to find edges
# Laplacian = cv2.Laplacian(median,-1, ksize=5, scale = 1, delta = 0, borderType=cv2.BORDER_DEFAULT)
# cv2.imshow("Laplacian", Laplacian)

#High Pass Filter "Sobel": to find edges
sobely = cv2.Sobel(median, -1, dx=0, dy=1, ksize=3, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)
cv2.imshow("sobely", sobely)

#Denoising Image
# fastNiLaplacian= cv2.fastNlMeansDenoising(Laplacian, 1,7,21)
# cv2.imshow("fastNiLaplacian", fastNiLaplacian)
fastNisobely= cv2.fastNlMeansDenoising(sobely, 1,7,21)
cv2.imshow("fastNisobely", fastNisobely)


#Erode
kernel = np.ones((3,3), np.uint8)
erode = cv2.erode(sobely,kernel, iterations = 1)
#erode = cv2.line(erode, (0,0),(5,5), (255,0,0),1)
cv2.imshow("Erode", erode)
#Blending images
imageblending = cv2.addWeighted(img, 0.15, sobely, 0.85, 0)
#cv2.imshow("Blending", imageblending)

px = erode[8,0,2]
#print("Red px: "+ str(px))
rows, cols, channels = erode.shape
print("rows: " + str(rows))
print("cols: " + str(cols))

blackpane = np.zeros((rows,cols), np.uint8)

#Iterate image
# for i in range(0, rows-1, 1):
#     for j in range (0, cols-1, 1):
#          if(erode[i,j,2]>15):
#              print(str(i)  +"x" +str(j) +": " + str(erode[i,j,2]))


blackpane = cv2.line(blackpane, (0, 0), (5, 5), (255, 0, 0), 1)
cv2.imshow("Blackpane", blackpane)

cv2.imwrite("erode.png", erode)


#cv2.imshow("Output", img)
cv2.waitKey()
cv2.destroyAllWindows()