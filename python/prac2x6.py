a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Input option:   1 for addition   2 for substraction   3 for division   4 for multiplication "))

if c == 1 :
     d=a+b
     print("Required value is: ",d)

elif c == 2:
    if a<b :
        d = b-a
        print("Required value is: ",d)
    else :
        d = a-b
        print("Required value is: ",d)

elif c == 3 :
    if b==0 :
        print("The second number cannot be zero")
    else :
        d = a/b
        print("Required value is: ",d)

elif c == 4 :
    d = a*b
    print("Required value is: ",d)

