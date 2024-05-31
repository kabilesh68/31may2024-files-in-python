names = ['Sanjay', 'Sunil', 'Akash', 'Rahul', 'Riddhi', 'Mangal']
f = open('students.txt', 'w+')
for studname in names :
  f.write(studname + '\n')
num = int(input('Enter student number: '))
f.seek(0,0)
i = 1
while i < num :
  data = f.readline( )
  i += 1
data = f.readline( )
print('Num =', num, 'Name =', data)
f.close( )
