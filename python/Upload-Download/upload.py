#!C:\Python34\pythonw.exe
import cgi, os
form = cgi.FieldStorage()
f1 = form['file']
if f1.filename:
    print("Content-type:text/html\r\n\r\n")
    fn = os.path.basename(f1.filename)
    open('upload/' + fn, 'wb').write(f1.file.read())
    print('The file "' + fn + '" was uploaded successfully')
else:
    print('No file was uploaded')

