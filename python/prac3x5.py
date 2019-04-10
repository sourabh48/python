#prime or composite

num = int(input("Enter a number: "))

for x in range(2,num): 
  if(num%x == 0):
      print ("The number is not prime")
      break;
else:
  print("The number is prime")   
