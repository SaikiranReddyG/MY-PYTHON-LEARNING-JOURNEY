#MODULES     (group of functoins, variables and classesd saved to a file )
#importing a module
import __init__
print(__init__.x)
__init__.add(200,500)
__init__.sub(200,5000)

#renaming a module as importing
import __init__ as uv
print(uv.x)
uv.add(20000,60000)
uv.sub(20000,59959)

#from import
from __init__ import x,add
print(uv.x)
uv.add(200099,6000)


#possibilities of module
                 # (import modulename)
                # (import module1,module2,module3)
               # (import module1 as m)
              # (import module1 as m1,module2 as m2,module3)
             # (from module import member)
            # (from module import member1,member2,memebr3)
           # (from module import memeber1 as x)
          # (from module import *)


#member aliasing
from __init__ import x as y,add as sum
print(y)
sum(3030,40404)


#reload()    (after loading a module if it is updated outside then updated version of module1 is not available to our program.)
              #(using reload module we can ensure that updated version is always available to our program)
import __init__
print(x)
from imp import reload
reload(__init__)
print(x)


#finding members of module by using dir() function

                            #dir()  To list out all members of current moduledir      (moduleName)  To list out all members of specified module
import data_types
print(dir(data_types))

#special variable   (__name__):
#1>>If the program executed as an individual program then the value of this variable is (__main__)
#2>>>If the program executed as a module from some other program then the value of this variable is the name of module where it is defined.
def ty():
    if __name__ == '__main__':
        print('code is executed as program')
    else:
        print('code is executed as module of another program')
ty()

import __init__
__init__.ty()


#math module
from math import *
print('sqrt is=',sqrt(9090))
print('ceil function is=',ceil(10.1))
print('floor function is =',floor(10.1))
print('fabs function is=',fabs(10.9))
print('fabs functiion is=',fabs(-10.99))


#random() function
from random import *
for i in range(10):
    print('random function is ',random())

#randint() function
from random import *
for i in range(10):
    print('randint function is ',randint(1,999))


#uniform() functiom
from random import *
for i in range(10):
    print('uniform function is ',uniform(1,10))

#randrange() function
from random import *
for i in range(10):
    print('randrange function is ',randrange(10))


from random import *
for i in range(10):
    print('randrange function is ',randrange(1,11,2))


#choice() function
from random import *
f =['h','g','s','t','a','rea','asa']
for i in range(10):
    print('choice function is=',choice(f))


