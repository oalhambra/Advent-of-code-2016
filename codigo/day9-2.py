import sys

f = open('day9-1.txt', 'r')
data=f.read()

print(data)


sublistas=[]
posicion=0
# print(data[:5])
while posicion<data.__len__():
    if data[posicion]=="(":
        posicion+=1

        longitud=''
        longParentesis=3
        while data[posicion]!='x':
            longitud=longitud+data[posicion]
            posicion+=1
            longParentesis+=1
        posicion+=1
        veces=''
        while data[posicion]!=')':
            veces=veces+data[posicion]
            posicion+=1
        posicion+=1

# while posicion<data.__len__():
#     if data[posicion]=="(":
#         posicion+=1
#         while data[posicion]!='x':
#             longitud=longitud+data[posicion]
#             posicion+=1
#         posicion+=1
#         veces=''
#         while data[posicion]!=')':
#             veces=veces+data[posicion]
#             posicion+=1
#         posicion+=1
#
#         mensaje=''
#         for i in range(posicion,posicion+int(longitud)):
#             mensaje=mensaje+data[posicion]
#         posicion+=int(longitud)
#         for i in range(0,int(veces)):
#             cadenaFinal=cadenaFinal+mensaje
#
#
#     else:
#         cadenaFinal=cadenaFinal+data[posicion]
#         posicion+=1



# sys.setrecursionlimit(6000)
#
# def analizarSegmento(segmento):
#
#     if '(' not in segmento:
#         return segmento.__len__()
#     else:
#         longitudRes=0
#         posicion=0
#         while posicion<data.__len__():
#             if data[posicion]=="(":
#                 posicion+=1
#                 longitud=''
#                 while data[posicion]!='x':
#                     longitud=longitud+data[posicion]
#                     posicion+=1
#                 posicion+=1
#                 veces=''
#                 while data[posicion]!=')':
#                     veces=veces+data[posicion]
#                     posicion+=1
#                 posicion+=1
#                 subsegmento=''
#                 for i in range(posicion,posicion+int(longitud)):
#                     subsegmento=subsegmento+data[i]
#                 longitudRes=longitudRes+analizarSegmento(subsegmento)*int(veces)
#                 posicion+=int(longitud)
#             else:
#                 longitudRes+=1
#                 posicion+=1
#         return longitudRes


# data.replace(" ","")

# cadenaFinal=""
posicion=0
# caracterActual=''
longitud=0

# print(int(data))

# while posicion<data.__len__():
#     caracterActual=data[posicion]
#     if data[posicion]=="(":
#         posicion+=1
#         while data[posicion]!='x':
#             longitud=longitud+data[posicion]
#             posicion+=1
#         posicion+=1
#         veces=''
#         while data[posicion]!=')':
#             veces=veces+data[posicion]
#             posicion+=1
#         posicion+=1
#
#         mensaje=''
#         for i in range(posicion,posicion+int(longitud)):
#             mensaje=mensaje+data[posicion]
#         posicion+=int(longitud)
#         for i in range(0,int(veces)):
#             cadenaFinal=cadenaFinal+mensaje
#
#
#     else:
#         cadenaFinal=cadenaFinal+data[posicion]
#         posicion+=1
# print(analizarSegmento(data))


