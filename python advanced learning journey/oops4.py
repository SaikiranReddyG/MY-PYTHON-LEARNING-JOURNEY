#ABSTRACT MEATHOD   (abstract method has only declaration  but not implementation.)
                    #@abstractmethod decorator present in abc module. Hence compulsory we should
                      #import abc module,otherwise we will get error.

from  abc import *
class test:
    @abstractmethod
    def m1(self):
        pass


from abc import *
class veichle:
    @abstractmethod
    def noofwheels(self):
        pass

class bus:
    def noofwheels(self):
        return 10

class auto:
    def noofwheels(self):
        return 3

class bike:
    def noofwheels(self):
        return 2

b = bus()
a = auto()
k = bike()
print(b.noofwheels())
print(a.noofwheels())
print(k.noofwheels())

#interfaces in python
from abc import *
class DBinterface(ABC):
    @abstractmethod
    def connect(self): pass

    @abstractmethod
    def disconnect(self): pass

class Oracle(DBinterface):
    def connect(self):
        print('connecting to Oracle database!!')

    def disconnect(self):
        print('disconnecting from Oracle database!!!')

class syron(DBinterface):
    def connect(self):
        print('connecting to syron database!!')


    def disconnect(self):
        print('disconnecting from syron database!!!')


dbname = input('enter database name')
classname = globals()[dbname]
x = classname()
x.connect()
x.disconnect()


          #reading class name from the file
from abc import *
class printer:
    @abstractmethod
    def printing(self,text): pass

    @abstractmethod
    def diconnecting(self): pass


class espon(printer):
    def printing(self,text):
        print('printing from espon printer.....')
        print(text)

    def diconnecting(self):
        print('disconnecting from the printer!!!!')

class hpprinter(printer):
    def printing(self,text):
        print('printing from hpprinter......')
        print(text)

    def diconnecting(self):
        print('disconnecting from the printer!!!!!')

with open(r'C:\Users\SUPER\directoryy') as f:
    pname = f.readline()


classname = globals()[pname]
x = classname()
x.printing('the data to be printed is')
x.disconnecting()


#public protected and private attributes

class Test:
    x = 20
    _y = 30
    __z = 99
    def m1(self):
        print(Test.x)
        print(Test._y)
        print(Test.__z)
t = Test()
t.m1()
print(Test.x)
print(Test._y)
print(Test.__z)

#accessing private variables from outside the class
class texting:
    def __init__(self):
        self.__x = 999


tt = texting()
print(tt._texting__x)


#__str__() method:
class student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno


    def __str__(self):
        return "the studentname is={} and rollno is={}".format(self.name,self.rollno)


s1 = student('saikiran',408)
s2 = student("reddy",444)
print(s1)
print(s2)
