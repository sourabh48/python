lst = [1,1,1,1,5,3,2,5,6,7,8,8]
lst2 = [2,"HI","YO", "YO"]
print ("before: ", lst)
lst = list(set(lst))
lst2 = list(set(lst2))
print ("after: ", lst)
lst2 = lst +lst2
print ("after append: ", lst2)