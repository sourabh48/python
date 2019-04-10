dict = {1:3,2:1,3:2,4:5}
x = int(input("Enter keys from 1 to 5: "))
value = dict.get(x,'NOT PRESENT')
if (value is not 'NOT PRESENT') :
    print('PRESENT')
else:
    print(value)    