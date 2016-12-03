

f = open('day2-1.txt', 'r')
data=f.read()
print(data)
keyInstruction=data.split("\n")
# print(keyInstruction)
# teclado=[[0 for x in range(3)] for y in range(3)]



def mover (tecla, posActual):
    if tecla=='L':
        if not (posActual==1 or posActual==2 or posActual==5 or posActual==10 or posActual==13):
            posActual-=1
    elif tecla=='R':
        if not (posActual==1 or posActual==4 or posActual==9 or posActual==12 or posActual==13):
            posActual+=1
    elif tecla=='U':
        if not (posActual==1 or posActual==2 or posActual==4 or posActual==5 or posActual==9):
            # posActual-=3
            if posActual==3 or posActual==13:
                posActual-=2
            else:
                posActual-=4
    else:
        if not (posActual==5 or posActual==10 or posActual==13 or posActual==12 or posActual==9):
            # posActual+=3
            if posActual==1 or posActual==11:
                posActual+=2
            else:
                posActual+=4
    return posActual

posActual=5

for i in keyInstruction:
    for tecla in i:
        posActual=mover(tecla,posActual)
    print(posActual)
