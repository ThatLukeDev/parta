import random
import math

def prime(x):
    count = 0
    retvar = True
    for i in range(math.floor(x / 2)):
        if x % (i + 2) == 0:
            retvar = False
            continue
        return retvar

def genprime():
    continue1 = True
    while continue1:
        tnum = random.randint(10000000000000000000000000000000,99999999999999999999999999999999)
        if prime(tnum):
            continue1 = False
    return tnum

def splitkey():
    print("Please input key:")
    key = input()

    keyarray = []
    random.seed(int(key))
    for i in range(256):
        keyarray.append(random.randint(0,99))
    
    return keyarray

def encrypt1(estring):
    keyarray = splitkey()
    estringarray = list(estring)

    count = 0
    for v in estringarray:
        estringarray[count] = ord(v)
        count += 1
    
    count = 0
    for v in estringarray:
        estringarray[count] += keyarray[count]
        count += 1

    printout = str(estringarray)
    printout = printout.replace("[","")
    printout = printout.replace("]","")
    printout = printout.replace(",","")
    print(printout)

def decrypt1(estring):
    keyarray = splitkey()
    estringarray = estring.split(" ")

    count = 0
    for v in estringarray:
        estringarray[count] = int(estringarray[count]) - keyarray[count]
        estringarray[count] = chr(int(estringarray[count]))
        count += 1
    
    printout = str(estringarray)
    printout = printout.replace("[","")
    printout = printout.replace("]","")
    printout = printout.replace(",","")
    printout = printout.replace("'","")
    printout = printout.replace(" ","")
    print(printout)

ende = input("Encrypt or decrypt or share keys (E/D/S): ")
if ende.lower() == "e":
    encrypt1(input("Enter String:"))
elif ende.lower() == "d":
    decrypt1(input("Enter String:"))
elif ende.lower() == "s":
    publickey = genprime()
    privatekey = genprime()
    print("The generated public key is", publickey, "if you would like to change this, please input a different key below: ")
    keyquery = input()
    if keyquery:
        publickey = int(keyquery)
    publicprivatekey = publickey * privatekey
    print("Your mixed key is", publicprivatekey, "Please enter your parties mixed key:")
    publicpartykey = int(input())
    key = publicpartykey * privatekey
    print("Your key is", key)
    
input()
