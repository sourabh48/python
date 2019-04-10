lst = []
for i in range(2000,3001):
    x=i
    value1 = x%10
    x= (x-value1)//10
    value2 = x%10
    x= (x-value2)//10
    value3 = x%10
    x= (x-value3)//10

    if(value1%2==0 and value2%2==0 and value3%2==0 and x%2==0):
        lst.append(i)
print(lst)        