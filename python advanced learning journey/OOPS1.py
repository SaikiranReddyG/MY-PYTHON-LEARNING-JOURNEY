#class   ( In Python every thing is an object. To create objects we required some Model or Plan or Blue print, which is nothing but class.)


#DEFINE A CLASS
class student:
    "this is student class with required data"
print(student.__doc__)
help(student)

#example of class
class students:
    "this is created by saikiran"
    def __init__(self,name,age,marks):
        self.name = 'saikiran'
        self.age = '24'
        self.marks = 90

    def talk(self):
        print('my name is=',self.name)
        print('my age is=',self.age)
        print('my marks are=',self.marks)
ss = students('saikir',22,99)
ss.talk()

#program to create student class and create a object to it
class studentss:
    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def talk(self):
        print('my name is =',self.name)
        print('my rollno is =', self.rollno)
        print('my marks are =', self.marks)
s1 = studentss("saik",18,99)
s1.talk()

#program to show constructor only executes only once per object
class test:
    def __init__(self):
        print('contructor execution')
    def my(self):
        print('meathod execution.........')

t1 = test()
t2 = test()
t3 = test()
t1.my()


#program to show constructor only executes only once per object
class student:
    "student class with required data"
    def __init__(self,x,y,z):
        self.name = x
        self.rollno = y
        self.marks = z

    def display(self):
        print('student name:{}\n rollno:{}\n marks:{}',format(self.name,self.rollno,self.marks))

s1 = student('saik',22,88)
s1.display()
s2 = student('reddy',29,98)
s2.display()
s3 = student('kiran',77,99)
s3.display()


#declaring instance variable >>>inside constructor
class employee:
    def __init__(self):
        self.eno = 99
        self.ename = 'saikiran'
        self.esal = 990099

v = employee
print(v.__dict__)

#declaring instance variable >>>inside instance meathod
class test:
    def __init__(self):
        self.a = 99
        self.b = 98
    def my(self):
        self.c = 97

t = test()
t.my()
print(t.__dict__)

#declaring instance variable >>>outside of class using object reference variable
class teest:
    def __init__(self):
        self.a = 99
        self.b = 98
    def my(self):
        self.c = 97

t = teest()
t.my()
t.d = 96
print(t.__dict__)


#accessing instance variable

class test1:
    def __init__(self):
        self.a = 99
        self.b = 98
    def display(self):
        print(self.a)
        print(self.b)
t = test1
t.display()
print(t.a,t.b)


#delete instance variable from the object
class trying:
    def __init__(self):
        self.a = 999
        self.b = 998
        self.c = 997
        self.d = 996


    def tried(self):
        del self.d


ty = trying()
print(ty.__dict__)
ty.tried()
print(ty.__dict__)
del ty.c
print(ty.__dict__)

#: The instance variables which are deleted from one object,will not be deleted from other objects.

class toying:
    def __init__(self):
        self.a = 999
        self.b = 998
        self.c = 997
        self.d = 996


to = toying()
too = toying()
del to.c
print(to.__dict__)
print(too.__dict__)

#If we change the values of instance variables of one object then those changes won't be
                                                      #reflected to the remaining objects

class tom:
    def __init__(self):
        self.a = 999
        self.b = 998
        self.c = 997
        self.d = 996


to = tom()
too = tom()
to.a = 889
to.b = 888
to.c = 887
to.d = 886
print(to.__dict__)
print(too.__dict__)


#static variable
class test:
    x = 10
    def __init__(self):
        self.y = 200

t1 = test()
t2 = test()
print('t1=',t1.x,t1.y)
print('t2=',t2.x,t2.y)
test.x = 8989
t1.y = 9898
print('t1=',t1.x,t1.y)
print('t2=',t2.x,t2.y)

#various places to access static variable

