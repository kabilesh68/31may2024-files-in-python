f = open('sample.txt', 'r')
while True :
  data = f.readline( )
  if data == '' :
    break
  print(data)
f.close( )
output:
CPython - is the reference implementation, written in C.
PyPy - Written in a subset of Python language called RPython.
Jython - Written in Java.
IronPython - Written in C#.
