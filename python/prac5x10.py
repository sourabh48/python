lst = []
x=1
amount = 0
while(x>0):
    str = input("Enter a log (type 'e' to end): ")
    if(str is 'e'):
        x=x-1
    elif(str is not 'e'):
        lst.append(str)
print("log: " , lst)
for i in range (0,len(lst)):
    str = lst[i]
    if(str[0] is 'W'):
        temp = int(str[2:])
        amount = amount - temp
    elif(str[0] is 'D'):
        temp = int(str[2:])
        amount = amount + temp
print("Your account balance: ", amount)         
        