class testing:
    a = 9090
    def __init__(self):
        b = 8080

    def m1(self):
        c = 7070

    @classmethod
    def m2(cls):
        cls.d1 = 6060
        testing.d2 = 5050
    @staticmethod
    def m3():
        testing.e = 4040


print(testing.__dict__)
t = testing()
print(testing.__dict__)
t.m1()
print(testing.__dict__)
testing.m2()
print(testing.__dict__)
testing.m3()
print(testing.__dict__)
testing.f = 3030
print(testing.__dict__)

#access static variables
class tst:
    a = 9090
    def __init__(self):
        print('01 print=',self.a)
        print('02 print=',tst.a)


    def m1(self):
        print('03 print=',self.a)
        print('04 print=',tst.a)

    @classmethod
    def m2(cls):
        print('05 print=',cls.a)
        print('06 print=',tst.a)

    @staticmethod
    def m3():
        print('07 print=',tst.a)


t = tst()
print('1st print=',tst.a)
print('2nd print=',t.a)
t.m1()
t.m2()
t.m3()


#modify the values of static variable

class ramp:
    a = 9091
    @classmethod
    def m1(cls):
        cls.a = 8081
    @staticmethod
    def m2():
        ramp.a = 7071

print('1st print=',ramp.a)
ramp.m1()
print('2nd print=',ramp.a)
ramp.m2()
print("3rd print=",ramp.a)


#delete Static  Variable of a class:
class dean:
    a = 999
    @classmethod
    def m1(cls):
        del cls.a
dean.m1()
print(dean.__dict__)


#modify or delete static variables only by using classname or cls variable.

import sys


class customer_banking:
    bankname = 'reddy^s bank'

    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amt):
        self.balance = self.balance + amt
        print('the total balance in your account after deposit of', amt, 'is', self.balance)

    def withdrawl(self, amt):
        if amt > self.balance:
            print('insufficient funds in your account....try less amount')
            sys.exit()
        self.balance = self.balance - amt
        print('the balance left in your account after withdrawl of', amt, 'is', self.balance)


print('welcome to our bank= ', customer_banking.bankname)
name = input('enter your name')
c = customer_banking(name)
while True:
    print('d-deposit\nw-withdrawl\ne-exit')
    option = input('choose your option')
    if option == 'd' or option == 'D':
        amt = float(input('enter your amount'))
        c.deposit(amt)

    elif option == 'w' or option == 'W':
        amt = float(input('enter your amount here'))
        c.withdrawl(amt)

    elif option == 'e' or option == 'E':
        print('thank you for using our bank!!!!')
        sys.exit()


    else:
        print('the syntax entered is invalid.........try again!!! ')


    break

#local variables    (to meet temporary requirements a programmer declares variables inside a meathod)
                    #created at the time of execution and deleted afterwards

class test:
    def m1(self):
        a = 700
        print(a)

    def m2(self):
        b = 600
       # print(a)
        print(b)
t1 = test()
t1.m1()
t1.m2()

#methods
          #1>>instance meathods
class students:
    def __init__(self,name,marks):
        self.name = name
        self.marks = int(marks)

    def m1(self,feedback):
        self.feedback = feedback


    def display(self):
        print('hi',self.name)
        print('your marks are',self.marks)



    def gradeit(self):
        if self.marks >= 95:
            print('excellent score')
            self.feedback ='good job keep it up!!!!!!!!!!!!!!'
            print(self.feedback)

        elif self.marks >= 85:
            print('terrific score')
            self.feedback = ('good score but try to get better!!!!!')
            print(self.feedback)

        elif self.marks >= 65:
            print('good score')
            self.feedback = "try harder next time!!!"
            print(self.feedback)

        elif self.marks >= 35:
            print('try harder!!!')
            self.feedback = "you have barely made it out this time!! "
            print(self.feedback)

        elif self.marks <=34:
            print('you have failed this exam!!')
            self.feedback = 'you better not repeat this next time!'
            print(self.feedback)

        else:
            print('the data entered is incorrect,, check and re enter data')


