times = int(input("Enter the value: "))
dict = {}
for i in range (1,times+1):
    dict1 = {i:i*i}
    dict.update(dict1)
print(dict)    