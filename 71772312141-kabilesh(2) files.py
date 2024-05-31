f1 = open('sample.txt', 'r')
para1 = ''
while True :
   data = f1.readline( )
   if data == '' :
    break
   para1 += data
f2 = open('trial.txt', 'r+')
para2 = ''
while True :
   data = f2.readline( )
   if data == '' :
     break
   para2 += data
   para2 += para1
print(para2)
f2.seek(0, 0)
f2.write(para2)
f1.close( )
f2.close( )
output:
'sample.txt' contains a few lines in lower case. 'trial.txt. contains the
same lines in uppercase. After concatenation the contents of 'tiral.txt' is
as shown below:
CPYTHON - IS THE REFERENCE IMPLEMENTATION, WRITTEN
IN C. PYPY - WRITTEN IN A SUBSET OF PYTHON LANGUAGE
CALLED RPYTHON.
JYTHON - WRITTEN IN JAVA.
IRONPYTHON - WRITTEN IN C#.
CPython - is the reference implementation, written in C.
PyPy - Written in a subset of Python language called RPython.
Jython - Written in Java.
IronPython - Written in C#
