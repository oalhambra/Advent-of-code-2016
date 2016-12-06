

f = open('day6-1.txt', 'r')
data=f.read()

mensaje=data.split("\n")
mensaje.pop(mensaje.__len__()-1)
print(mensaje)


for i in range(0, mensaje[0].__len__()):
    frecuencia=[0 for k in range(26)]
    for letra in range(0,mensaje.__len__()):
        # print(i)
        # print(letra)
        # print(letra[i])
        pos=ord(mensaje[letra][i])
        pos -=97
        frecuencia[pos]+=1
    # print(frecuencia)
    letraComun=-1
    countLetras=9999
    for j in range(0,26):
        if frecuencia[j]<countLetras:
            letraComun=j
            countLetras=frecuencia[j]
    print(chr(letraComun+97))

