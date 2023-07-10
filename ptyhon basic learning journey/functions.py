#FUNCTIONS>>> (If a group of statements is repeatedly required then it is not recommended to write these statements everytime seperately.We have to define these statements
# as a single unit and we can call that unit any number of times based on our requirement without
# rewriting. This unit is nothing but function.)

#2 TYPES OF FUNCTIONS 1>builtin  2>user defined

#program function to take name of the student as input and print wish message by name.
def wish(name):
    print('hello',name,'good morning!!!')
wish('saikiran')
wish('reddy')

# program function to take number as input and print its square value
def squareof(number):
    print('square of:',number,'is',number*number)
squareof(4)
squareof(8)

#program to check if the given function is even or odd
def even_odd(num):
    if num%2 == 0:
        print('the num is even')
    else:
        print('the num is odd')
even_odd(56)
even_odd(22)
even_odd(99)

#function to find factorial of a given num
def fact(num):
    result = 1
    while num >=1:
        result = result*num
        num = num-1
    return result
for i in range(1,5):
    print('the factorial of ',i, 'is',fact(i))


#program to return multiple values from a funtion
def sum_sub(a,b):
    sum = a + b
    sub = a - b
    return sum,sub
x,y = sum_sub(500,400)
print('the sum is:',x)
print('subraction is :',y)

def calc(a,b):
    sum = a+b
    sub = a-b
    mul = a*b
    div = a/b
    return sum,sub,mul,div
t = calc(400,500)
print('the results are:')
for i in t:
    print(i)

#ARGUEMENTS

#1>>positionsal arguements   ( arguments passed to function in correct positional order.)
def sub(a,b):
    print(a-b)

#2>>keyword arguement  ()
def wish(name,msg):
    print('hello',name,msg)
wish(name="saikiran",msg='gud mrng')
wish(name='reddy',msg='hw r u')

#3>>variable length arguements()
def sum(*n):
    total = 0
    for n1 in n:
        total = total + n1
    print('the sum=',total)
sum()
sum(31,3645,78)
sum(1,4,6)




#variables
#1>>>global variables  (the varables that are declared outside the function)
a = 99
def fi():
    print(a)
def fy():
    print(a)

#2>>local variables    (variables that are declared inside a function)
def fi():
    a =99
    print(a)
def fy():
    a = 77
    print(a)


#global keyword (to declare a global varable inside a function)
a = 99         #without global keyword
def fi():
    a = 789
    print(a)
def fy():
    print(a)


a = 99        #with global key word
def fi():
    global a
    a = 789
    print(a)
def fy():
    print(a)


#recursive function   (a function that calls itself)
      #program to find factorial of given function with recursion
def factorial(n):
    if n==0:
        result = 1
    else:
        result = n * factorial(n-1)
    return result

print('factorial of 4 is=',factorial(4))
print('factorial of 8 is=',factorial(8))


#lambda function( write very concise code so that readability of the program will be improved)


       #program to create almbda function to find square of a given number
s = lambda n:n*n
print('square of 4 is:',s(4))
print('square of 8 is:',s(8))

      #sum of two given numbers
s = lambda a,b,c:a+b+c
print('sum of (10,20,30) is=',s(10,20,30))


  #program ot filtr only  even numbers from the list

      #without using lambda function
def is_even(x):
    if x%2==0:
        return True
    else:
        return False
r = [2,43,56,86,2,4,43]
re = list(filter(is_even,r))
print(re)


       #using lambda function
r = [2,43,56,86,2,4,43,45,67,78,1,2,3,45]
l = list(filter(lambda x:x%2==0,r))
l2 = list(filter(lambda x:x%2!=0,r))
print(l)
print(l2)


#map() (for every element present in the given sequence perform a operation and generate a new element)
        #program to perform double for each element of the list and generate new list
#without using lambda
k = [56,86,2,4,43,45,67,78,1,2,3,45]
def double_it(x):
    return 2*x
kk = list(map(double_it,k))
print(kk)

#using lambda function
p = [56,86,2,4,43,45,67,78,1,2,3,45]
pp = list(map(lambda x:2*x,p))
print(pp)

# to find square of given numbers
o = [56,86,2,4,43,45,67,78,1,2,3,45]
oo = list(map(lambda x:x*x,o))
print(oo)


#applying map function to multiple numbers
u = [2,4,43,45,67]
v = [2,4,43,45,67]
w = list(map(lambda x,y:x*y,u,v))
print(w)

#reduce()      (reduse sequence of elements into singlle element applying specific function)
from functools import *
x = [10,20,30,40,50,60,70,80,90,100]
result = reduce(lambda x,y:x + y,x)
print(result)
result1 = reduce(lambda x,y:x*y,x)
print(result1)

from functools import *
result3 = reduce(lambda x,y:x+y,range(1,55))
print(result3)

#function aliasing (giving another name to existing function)
def wish(name):
    print('good morning:',name)
greeting=wish
print(id(wish))
print(id(greeting))

greeting('saik')
wish('reddy')

#nested function()     (declare a function inside another function)

def outer():
    print('this is outer function')
    def inner():
        print('this is inner function')
    print('outer function calling inner function')
    inner()
outer()

 #another example
def outer():
    print('this is outer function')
    def inner():
        print('this is inner function')
    print('outer function calling inner function')
    return inner

ff = outer()
print(ff)

#f1 = outer            (assigning another name to f1 as outer)
#f1 = outer()           (calling outer function usinf f1)
