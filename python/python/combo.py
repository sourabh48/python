#!C:\Python34\pythonw.exe
import cgi
import mysql.connector
import connection


print('<html><form name=f1 method=post action=a.py>')
print('<select name=d1>')

try:
    con=connection.connect()
    if con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM course")
        rows=cursor.fetchall()
        if not rows:
            print("No record found...")
        else:
            for i in rows:
                cid=i[0]
                cname=i[1]
                print('<option value=',cid,'>',cname,'</option>')
            
    else:
        print("<h1>Connection not established...</h1>")
except:
    print("<h1>Failed to show data...</h1>")
finally:
    con.commit()
    con.close()
  
print('</select></form></html>')
  
    



