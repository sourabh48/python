import re

regex = r'\b[\w.-]+?@\w+?\.\w+?\b'
str = "my email is sourabh91@kiit.ac.in"
match=re.findall(regex,str)
print ("Email: ", match)
lst = str.split("@")
print("Username: ", lst[0])
str1 = lst[1]
lst1 = str1.split(".")
print("Company: ", lst1[0])