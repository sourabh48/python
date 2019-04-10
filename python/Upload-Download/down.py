#!C:\Python34\pythonw.exe
import os
print('Content-type:text/html\r\n\r\n')
print('<h2>Select the file to be downloaded</h2>')

print("\
<body>\
<form id='form1' name='form1' method='post' action='download.py'>\
  <p>")
for root, directories, filenames in os.walk('upload'):   
    for file in filenames:
        print("<input type='radio' name='r1'  value='",file,"' />")
        print("<label for='r1'>",file,"</label>")

    
print("\
  </p>\
  <p>\
    <input type='submit' name='b1' id='b1' value='Download' />\
  </p>\
</form>\
</body>\
")



'''  
print('Content-Disposition: attachment; filename=upload\'Login.txt\'')



Select_file.php
<?php
$files = scandir('up'); 
echo '<h1>Click to Download</h1>';
foreach($files as $file)
{		
	 echo '<a href=download.php?var='.$file.'>'.$file.'</a><br>';
}
?>

download.php
<?php
$n=$_GET['var'];
if(isset($n))
{
header('Content-length: '.filesize('upload/'.$n)); 
header('Content-disposition: attachment; filename='.basename('upload/'.$n)); 	
readfile('upload/'.$n); 
exit;
}
?>


'''
