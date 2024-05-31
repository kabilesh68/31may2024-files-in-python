f = open('a.txt', 'r')
data = f.read( )
f.close( )
data = data.replace(' a ', ' ')
data = data.replace(' an ', ' ')
data = data.replace(' the ', ' ')
f = open('b.txt', 'w')
f.write(data)
f.close( )
output:
The input file 'a.txt' contains following text:
The world is full of duplicates.
I want an apple a day.
I cannot do the stuff that you want me to do.
The output file 'b.txt' contains following text:
The world is full of duplicates.
I want apple day.
I cannot do stuff that you want me to do
