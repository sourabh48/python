#!C:\Python34\pythonw.exe
import cgi
import mysql.connector
import connection

try:
    con=connection.connect()
    if con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM users")
        rows=cursor.fetchall()
        if not rows:
            print("No record found...")
        else:
            print("<table border=1 align=center width=500><tr><th>Ucode</th><th>Uname</th><th>EmailID</th><th>Mobile</th><th>User ID</th><th>Password</th></tr>")
            for i in rows:
                print("<tr><td>",i[0],"</td><td>",i[1],"</td><td>",i[2],"</td><td>",i[3],"</td><td>",i[4],"</td><td>",i[5],"</td></tr>")
            print("</table>")
    else:
        print("<h1>Connection not established...</h1>")
except:
    print("<h1>Failed to show data...</h1>")
finally:
    con.commit()
    con.close()
    



