


f = open('day3-1.txt', 'r')
data=f.read()
# print(data)

triangleSet=data.split("\n")
triangles=[]

for triangle in triangleSet:
    sides=triangle.split(" ")
    final=[]
    for side in sides:
        if side != "":
            final.append(int(side))
    triangles.append(final)
    # print(final)

triangulosFinal=[]
triangles.pop(triangles.__len__()-1)

for i in range(0,int(triangles.__len__()/3)):

    for j in range(0,3):
        triangulo=[]
        triangulo.append(triangles[i*3][j])
        triangulo.append(triangles[i*3+1][j])
        triangulo.append(triangles[i*3+2][j])
        triangulosFinal.append(triangulo)
        print(triangulo)

# print(triangulosFinal)

def isTrianglable(triangle):
    if (triangle[0]+triangle[1])<=triangle[2]:
        return False
    elif (triangle[1]+triangle[2])<=triangle[0]:
        return False
    elif (triangle[2]+triangle[0])<=triangle[1]:
        return False
    else:
        return True

contador=0
for triangle in triangulosFinal:
    if isTrianglable(triangle):
        contador+=1
print(contador)
