str = 'Yo Im Sourabh'
str1 = ''
print ('Before removal: '+ str)
lst = list(str)
for i in range (0,len(str)):
    if(i%2==0):
        str1 = str1+lst[i]
print(str1)         