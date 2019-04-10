#!C:\Python34\pythonw.exe
import cgi
import mysql.connector
import connection

form = cgi.FieldStorage()
unm  = form.getvalue('t1')
eml  = form.getvalue('t2')
mob  = form.getvalue('t3')
uid  = form.getvalue('t4')
pas  = form.getvalue('t5')


def redirect():
    print('<html>')
    print('  <head>')
    print('    <meta http-equiv="refresh" content="0;url='+str("http://localhost/python/login.html")+'" />') 
    print('  </head>')
    print('</html>')

def auto():
    con=connection.connect()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM users")
    rows=cursor.fetchall()
    if not rows:
        ucd="U1001"
    else:
        for i in rows:
            a=i[0]
            
        
        a=a[1:]
        x=int(a)+1
        return("U"+str(x))     
        

def insert():
    cursor = con.cursor()
    ucd=auto()
    sql = "insert into users(ucode,unm,eml,mob,uid,pas)VALUES (%s, %s, %s, %s, %s, %s)"        
    cursor.execute(sql,(ucd,unm,eml,mob,uid,pas))
    redirect()
try:
    con=connection.connect()
    if con:
        insert()
        redirect()
        #print ("<h2>User created Successfully...</h2>")
    else:
        print("<h1>Connection not established...</h1>")
except:
    print("<h1>User creation failed...</h1>")
finally:
    con.commit()
    con.close()
    



