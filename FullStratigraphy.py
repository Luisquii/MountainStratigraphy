import cv2
import numpy as np


def nothing(x):
    pass


imgName = "imgs/UnoOnlyMountain.png"
img = cv2.imread(imgName)
cv2.imshow("Input", img)


#median blur
median = cv2.medianBlur(img, ksize=11)


#High Pass Filter "Sobel": to find edges
sobely = cv2.Sobel(median, -1, dx=0, dy=1, ksize=3, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)


#Erode
kernel = np.ones((3,3), np.uint8)
erode = cv2.erode(sobely,kernel, iterations = 1)
GrayErode = cv2.cvtColor(erode, cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayErode", GrayErode)


#Blending images
imageblending = cv2.addWeighted(img, 0.30, erode, 0.70, 0)
cv2.imshow("Blending", imageblending)

rows, cols = GrayErode.shape
Matrix = [[0 for x in range(cols)] for y in range(rows)]
print(cols)
print(rows)
for i in range(0, rows-1,1):
    for j in range(0, cols-1,1):
        Matrix[i][j] = GrayErode[i,j]

sixpos = 8      #Play with this value [5,25]
threepos = sixpos -1

#Lista para anadir los puntos deseados
mapaDePuntos = []
for i in range(1, rows-1, 1):
    for j in range (1, cols-1, 1):
        # print("   i   " +str(j*i))
        #Checar primeras 6 posiciones de la matriz
        if(Matrix[i-1][j - 1] < sixpos) and (Matrix[i-1][j] < sixpos) and (Matrix[i-1][j + 1]< 21) and (Matrix[i][j - 1]< sixpos) and (Matrix[i][j] < sixpos) and (Matrix[i][j + 1] <sixpos):
            #Checal ultimas 3 posiciones de la matriz
            if Matrix[i + 1][j - 1] > threepos or Matrix[i + 1][j] > threepos or Matrix[i + 1][j + 1] > threepos:
                maxpx = 0
                if Matrix[i + 1][j - 1] > maxpx:
                    maxpx= Matrix[i + 1][j - 1]
                    pos= (j-1, i+1)
                if Matrix[i + 1][j] > maxpx:
                    maxpx = Matrix[i + 1][j]
                    pos = (j, i+1)
                if Matrix[i + 1][j + 1] > maxpx:
                    maxpx = Matrix[i + 1][j + 1]
                    pos = (j+1, i+1)

                # try:
                #     print(str(Matrix[i - 1][j - 1]) + "  " + str(Matrix[i - 1][j]) + "  " + str(Matrix[i - 1][j + 1]))
                # except:
                #     print("Not found")
                # try:
                #     print(str(Matrix[i][j - 1]) + "  " + str(Matrix[i][j]) + "  " + str(Matrix[i][j + 1]))
                # except:
                #     print("Not found")
                # try:
                #     print(str(Matrix[i + 1][j - 1]) + "  " + str(Matrix[i + 1][j]) + "  " + str(Matrix[i + 1][j + 1]))
                # except:
                #     print("Not found")

                if pos not in mapaDePuntos:
                    mapaDePuntos.append(pos)
                else:
                    pass
                # print("Pos in Matrix:  Column->" +str(pos[0]) +"   Renglon ->"  +str(pos[1]) )
                # print("Pos in ImLAb: column->" +str(pos[0]) +"  Renglon ->" +str((165-pos[1])-1))
                # print("Max Num: " + str(maxpx))
                # print("---------------------------")


print(mapaDePuntos)
print(len(mapaDePuntos))

iterarPunots = len(mapaDePuntos) -1
for i in range(0, iterarPunots ,1):
    img = cv2.line(img, mapaDePuntos[i], mapaDePuntos[i], (0,255,0), 1 )

    #print(str(mapaDePuntos[i]) + " " + str(mapaDePuntos[i+1]))


cv2.imshow("Erode", erode)
cv2.imshow("Union", img)
cv2.waitKey()
cv2.destroyAllWindows()