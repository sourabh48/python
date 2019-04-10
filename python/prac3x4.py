num = int(input("Enter a number: "))
tot = 0
while(num>0):
    dig = num%10
    tot = tot + dig
    num = num//10
print("The required value is: ", tot)
