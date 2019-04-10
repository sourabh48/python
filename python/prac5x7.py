lst = [1,2,3,4,5,6,7,8,9,0]
i = int(input("Enter a digit: "))
print("Index no of given element: " ,lst.index(i))
lst.remove(lst[0])
lst.remove(lst[4])
lst.remove(lst[5])
print("After removal of elements: ",lst)

