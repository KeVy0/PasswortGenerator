#! /usr/bin/env python3
import sys
import string
from random import *

rsome = randint(1,100)
result = []


def usage():
    print ("PASSWORT GENERATOR : %s <wie viele Zeichen ( Muss eine Zahl sein)>"% sys.argv[0])



def random():
    userinput = int(sys.argv[1])
    # Noch schnell reingebaut, Idioten und so
    if userinput >= 1000000:
        checkif100 = input("Passwort uber 1000000 Zeichen , bist du dir sicher ? (Kann langer dauern) [j/n] ~> ")
        if checkif100 == "j":
            print("Gut, du wolltest es so....")
        elif checkif100 == "n":
            print("Abbruch...")
            exit()
        else:
            print("[j/n], sonst nichst")
            random()
     # Wenn Passwort über 1 Millionen wird nochmal nachgefragt       
    upperC = list(string.ascii_uppercase)
    lowerC = list(string.ascii_lowercase)
    digits = list(string.digits)
    hexdigits = list(string.hexdigits)
    punctation = list(string.punctuation)

    rpick = upperC + lowerC + digits + hexdigits + punctation

    while len(result) < userinput:
        result.append(choice(rpick))
    print("-----------Dein sicheres Passwort-------------")
    print (''.join(result))
        


def main():
    try:
        random()
    except Exception as e:
        usage()

main()        
