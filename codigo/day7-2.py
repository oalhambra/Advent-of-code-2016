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
    tiene=[]
    if seccion.__len__()<3:
        return [""]
    for i in range(0,seccion.__len__()-2):
        if(seccion[i]==seccion[i+2]):
            tiene.append(seccion[i]+seccion[i+1]+seccion[i+2])
    if tiene==[]:
        return [""]
    else:
        return tiene

def reversePalindrome(palindrome):
    return palindrome[1]+palindrome[0]+palindrome[1]

contador=0
for i in listaProcesada:
    tiene=None
    palindromos=[]
    for j in range(i.__len__()):
        palindromos.append(hasPalindrome(i[j]))
    # print(palindromos)
    palindromosFuera=palindromos[0:][::2]
    palindromosDentro=palindromos[1:][::2]
    # print(palindromosDentro)
    # print(palindromosFuera)
    for i in palindromosFuera:
        for j in i:
            if j!="":
                inverso=reversePalindrome(j)
                for k in palindromosDentro:
                    for l in k:
                        if inverso==l:
                            tiene=True
                            print(l, inverso)
                            # contador+=1

        # if hasPalindrome(i[j]):
        #     if(j%2==0):
        #         if tiene!=False:
        #             tiene=True
        #     else:
        #         tiene=False
    if tiene==True:
        contador+=1
print(contador)
print(listaProcesada.__len__())

