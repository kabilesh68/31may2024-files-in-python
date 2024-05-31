import json
def encode_employee(x):
  if isinstance(x, Employee) :
    return(x.ecode, x.ename, x.doj, x.sal)
  else :
    raise TypeError('Complex object is not JSON serializable')
def decode_employee(dct):
  if ' Employee ' in dct :
    return Employee(dct['ecode'], dct['ename'], dct['doj'], dct['sal'])
  return dct
class Employee :
  def init (self, ecode, ename, doj, sal) :
   self.ecode = ecode
   self.ename = ename
   self.doj = doj
   self.sal = sal
  def print_data(self) :
   print(self.ecode, self.ename, self.doj, self.sal)
e = Employee('A101', 'Sameer', '17/11/2017', 25000)
f = open('data', 'w+')
json.dump(e, f, default = encode_employee)
f.seek(0)
ine = json.load(f, object_hook = decode_employee)
print(ine)
output:
['A101', 'Sameer', '17/11/2017', 25000]
