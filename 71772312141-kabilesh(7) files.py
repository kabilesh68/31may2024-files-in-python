donors = {
     'Sanjay' : ['Gokulpeth', 25, 1],
     'Sunil' : ['Shankarnagar', 26, 2],
     'Akash' : ['Sitaburdi', 27, 3],
     'Rahul' : ['Ramnagar', 23, 2],
     'Riddhi' : ['Dharampeth', 22, 2],
     'Mangal' : ['Ramdaspeth', 21, 2]
}
f = open('donors.txt', 'w+')
for k, v in donors.items( ) :
  s = '{0:20s}{1:40s}{2:2s}{3:1s}\n'.format(k, v[0], str(v[1]), str(v[2]))
  f.write(s)
f.seek(0,0)
while True :
   data = f.readline( )
   if data == '' :
     break
   nam = data[:20]
   address = data[20:59]
   age = int(data[60:62:])
   bloodtype = int(data[62:])
   if age < 25 and bloodtype == 2 :
    print(nam, address, age, bloodtype)
f.close() 
