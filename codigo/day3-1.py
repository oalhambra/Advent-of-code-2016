


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
    # sides.pop(5)
    # sides.pop(3)
    # sides.pop(1)
    # sides.pop(0)
    triangles.append(final)
    print(final)

def isTrianglable(triangle):
    if (triangle[0]+triangle[1])<=triangle[2]:
        return False
    elif (triangle[1]+triangle[2])<=triangle[0]:
        return False
    elif (triangle[2]+triangle[0])<=triangle[1]:
        return False
    else:
        return True

triangles.pop(triangles.__len__()-1)
print(triangles.__len__())
contador=0
for triangle in triangles:
    if isTrianglable(triangle):
        contador+=1
print(contador)