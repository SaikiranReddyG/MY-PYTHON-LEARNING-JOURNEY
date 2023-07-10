#datatypes

#INT datatypes
a = 995566
print(a)
print(type(a))
print(id(a))
print(bin(a))
print(oct(a))
print(hex(a))

#FLOAT datatypes
f = 123.45
print(f)
f1 = 12e45
print(f1)

#complex datatype
a = 3+5j
b = 6+9j
c = a + b
print(a,b)
print(c)
print(type(c))
print(c.real)
print(c.imag)

#Boolean values datatype
a = 9
b = 55
c = a > b
d = a < b
print(c)
print(d)
print(type(c))
print(c + d)

#string datatype
a = 'sai'
b = "kiran"
c = 'reddy'
d = """saikiran
 reddy"""
print(a)
print(d)
print(a[1])
print(a[0],b[1],c[3])
print(a + d)
print(a*5)
print(len(d))
#In Python the ( int ,float,complex,bool,str) data types are considered as Fundamental Data types
         #'''All Fundamental Data types are immutable. i.e once we creates an object,we cannot
             #perform any changes in that object. If we are trying to change then with those changes
             # new object will be created. This non-chageable behaviour is called immutability'''



#bytes data type
x=[10,20,30,40]     #The only allowed values for byte data type are 0 to 256. By mistake if we are trying provide any other values then we will get value error.
                    #'bytes' object does not support item assignment
b = bytes(x)
print(type(b))
print(b[2])
for i in b :
    print(i)

#bytearray datatype       #bytearray is exactly same as byte datatype but its elements can be modified
x=[10,20,30,40]
b = bytearray(x)
print(type(b))

#list datatype             #list is flexible
v = [22,54,452,'fra',65,'adf','afd',432]
print(type(v))
print(v[3])
print(v[1:4])
v[4] = 'ssss'
print(v)
v.append('saikiran_reddy_G')
v.remove('adf')
print(v)
v2 = v*5
print(v2)

#tuple datatype     #same as list but its elements are immutable
                    #tuple is the read only version of list
x = (22,54,452,'fra',65,'adf','afd',432)
print(type(x))

#range datatype           #represent sequence of numbers in the given range
r = range(500,555)
for i in r:
    print(i)
r2 = range(22)
for i in r2:
    print(i)
r3 = list[r2]
print(r3)


#set datatype         #no duplicates and order is not importent
s={100,0,10,200,10,'durga'}
s.add(500)
s.remove(10)
print(s)

#frozenset          #immutable version of set
s1={100,0,10,200,10,'durga'}
s2 = frozenset(s1)
print(type(s2))


#dictionary          # represent a group of values as key-value pairs
g={101:'durga',102:'ravi',103:'shiva'}
