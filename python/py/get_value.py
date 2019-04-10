#!C:\Python34\pythonw.exe
import cgi
print ("Content-type:text/html\r\n\r\n")
form = cgi.FieldStorage()
name = form.getvalue('t1')
age  = form.getvalue('t2')

print ("<h1>Hello" ,name, "You are ",age," yrs. old</h1>") 


