#!C:/Python36/python.exe

import cgi
import ML

form = cgi.FieldStorage()

maths = int(form.getvalue('m_marks'))
read = int(form.getvalue('r_marks'))

pred = ML.predictMarks(maths,read)

print("Content-type:text/html\r\n\r\n")
print("""
<html>
<head>
<title>Machine Learning</title>
</head>
<body>
<h1>Your Predicted marks are : {}</h1>
</body>
</html>
""".format(int(pred)))
