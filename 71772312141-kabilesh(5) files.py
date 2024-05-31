f1 = open('sample.txt', 'r')
f2 = open('trial.txt', 'r')
f3 = open('combined.txt', 'w')
while True :
  data1 = f1.readline( )
  if data1 == '' :
   break
  f3.write(data1)
  data2 = f2.readline( )
  if data2 == '' :
   break
  f3.write(data2)
if data1 != '' :
  while True :
    data1 = f1.readline( )
    if data1 == '' :
     break
    f3.write(data1)
if data2 != '' :
  while True :
    data2 = f2.readline( )
    if data2 == '' :
      break
    f3.write(data2)
f1.close( )
f2.close( )
f3.close( )
output:
File 'sample.txt' contains following lines:
1. SANJAY 25
2. SAMEER 30
3. ANIL 23
4. SURESH 33
5. PRABHU 22
6. DINESH 40
7. Suresh 34
File 'trial.txt' contains following lines:
1. Sandhya 25
2. Seema 30
3. Swati 23
4. Supriya 33
5. Sunidhi 22
Resulting file 'comined.txt' contains following lines:
1. SANJAY 25
1. Sandhya 25
2. SAMEER 30
2. Seema 30
3. ANIL 23
3. Swati 23
4. SURESH 33
4. Supriya 33
5. PRABHU 22
5. Sunidhi 22
6. DINESH 40
7. Suresh 34
