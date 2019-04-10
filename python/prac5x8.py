lst = []
for x in range(1,4):
    str = input("Enter a line : ")
    str2 = str[0].upper() + str[1:len(str)]
    lst.append(str2)
print(lst)     