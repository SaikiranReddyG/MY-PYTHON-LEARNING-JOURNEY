#polymorphism    (poly means many. Morphs means forms.   Polymorphism means 'Many Forms'.)
class duck:
    def talk(self):
        print('quack...quack')

class human:
    def talk(self):
        print('hi....hello!!!!')


class dog:
    def bark(self):
        print('woof woof')

def f1(obj):
    if hasattr(obj,'talk'):       #hasattr
        obj.talk()
    elif hasattr(obj,'bark'):
        obj.bark()

d = duck()
f1(d)

h = human()
f1(h)

g = dog()
f1(g)

#overloaading  (We can use same operator or methods for different purposes.)
            #operator overloading
class books:
     def __init__(self,pages):
         self.pages = pages


     def  __add__(self, other):
         return self.pages + other.pages


b1 = books(90909)
b2 = books(989898)
print('the total no of pages',b1+b2)

#list of operators and coresspoding magic operators
#(+)    object.__add__(self,other)
#(-)    object.__sub__(self,other)
#(*)    object.__mul__(self,other)
#(/)    object.__div__(self,other)
#(//)   object.__floordiv__(self,other)
#(%)    object.__mod__(self,other)
#(**)   object.__pow__(self,other)
#(+=)   object.__iadd__(self,other)
#(-=)   object.__isub__(self,other)
#(*=)   object.__imul__(self,other)
#(/=)   object.__idiv__(self,other)
#(//=)  object.__ifloordiv__(self,other)
#(%=)   bject.__imod__(self,other)
#(**=)  object.__ipow__(self,other)
#(<)    object.__lt__(self,other)
#(<=)   object.__le__(self,other)
#(>)    object.__gt__(self,other)
#(>=)   object.__ge__(self,other)
#(==)   object.__eq__(self,other)
#(!=)   object.__ne__(self,other)


#Overloading > and <= Operators
class students:
    def __init__(self,name,marks):
        self.name = name
        self.marks = int(marks)

    def __gt__(self, other):
        return self.marks > other.marks

    def __le__(self, other):
        return self.marks <= other.marks


s1 = students('saikiran', 99)
s2 = students('reddy', 77)
print('s1>s2=', s1 > s2)
print('s1<s2=', s1 < s2)
print('s1>=s2=', s1 >= s2)
print('s1<=s2=', s1 <= s2)

#overloading multiplication
class employee:
    def __init__(self,name,salery):
        self.name = name
        self.salery = int(salery)

    def __mul__(self, other):
        return self.salery * other.days

class timesheet:
    def __init__(self,name,days):
        self.name = name
        self.days = int(days)

e1 = employee('saikiran',10000000)
t1 = timesheet('saikiran',55)
print('total salery is=',e1 * t1)


#handling meathod requirements in python:


#with default arguements
class test:
    def sum(self,a=None,b=None,c=None):
        if a!= None and b!= None and c!= None:
            print('the sum of three numbers is=', a + b + c)
        elif a!= None and b!= None:
            print('the sum of two numbers is=', a + b)
        else:
            print('enter 2 or 3 numbers to perform sum!!')

c = test()
c.sum(22,55,77)
c.sum(22,55)
c.sum(22)
c.sum()

#with variable no of arguements:
class test:
    def sum(self, *a):
        total = 0
        for x in a:
            total = total + x
        print('the sum is=',total)


c = test()
c.sum(22,55,77)
c.sum(22,55)
c.sum(22)
c.sum()

#overriding
#meathod overriding   ( If the child class not satisfied with parent class implementation then child class is allowed to redefine that method in the child class based on its requirement)
class p:
    def property(self):
        print('land', 'cash', 'power')
    def marry(self):
        print('saikiran')

class c(p):
    def marry(self):
        print('reddy')

b = c()
b.marry()



class o:
    def property(self):
        print('land', 'cash', 'power')
    def marry(self):
        print('saikiran')

class u(o):
    def marry(self):
        super().marry()
        print('reddy')

b = u()
b.marry()


