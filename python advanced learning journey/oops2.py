# inheritence


# By Composition   (Has - A Relationship):
class car:
    def __init__(self, carname, model, color):
        self.carname = carname
        self.model = model
        self.color = color

    def getinfo(self):
        print('the car details are carname{}carmodel{}carcolor{}'.format(self.carname, self.model, self.color))


class employee:
    def __init__(self, ename, eno, ecar):
        self.ename = ename
        self.eno = eno
        self.ecar = ecar

    def employeeinfo(self):
        print('the employee name is', self.ename)
        print('the employee no is ', self.eno)
        print('the employee car details is ')
        self.ecar.getinfo()


c = car('glanzaa', '3.5ve', 'redd')
e = employee('saikiran', 10000, c)
e.employeeinfo()


class X:
    a = 10

    def __init__(self):
        self.b = 20

    def m1(self):
        print('m1 meathod of X class:')


class Y:
    c = 30

    def __init__(self):
        self.d = 40

    def m2(self):
        print('m2 is meathod of Y class')

    def m3(self):
        x1 = X()
        print(x1.a)
        print(x1.b)
        x1.m1()
        print(Y.c)
        print(self.d)
        self.m2()
        print('m3 meathod of y class')


y1 = Y()
y1.m3()


# IS-A relationship
class p:
    a = 99

    def __init__(self):
        self.b = 97

    def m1(self):
        print("parent instance meathod")

    @classmethod
    def m2(cls):
        print('parent class meathod')

    @staticmethod
    def m3():
        print('parent static meathod')


class C(p):
    pass


c = C()
print(c.a)
print(c.b)
c.m1()
c.m2()
c.m3()


class pp:
    def m1(self):
        print('parent class meathod')


class C(pp):
    def m2(self):
        print('child class meathod')


c = C()
c.m1()
c.m2()


class r:
    a = 33

    def __init__(self):
        self.b = 44


class e:
    c = 44

    def __init__(self):
        super().__init__()  # (Line - 1)
        self.d = 55


c = e()
print(c.a, c.b, c.c, c.d)


# demo prgram for inheritence


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eatndrink(self):
        print('work all day and chill all night')

class  employee(person):
        def __init__(self,name,age,eno,esal):
            super().__init__(name,age)
            self.eno = eno
            self.esal = esal

        def work(self):
            print('the work is simple and easy')

        def empinfo(self):
            print('the emp name is=',self.name)
            print('the empage is=',self.age)
            print('the emp eno is=',self.eno)
            print('the emp esal is=',self.esal)
e = employee('sai',40,555,1000)
e.eatndrink()
e.work()
e.empinfo()

#IS-A vs HAS-A relationship
class car:
    def __init__(self,name,model,colour):
        self.name = name
        self.model = model
        self.colour = colour

    def getinfo(self):
        print('\tcarname is={}\t\ncarmodel is={}\t\ncar colour is={}\t'.format(self.name,self.model,self.colour))
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eatndrink(self):
        print('eat all day and chill all night')


class employee(person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno = eno
        self.esal = esal

    def work(self):
        print('work is eay and simple all day!!!!')
    def empinfo(self):
        print('emp name is=', self.name)
        print('emp age is=', self.age)
        print('emp no is=', self.eno)
        print('emp salery is=', self.esal)
        print('emp car info is=')


e = employee('saikiran',23,555,100000000000)
e. eatndrink()
e.work()
e.empinfo()

#Composition:
                             #Without existing container object if there is no chance of existing contained object then
                             #the container and contained objects are strongly associated and that strong association is nothing but Composition
#Aggregation:
                            #Without existing container object if there is a chance of existing contained object then the
                            #container and contained objects are weakly associated and that weak association is nothing but Aggregation.







#types of inheritence

#single inheritence       #(process of inherting properties from one class to another class )
class po:
    def m1(self):
        print('parent meathod!!!')

class op(po):
    def m2(self):
        print('child class meathod!!!')
c = op()
c.m1()
c.m2()


#Multi Level Inheritance:         (the process of inherting properties from multi classes to a single class by the cocept of one after another)
class s:
    def m1(self):
        print('parent class meathod')
class sa(s):
    def m2(self):
        print('child class meathod')

class sai(sa):
    def m3(self):
        print('sub child class meathod')

saik = sai()
saik.m1()
saik.m2()
saik.m3()

#Hierarchical Inheritance:     (process of inherting properties from one class to multiple classes which are present in same level )
class p:
    def m1(self):
        print('parent class meathod')
class c1(p):
    def m2(self):
        print('child 1 meathod')

class c2(p):
    def m3(self):
        print('sub child 2 meathod')

c = c1()
c.m1()
c.m2()
cc = c2()
cc.m1()
cc.m3()


#multiple inhertence     (inherting properties of multiple classes into single class at a time)
class p:
    def m1(self):
        print('parent class meathod')
class c1:
    def m2(self):
        print('child 1 meathod')

class c2(p,c1):
    def m3(self):
        print('sub child 2 meathod')

c = c2()
c.m1()
c.m2()
c.m3()

#hybrid inheritence           (combinaation of single,multi level,multiple and hieraciel inheritence )
#cyclic inheritence            (inherting properties from one class to anther class in a cyclic way is called cyclic inhertence)




#Method Resolution Order (MRO):        (it follows DLR(depth first left to right) i.e child will get more priority than parent and left parent will get more priority than right parent)


#demo1 for MRO(meathod resolution order)
#question --
#(mro(A) = A, object
#mro(B) = B, A, object
#mro(C) = C, A, object
#mro(D) = D, B, C, A, object)

class A : pass
class B(A) : pass
class C(A) : pass
class D(B,C) : pass
print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())

#demo2 for MRO(meathod resolution order)
#question2 --
#mro(A)=A,object
#mro(B)=B,object
#mro(C)=C,object
#mro(X)=X,A,B,object
#mro(Y)=Y,B,C,object
#mro(P)=P,X,A,Y,B,C,object
class A:
    def m1(self):
        print('class A meathod!!')
class B:
    def m1(self):
        print('class B meathod!!')

class C:
    def m1(self):
        print('class C meathod!!')

class X(A,B):
    def m1(self):
        print('cass X meathod')

class Y(B,C):
    def m1(self):
        print('class Y meathod!!')
class P(X,Y,C):
    def m1(self):
        print('class P meathod!!')


p = P()
p.m1()

#super() meathod  (built in meathod which is useful to call super class constructors,variables and meathods of child class)
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print('name of person is=',self.name)
        print('age of the person is=',self.age)

class student(person):
    def __init__(self,name,age,rollno,marks):
        super().__init__(name,age)
        self.rollno = rollno
        self.marks = marks

    def display(self):
        super().display()
        print('rollno of student is=',self.rollno)
        print('marks of the student is==',self.marks)


d = student('saikiran,23,55,99')
d.display()


#to call a meathod of a patiular super class
class A:
    def m1(self):
        print('class A meathod!!')

class B(A):
    def m1(self):
        print('class B meathod!!')


class C(B):
    def m1(self):
        print('class c meathod!!')

class D(C):
    def m1(self):
        print('class D meathod!!')

class E(D):
    def m1(self):
        print('class E meathod!!')
        A.m1(self)                           #this function helps in calling a paticular super function

e = E()
e.m1()


class R:
    def __init__(self):
        print('parent constructor')
    def m1(self):
        print('parent instance meathod')

    @classmethod
    def m2(cls):
        print('PARENT CLASS MEATHOD')


    @staticmethod
    def m3():
        print('parent static meathod')

class e(R):
    def __init__(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
    def m1(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()


c = e()
c.m1()




