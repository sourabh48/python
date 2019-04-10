#!C:\Python34\pythonw.exe
import cgi
import mysql.connector
import connection

form = cgi.FieldStorage()
c_id = form.getvalue('t1')
#print(c_id)

try:
    con=connection.connect()
    if con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM course where cid = '%s'" % (c_id))
        #cursor.execute("SELECT * FROM course where cid = 'C1001'")
        rows=cursor.fetchall()
        if not rows:
            print("No record found...")
        else:
            print("<form name=f1 method=post action=c_update.py>")
            #print("<table border=1 align=center width=500><caption>Course Details</caption><tr><th>Course ID</th><th>Course Name</th><th>Fees</th><th>Duration</th><th>Status</th></tr>")
            print("<table>")
            for i in rows:
                print("<tr><td>Course ID:</td><td><input type=text name=t1 value=",i[0]," readonly></td></tr>")
                print("<tr><td>Course Name:</td><td><input type=text name=t2 value=",i[1]," readonly></td></tr>")
                print("<tr><td>Course Fees:</td><td><input type=text name=t3 value=",i[2],"></td></tr>")
                print("<tr><td>Course Duration:</td><td><input type=text name=t4 value=",i[3],"></td></tr>")
                print("<tr><td>Course Status:</td><td><input type=text name=t5 value=",i[4],"></td></tr>")
                print("<tr><td>&nbsp;</td><td><input type=submit name=t1 value=Update></td></tr>")
            print("</table>")
    else:
        print("<h1>Connection not established...</h1>")
except:
    print("<h1>Failed to show data...</h1>")
finally:
    con.commit()
    con.close()
    



