


f = open('day1-2.txt', 'r')
data=f.read()
# print(data)

formatedData=data.split(', ')
# print(formatedData[2][0]=="R")
mundo=[[0 for x in range(1000)] for y in range(1000)]
posX=500
posY=500

# print(mundo)

direccionActual=0
for i in formatedData:
    if i[0]=="R":
        direccionActual+=1
        direccionActual=direccionActual%4
        valor=int(i.replace("R",""))
    else:
        direccionActual-=1
        direccionActual=direccionActual%4
        valor=int(i.replace("L",""))

    if direccionActual==0:
        for i in range(0,valor):
            posX+=1
            mundo[posX][posY]+=1
            if mundo[posX][posY]==2:
                print("solucion!", posX,posY)
                print(abs(posX-500)+abs(posY-500))
                break

    elif direccionActual==1:
        for i in range(0,valor):
            posY+=1
            mundo[posX][posY]+=1
            if mundo[posX][posY]==2:
                print("solucion!", posX,posY)
                print(abs(posX-500)+abs(posY-500))
                break
    elif direccionActual==2:
        for i in range(0,valor):
            posX-=1
            mundo[posX][posY]+=1
            if mundo[posX][posY]==2:
                print("solucion!", posX,posY)
                print(abs(posX-500)+abs(posY-500))
                break
    else:
        for i in range(0,valor):
            posY-=1
            mundo[posX][posY]+=1
            if mundo[posX][posY]==2:
                print("solucion!", posX,posY)
                print(abs(posX-500)+abs(posY-500))
                break



print(posX,posY)
posX-=500
posY-=500
print(posX,posY)
print(abs(posX)+abs(posY))