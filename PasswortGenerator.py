import sys
import string
from random import *

rsome = randint(1,20)
result = []


def usage():
    print ("PASSWORT GENERATOR : %s <wie viele Zeichen ( Muss eine Zahl sein)>"% sys.argv[0])



def random():
    userinput = int(sys.argv[1])
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
