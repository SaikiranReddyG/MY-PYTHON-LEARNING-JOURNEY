#TUPLE
# 1) Tuple is exactly same as List except that it is immutable.
# 2) Hence Tuple is Read only version of List.
# 3) Parenthesis are optional but recommended to use.
t = 12,43,35,66,75,45
print(type(t))

tt = 13
print(type(tt))

tr = 13,
print(type(tr))

#converting list to tuple
lit = [23,53,7,6,12]
t = tuple(lit)
print(t)

#accessing elements of a tuple
   #by using index
u = 12,43,35,66,75,45
print(u[0])
print(u[3])
print(u[-2])

    #by using slice operator
#accessing elements of a tuple
   #by using index
uw = 12,43,35,66,75,45
print(uw[1:3:2])
print(uw[1:-1:2])
print(uw[1:3:-2])

#immutability >>> tuple objects are immutable.


#mathametical opreations

       #concacination(+)
t1 = (12,43,35,66,75,45)
t2 = (23,53,7,6,12)
t3 = t1 + t2
print(t3)
        #repitation(*)
ty = (23,53,7,6,12)
tty = ty*3
print(tty)

#functions of tuple

#len
to = (12,43,35,66,75,45)
print(len(to))
#count
to = (12,43,35,12,66,75,45)
print(to.count(12))

#sorting
t = (12,43,35,12,66,75,45)
ty = sorted(t)
print(t)

#min() and max()
t = (12,43,35,12,66,75,45)
print(min(t))
print(max(t))

#tuple packing and unpacking
a = 33
b = 54
c = 76
t = a,b,c
print(t)

a,b,c = t
print('a=',a,'b=',b,'c=',c)

#print entered tuple sum and average
t = eval(input('enter a tuple:'))
k = len(t)
sum = 0
for x in t:
    sum =sum + x
print('sum = ',sum)
print('average = ',sum/k)