

f = open('day8-1.txt', 'r')
data=f.read()

instrucciones=data.split("\n")

pantalla=[["." for x in range(6)] for y in range(50)]
print(pantalla)

def shiftRow(row):
    pantallaAux=[]
    for i in range(0, 50):
        pantallaAux.append(pantalla[i][row])
    for i in range(0, 50):
        pantalla[i][row]=pantallaAux[(i-1)%50]
    # pantalla[0][row]=pantallaAux[49]
# pantalla[49][0]=1
# pantalla[0][1]=1
# shiftRow(0)

def shiftColumn(column):
    pantallaAux=[]
    for i in range(0, 6):
        pantallaAux.append(pantalla[column][i])
    for i in range(0, 6):
        pantalla[column][i]=pantallaAux[(i-1)%6]
for i in pantalla:
    print(i)
for instruccion in instrucciones:
    if "rect" in instruccion: #instruccion rect
        dimensiones=instruccion.replace("rect ","")
        dimensiones=dimensiones.split("x")
        for i in range(0,int(dimensiones[0])):
            for j in range(0,int(dimensiones[1])):
                pantalla[i][j]="#"
    if "rotate row" in instruccion: #instruccion row
        filaValor=instruccion.replace("rotate row y=","")
        # print(filaValor, instruccion)
        filaValor=filaValor.split(" by ")
        # print(filaValor)
        for i in range(0,int(filaValor[1])):
            shiftRow(int(filaValor[0]))
    if "rotate column" in instruccion:
        # print(instruccion)
        columnaValor=instruccion.replace("rotate column x=","")
        columnaValor=columnaValor.split(" by ")
        for i in range(0,int(columnaValor[1])):
            shiftColumn(int(columnaValor[0]))
contador=0
print("\n\n\n")
for i in pantalla:
    print(i)
    for j in i:

        if j=="#":
            contador+=1
print(contador)
asdf=[list(i) for i in zip(*pantalla)]
for i in asdf:
    print(i)