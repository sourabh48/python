#!C:\Python34\pythonw.exe
import cgi
import mysql.connector
import connection


print('<html><form name=f1 method=post action=confirmation.py>')
print('<table align=center><caption>Student Details</caption>')
print('<tr><td>Student Name:</td><td><input type=text name=t1 ></td></tr>')
print('<tr><td>Fathers Name:</td><td><input type=text name=t2 ></td></tr>')
print('<tr><td>Gender:</td><td><input type=radio name=t3 value=Male>Male&nbsp&nbsp<input type=radio name=t3 value=Female>Female</td></tr>')
print('<tr><td>Address:</td><td><input type=text name=t4 ></td></tr>')
print('<tr><td>Contact No:</td><td><input type=text name=t5 ></td></tr>')
print('<tr><td>Email ID:</td><td><input type=text name=t6 ></td></tr>')
print('<tr><td>Course Name:</td><td><select name=d1>')

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
  
print('</select></td></tr>')
print('<tr><td>&nbsp;</td><td><input type=submit value=Go></td></tr>')
print('</table></form></html>')
  
    



