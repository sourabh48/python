num = int(input("Enter a number: "))
factorial = 1
for x in range(1,num+1):
   factorial = x * factorial
print("The factorial of the given number is: ",factorial)