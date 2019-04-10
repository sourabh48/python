#!C:\Python34\pythonw.exe
import cgi
import mysql.connector
import connection

form = cgi.FieldStorage()

courseid = form.getvalue('courseid')
coursename = form.getvalue('coursename')
coursefees = form.getvalue('coursefees')
courseduration = form.getvalue('courseduration')
status = "active"

print(courseid,coursename,coursefees,courseduration,status)

def insert():
    cursor = con.cursor()
    sql = "insert into course_details(courrse_id,course_name,fees,duration,status)VALUES (%s, %s, %s, %s, %s)"        
    cursor.execute(sql,(courseid,coursename,coursefees,courseduration,status))

try:
    con=connection.connect()
    if con:
        insert()
        #redirect()
        print ("<h2>Course hasbeen successfully added</h2>")
    else:
        print("<h1>Connection not established...</h1>")
except:
    print("<h1>Internal Error</h1>")
finally:
    con.commit()
    con.close()
