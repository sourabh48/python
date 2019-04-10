add = 0
mult = 1
lst = [2,3,5,6]
for i in range (0,len(lst)):
    add = add + lst[i]
print("Sum of elements:",add)    

for i in range (0,len(lst)):
    mult = mult * lst[i]
print("Product of elements:",mult)

print("Smallest element:", min(lst))    
print("Largest element:", max(lst))    


