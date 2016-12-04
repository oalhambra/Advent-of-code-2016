

f = open('day4-1.txt', 'r')
data=f.read()
# print(data)
rooms=data.split("\n")
roomList=[]
for room in rooms:
    roomList.append(room.split("-"))
    # print(room.split("-"))
roomList.pop(roomList.__len__()-1)
roomList.__len__()
for room in roomList:
    idCheck=room[room.__len__()-1]
    # print(idCheck)
    idCheck=idCheck.split("[")
    # print(idCheck)
    idCheck[1].replace("]","")
    room.pop(room.__len__()-1)
    room.append(int(idCheck[0]))
    room.append(idCheck[1])
print(roomList)

def charCount(room):
    letras=[0 for y in range(27)]
    check=room.pop(room.__len__()-1)
    id=room.pop(room.__len__()-1)
    for word in room:
        for char in word:
            letras[ord(char)-97]+=1
    room.append(id)
    room.append(check)
    return letras
print(charCount(roomList[0]))
print(roomList[0])

def maxValues(count,numValues):
    values=[-1 for y in range(numValues)]
    letters=[-1 for y in range(numValues)]
    for i in range(0,numValues):
        maxLetter=-1
        for j in range(0, count.__len__()):
            if values[i]<count[j] and j not in letters:
                maxLetter=j
                values[i]=count[j]
        letters[i]=maxLetter
    return letters
print(maxValues(charCount(roomList[0]),5))

def validateRoom(room):
    letras=charCount(room)
    checkSum=maxValues(letras,5)
    checkRoom=room[room.__len__()-1]
    resultado=True
    for i in range(0, checkSum.__len__()):
        if not (checkRoom[i]==chr(checkSum[i]+97)):
            resultado=False
            break
    return resultado

print(validateRoom(roomList[0]))
validRooms=[]
for room in roomList:
    if validateRoom(room):
        validRooms.append(room)
print(validRooms)
messages=[]
for room in validRooms:
    message=""
    check=room.pop(room.__len__()-1)
    id=room.pop(room.__len__()-1)
    for word in room:
        for char in word:
            # print(id)
            intChar=ord(char)
            intChar-=97
            intChar+=id
            intChar=intChar%26
            intChar+=97
            char=chr(intChar)
            message+=char
            # print(char)
        message+=" "
    room.append(id)
    room.append(check)
    messages.append([message,id])
    # print(message, id)
    for message in messages:
        if "north" in message[0]:
            print(message)