#!C:\Python34\pythonw.exe
import cgi
import mysql.connector
import connection

#print ("Content-type:text/html\r\n\r\n")

form = cgi.FieldStorage()
ucode1 = form.getvalue('t1')
pwd  = form.getvalue('t2')
print(ucode1)

try:
    con=connection.connect()
    if con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM users where ucode = '%s'" % (ucode1))
        #cursor.execute("select * from users where ucode='U1003'")
        rows=cursor.fetchall()
        if not rows:
            print("No record found...")
        else:
            print("Login Successfull")
    else:
        print("<h1>Connection not established...</h1>")
except :
        #logger.error('Error: '+ str(e))
        print("<h1>Failed to show data...</h1>")
finally:
    con.commit()
    con.close()
    



