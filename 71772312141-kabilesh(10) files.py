f = open('a.txt', 'r')
data = f.read( )
f.close( )
data = data.replace(' a ', ' ')
data = data.replace(' an ', ' ')
data = data.replace(' the ', ' ')
f = open('b.txt', 'w')
f.write(data)
f.close( )
