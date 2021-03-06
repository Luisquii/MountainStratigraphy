import cv2

img = cv2.imread("imgs/UnoOnlyMountain.png")
erode = cv2.imread("erode.png")
rows, cols, channels = erode.shape
Matrix = [[0 for x in range(cols)] for y in range(rows)]
print(cols)
print(rows)
for i in range(0, rows-1,1):
    for j in range(0, cols-1,1):
        Matrix[i][j] = erode[i,j,2]

sixpos = 21
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