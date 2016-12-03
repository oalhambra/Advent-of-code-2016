



f = open('day1-1.txt', 'r')
data=f.read()
# print(data)

formatedData=data.split(', ')
# print(formatedData[2][0]=="R")


direccion=[0,0,0,0]
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

    direccion[direccionActual]+=valor
print(direccion)
ns=direccion[0]-direccion[2]
eo=direccion[1]-direccion[3]
print(ns,eo)
print(abs(ns)+abs(eo))









#
# simbolo=1
# derecha=giroDerecha[0]
# giroIzquierda.pop(0)
# for a in giroDerecha:
#     derecha=derecha+a*simbolo
#     simbolo=simbolo*-1
#
#
# simbolo=1
# izquierda=giroIzquierda[0]
# giroIzquierda.pop(0)
# for b in giroIzquierda:
#     izquierda=izquierda+b*simbolo
#     simbolo=simbolo*-1
#
# print(derecha)
# print(izquierda)
# print(derecha+izquierda)