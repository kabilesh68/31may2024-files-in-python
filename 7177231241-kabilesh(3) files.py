import operator
f = open('students.txt', 'r')
dct = { }
while True :
  data = f.readline( )
  if data == '' :
    break
  stud = data.split( )
  dct[stud[0]] = stud[1]
f.close( )
lst = sorted(dct.items( ), key = operator.itemgetter(0))
for item in lst :
    print(item[0], item[1])
output:
Anil 23
Prabhu 22
Rakesh 25
Sameer 30
Sanjay 25
Suresh 33
