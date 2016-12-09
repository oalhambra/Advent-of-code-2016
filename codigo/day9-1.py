

f = open('day9-1.txt', 'r')
data=f.read()

print(data)

data.replace(" ","")

cadenaFinal=""
posicion=0
# caracterActual=''

# print(int(data))

while posicion<data.__len__():
    caracterActual=data[posicion]
    if data[posicion]=="(":
        posicion+=1
        longitud=''
        while data[posicion]!='x':
            longitud=longitud+data[posicion]
            posicion+=1
        posicion+=1
        veces=''
        while data[posicion]!=')':
            veces=veces+data[posicion]
            posicion+=1
        posicion+=1
        mensaje=''
        for i in range(posicion,posicion+int(longitud)):
            mensaje=mensaje+data[posicion]
        posicion+=int(longitud)
        for i in range(0,int(veces)):
            cadenaFinal=cadenaFinal+mensaje


    else:
        cadenaFinal=cadenaFinal+data[posicion]
        posicion+=1
print(cadenaFinal.__len__())


