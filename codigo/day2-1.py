

f = open('day2-1.txt', 'r')
data=f.read()
print(data)
keyInstruction=data.split("\n")
# print(keyInstruction)
# teclado=[[0 for x in range(3)] for y in range(3)]



def mover (tecla, posActual):
    if tecla=='L':
        if not (posActual==1 or posActual==4 or posActual==7):
            posActual-=1
    elif tecla=='R':
        if not (posActual==3 or posActual==6 or posActual==9):
            posActual+=1
    elif tecla=='U':
        if not (posActual==1 or posActual==2 or posActual==3):
            posActual-=3
    else:
        if not (posActual==7 or posActual==8 or posActual==9):
            posActual+=3
    return posActual

posActual=5

for i in keyInstruction:
    for tecla in i:
        posActual=mover(tecla,posActual)
    print(posActual)
