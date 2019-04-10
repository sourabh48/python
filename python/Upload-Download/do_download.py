#!C:\Python34\pythonw.exe
import cgi, os
form = cgi.FieldStorage()
f=form.getvalue('r1')
print("Content-Disposition: attachment; filename=",f)
print("Content-type:text/html\r\n\r\n")

