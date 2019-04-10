lst = []
str = input("Enter numbers in coma separated way.")
lst1 = str.split(',')
for i in range (0,len(lst1)):
    lst.append(int(lst1[i])**2)
print (lst)
