#!C:\Python34\pythonw.exe
import cgi
import mysql.connector
import connection

form = cgi.FieldStorage()
dno = form.getvalue('t1')
dnm = form.getvalue('t2')
loc = form.getvalue('t3')
print(dno," ",dnm," ",loc)
try:
    con=connection.connect()
    if con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM dept WHERE deptno=%s" % (dno))
        rows=cursor.fetchall()
        if not rows:
            print("Record not found...")
        else:        
            cursor.execute("UPDATE dept SET dname=%s, loc=%s WHERE deptno=%s" , (dnm,loc,dno))            
            con.commit()
            print("Record Updated...")        
    else:
        print("<h1>Connection not established...</h1>")
except:
    print("<h1>Failed to Update...</h1>")
finally:    
    con.close()
    



