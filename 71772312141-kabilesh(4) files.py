f1 = open('stud1.txt', 'r')
f2 = open('stud2.txt', 'w')
while True :
  data = f1.readline( )
  if data == '' :
   break
  data = data.upper( )
  f2.write(data)
f1.close( )
f2.close( )
output:
SANJAY 25
SAMEER 30
ANIL 23
SURESH 33
PRABHU 22
RAKESH 25
