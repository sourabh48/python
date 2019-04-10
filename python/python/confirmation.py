#!C:\Python34\pythonw.exe
import cgi
import mysql.connector
import connection

form = cgi.FieldStorage()

username = form.getvalue('username')
fathername = form.getvalue('fathername')
address = form.getvalue('address')
phoneno = form.getvalue('phoneno')
email = form.getvalue('email')
if form.getvalue('gender'):
   gender = form.getvalue('gender')
else:
   gender = "Not entered"
if form.getvalue('course'):
   course = form.getvalue('course')
else:
   course = "Not entered"
accounttype = "consumer"

try:
    con=connection.connect()
    if con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM course_details where courrse_id = '%s'" % (course,))
        rows=cursor.fetchall()
        if not rows:
            print("No record found...")
        else:
            print("<form name=f1 method=post action=payment.py>")
            print("<table>")
            for i in rows:
                print("<tr><td>Course ID:</td><td><input type=text name=t1 value=",i[0]," readonly></td></tr>")
                print("<tr><td>Course Name:</td><td><input type=text name=t2 value=",i[1]," readonly></td></tr>")
                print("<tr><td>Course Fees:</td><td><input type=text name=t3 value=",i[2]," readonly></td></tr>")
                print("<tr><td>Pay Now:</td><td><input type=text name=t4></td></tr>")
                
                print("<tr><td>&nbsp;</td><td><input type=submit name=b1 value=Pay></td></tr>")
                print('<input type=hidden name=p1 value=',username,'>')
                print('<input type=hidden name=p1 value=',fathername,'>')
                print('<input type=hidden name=p1 value=',gender,'>')
                print('<input type=hidden name=p1 value=',address,'>')
                print('<input type=hidden name=p1 value=',phoneno,'>')
                print('<input type=hidden name=p1 value=',email,'>')
                
            print("</table>")
    else:
        print("<h1>Connection not established...</h1>")
except:
    print("<h1>Failed to show data...</h1>")
finally:
    con.commit()
    con.close()
    



