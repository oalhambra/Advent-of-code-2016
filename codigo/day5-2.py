import hashlib

input="wtnhxymk"
# input+="1"
# input="abc3231929"
# input=bytes(input, "utf-8")
# print(input)

# m=hashlib.md5()
# m.update(input)
# print(m.hexdigest())

index=0
clave=["-1","-1","-1","-1","-1","-1","-1","-1"]

for i in range(0,8):
    encontrado=False
    while not encontrado:
        valor=input+str(index)
        valor=bytes(valor, "utf-8")
        m=hashlib.md5()
        m.update(valor)
        md5=m.hexdigest()
        # print(index)
        if md5.startswith("00000"):
            # print("posible")
            if md5[5]>="0"and md5[5]<="7":
                posicion=int(md5[5])
                if clave[posicion]== "-1":
                    clave[posicion]=md5[6]
                    encontrado=True
                    print(i+1)
        index+=1
print("It's got the code. It's about to launch!!")
print(clave)