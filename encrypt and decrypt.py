import random
def encrypter(massage):
    list = []
    for i in massage:
        x = ord(i)
        x = x + (13*4) + 13
        y = chr(x)
        list.append(y)
    re = "".join(map(str,list))
    return re
def decrypter(massage):
    list = []
    for i in massage:
        x = ord(i)
        x = x - int(13*4) - 13
        y = chr(x)
        list.append(y)
    re = "".join(map(str,list))
    return re

print('''
WELCOME TO ENCRYPTER AND DECRYPTER
      MAKE YOUR MASSAGE MORE SECRET ---->>>>💀💀
      WHAT WOULD YOU LIKE TO DO ....
        1 = ENCRYPT YOUR MASSAGE 
        2 = DECRYPT YOUR MASSAGE
        CHOOSE ONE : ''')
userinput = int(input())
match userinput:
    case 1 :
        print("ENTER THE MASSAGE YOU WANT TO ENCRYPT : ")
        massage = input()
        optupt = encrypter(massage)
        print(f"YOUR ENCRYPTED MASSAGE IS : {optupt}")
    case 2 : 
        print("ENTER THE MASSAGE YOU WANT TO DECRYPT : ")
        massage = input()
        optupt = decrypter(massage)
        print(f"YOUR DECRYPTED MASSAGE IS : {optupt}")
        