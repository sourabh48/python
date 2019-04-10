import re

str = "our roll no is 1515048 and 1515049."

regex = r'\d+'
match=re.findall(regex,str)
print ("numbers: ", match)
