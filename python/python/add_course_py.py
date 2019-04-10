#!C:\Python34\pythonw.exe
import cgi
import mysql.connector
import connection

form = cgi.FieldStorage()
cname  = form.getvalue('t1')
fees  = form.getvalue('t2')
duration = form.getvalue('t3')
sts = 'Active'
print(cname,fees,duration,sts)


'''

def redirect():
    print('<html>')
    print('  <head>')
    print('    <meta http-equiv="refresh" content="0;url='+str("http://localhost/python/login.html")+'" />') 
    print('  </head>')
    print('</html>')
'''

def insert():
    cursor = con.cursor()
    c_id=auto()
    sql = "insert into course(cid,cname,fees,duration_month,status)VALUES (%s, %s, %s, %s, %s)"        
    cursor.execute(sql,(c_id,cname,fees,duration,sts))
    #redirect()
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
    



