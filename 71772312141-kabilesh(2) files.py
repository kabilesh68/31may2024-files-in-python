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
