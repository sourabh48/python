#!C:\Python34\pythonw.exe
import cgi
import smtplib
import passwd

form = cgi.FieldStorage()
#c_id = form.getvalue('t1')

print ("Content-type:text/html\r\n\r\n")
#print("<h2>Hello World</h2>")

sender,passw=passwd.get_sender_add()
receivers = ['sourabh.654321@outlook.com']
message = """From: Sourabh <ssunta.5884@gmail.com>
To: To Person <sourabh.654321@outlook.com>
Subject: Python SMTP e-mail test
We are testing sending email in Python-,c_id
"""
try:
    e = smtplib.SMTP('smtp.gmail.com', 587)
    e.ehlo()
    e.starttls()
    e.login(sender,passw)
    e.sendmail(sender, receivers, message)
    print ("Successfully sent email")
except SMTPException:
    print ("Error: unable to send email")
