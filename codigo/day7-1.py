import re

f = open('day7-1.txt', 'r')
data=f.read()

ips=data.split('\n')

listaProcesada=[]

for ip in ips:
    listaProcesada.append(re.split('[\[\]]',ip))

print(listaProcesada)
listaProcesada.pop(listaProcesada.__len__()-1)

def hasPalindrome(seccion):
    has=False
    if seccion.__len__()<4:
        return False
    for i in range(0,seccion.__len__()-4):
        if(seccion[i]==seccion[i+3])and(seccion[i+1]==seccion[i+2]):
            has=True
    return has

print(hasPalindrome(listaProcesada[0][0]))

contador=0
for i in listaProcesada:
    tiene=None
    for j in range(i.__len__()):
        if hasPalindrome(i[j]):
            if(j%2==0):
                if tiene!=False:
                    tiene=True
            else:
                tiene=False
    if tiene==True:
        contador+=1
print(contador)
print(listaProcesada.__len__())
lista=[]
print(lista.append([]))

