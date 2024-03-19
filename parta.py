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

def genprime(num1,num2):
    continue1 = True
    while continue1:
        tnum = random.randint(num1,num2)
        if prime(tnum):
            continue1 = False
    return tnum

def splitkey():
    print("Please input key:")
    key = input()

    keyarray = []
    random.seed(int(key, base=16))
    for i in range(256):
        keyarray.append(random.randint(0,99))
    
    return keyarray

def encrypt1(estring):
    keyarray = splitkey()
    estringarray = list(estring)

    count = 0
    for v in estringarray:
        if v == " ":
            estringarray[count] = 95
        else:
            estringarray[count] = ord(v)
        count += 1
    
    count = 0
    for v in estringarray:
        estringarray[count] += keyarray[count]
        estringarray[count] = hex(estringarray[count]).replace("0x","")
        count += 1

    printout = str(estringarray)
    printout = printout.replace("[","")
    printout = printout.replace("]","")
    printout = printout.replace(",","")
    printout = printout.replace("'","")
    printout = printout.replace(" ","")
    print()
    print("Your encrypted string is")
    print(printout)

def decrypt1(estring):
    keyarray = splitkey()
    estringarray = []
    for i in range(0,len(estring),2):
        estringarray.append(estring[i] + estring[i + 1])

    count = 0
    for v in estringarray:
        estringarray[count] = int(v, base=16)
        count += 1
    
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
    print()
    print("Your decrypted string is")
    print(printout)

ende = input("Encrypt or decrypt or share keys (E/D/S): ")
if ende.lower() == "e":
    encrypt1(input("Enter String:"))
elif ende.lower() == "d":
    decrypt1(input("Enter String:"))
elif ende.lower() == "s":
    publickey = genprime(1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    hexpublickey = hex(publickey).replace("0x","")
    print("The generated public key is\n" + hexpublickey + "\nIf you would like to change this, please input a different key below: ")
    keyquery = input()
    if keyquery:
        publickey = int(keyquery, base=16)
    smallerkey = genprime(10000000000000000000000000000000,99999999999999999999999999999999)
    hexsmallerkey = hex(smallerkey).replace("0x","")
    print()
    print("The generated smaller public key is\n" + hexsmallerkey + "\nIf you would like to change this, please input a different key below: ")
    keyquery = input()
    if keyquery:
        smallerkey = int(keyquery, base=16)
    
    privatekey = genprime(1,publickey)
    publicprivatekey = pow(smallerkey,privatekey,publickey)
    hexpublicprivatekey = hex(publicprivatekey).replace("0x","")
    print()
    print("Your mixed key is\n" + hexpublicprivatekey + "\nPlease enter your parties mixed key:")
    publicpartykey = int(input(), base=16)
    key = pow(publicpartykey,privatekey,publickey)
    print()
    print("Your key is\n" + hex(key).replace("0x",""))
    
input()