n = int(input('enter total no of students!!!'))
for i in range(n):
    name = input('enter the name of the student')
    marks = input('enter the marks of the student')
    s = students(name,marks)
    s.display()
    s.gradeit()
    print()

#setter and getter meathods
class student:
    def setname(self,name):
        self.name = name


    def getname(self,name):
        return self.name

    def setmarks(self,marks):
        self.marks = marks

    def getmarks(self,marks):
        return self.marks


v = int(input('enter no of students!!!!'))
for i in range(v):
    s = student()
    name = input('enter your name')
    s.setname(name)
    marks = input('enter your marks!!!!')
    s.setmarks(marks)
    print('hi', s.getname(name))
    print('your marks are', s.getmarks(marks))
    print()

#class meathod
class animal:
    legs = '4'
    @classmethod
    def walks(cls,name):
        print('{} walks with {}legs.....'.format(name,cls.legs))


animal.walks('pig')


#Program to track the Number of Objects created for a Class:
class test:
    count = 0
    def __init__(self):
        test.count = test.count + 1
    @classmethod
    def noofobjects(cls):
        print('the no of objects for test class',cls.count)

t1 = test()
t2 = test()
test.noofobjects()
t3 = test()
t4 = test()
t5 = test()
test.noofobjects()

#static  meathods
class arthematics:
    @staticmethod
    def add(x,y):
        print('the sum is',x+y)

    @staticmethod
    def sub(x, y):
        print('the sub is', x - y)

    @staticmethod
    def mul(x, y):
        print('the mul is', x * y)

arthematics.add(200,700)
arthematics.sub(200,300)
arthematics.mul(446,700)


#passing members form one class to another
class employee:
    def __init__(self,eno,ename,esal):
        self.eno = eno
        self.ename = ename
        self.esal = esal


    def display(self):
        print('the employee no is',self.eno)
        print('the employee name is', self.ename)
        print('the employee salery is', self.esal)

class test:
    def modify(emp):
        emp.esal = emp.esal + 10000
        emp.display()
e = employee(100,"saik",10000)
test.modify(e)

#inner classes

class outer:
    def __init__(self):
        print('the outer class object')

    class inner :
        def __init__(self):
            print('the inner class object')


        def m1(self):
            print('the inner of inner object')

o = outer()
i = o.inner()
i.m1()
outer().Inner().m1()


class dateofbirth:
    def __init__(self):
        self.name = "name"
         #self.db = Dob()

    def display(self):
        print('name is',self.name)

    class dob:
        def __init__(self):
          self.dd = 22
          self.mm = 3
          self.yy = 2000

        def display(self):
            print('dob = {}/{}/{}'.format(self.dd,self.mm,self.yy))


p = dateofbirth()
p.display()
x = p.db
x.display()



class human:
    def __init__(self):
        self.name = 'saikiran'
        self.head = self.Head()
        self.brain = self.Brain()


    def dispaly(self):
        print('name is',self.name)

    class Head:
        def talk(self):
            print('talking')


    class Brain:
        def think(self):
            print('thinking')


h = human()
h.dispaly()
h.head.talk()
h.brain.think()



#garbage collection  (main objective of Garbage Collector is to destroy useless objects.)
                      # If an object does not have any reference variable then that object eligible for Garbage Collection.


#enabling and disabling garbage collection


#gc.isenabled()  Returns True if GC enabled
#gc.disable() To disable GC explicitly
#gc.enable() To enable GC explicitly

import gc
print(gc.isenabled())
gc.disable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled())

#Destructors:
#Destructor is a special method and the name should be __del__
#Just before destroying an object Garbage Collector always calls destructor to perform clean up activities

import time
class test:
    def __init__(self):
        print('object intialization')

    def __del__(self):
        print('fulfilling last wish and performing clean up activities')

t1 = test()
t1 = None
time.sleep(5)
print('end of applications')









