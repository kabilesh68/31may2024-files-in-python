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
