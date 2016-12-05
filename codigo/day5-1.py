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
clave=[]
for i in range(0,8):
    encontrado=False
    while not encontrado:
        valor=input+str(index)
        valor=bytes(valor, "utf-8")
        m=hashlib.md5()
        m.update(valor)
        md5=m.hexdigest()
        if md5.startswith("00000"):
            encontrado=True
            print(index)
            clave.append(md5[5])
        index+=1
print(clave)