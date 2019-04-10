dict = {1:3,2:1,3:2,4:5}
print("Original: ",dict)
add = 0
mult = 1
dict.setdefault(5,7)
print("After addition: ",dict)
keys = sorted(dict.keys())
print("List of keys: ", keys)
for x in range (0,len(keys)):
    add = add + keys[x]
values = sorted(dict.values())
print("List of values: ", values)
for x in range (0,len(keys)):
    mult = mult * values[x]
print("Addition: ",add)
print("Product: ",mult)    