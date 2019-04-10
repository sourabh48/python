#guessing game

import random

rndomvalue = random.randint(1,10)
userinput = 0

while (userinput!=rndomvalue):
    userinput = int(input("Enter an integer: "))

    if(userinput==rndomvalue):
        print("well done")
        break
    else:
        if(userinput>rndomvalue):
            print("Alas! U guessed it wrong! value I thought is less than u entered!")
        elif(userinput<rndomvalue):
            print("Alas! U guessed it wrong! value I thought is more than u entered!")
        print("Try again.")
    

