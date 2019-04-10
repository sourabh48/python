unit = float(input("Enter units consumed: "))
if unit >= 0 and unit <= 100:
    amount = (100 + (unit * .80)) 
    print("Bill: ", amount)
elif unit >= 101 and unit <= 200:
    amount = (100 + (unit * .1))
    print("Bill: ", amount)
elif unit >= 201 and unit <= 300 :
    amount = (100 + (unit * 1.5))
    print("Bill: ", amount) 
elif unit >= 301 :
    amount = (100 + (unit * 2))
    print("Bill: ", amount)  
else :
    print("Unit cannot be negetive!")