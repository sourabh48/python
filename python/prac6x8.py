keys = [1,2,3,4,5,6]
values = ['hi','hello','hola','hellow','bye','goodnight']
dict = dict(zip(keys,values))
print("before delete: ",dict)
del dict[3]
print("After delete: ",dict)
newval = {7:'help'}
dict.update(newval)
print("After addition: ",dict)
