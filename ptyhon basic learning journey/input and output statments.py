#input
             #program to read two numbers from keyboard and print sum
x = input('enter 1st num')
y = input('enter 2nd num')
i = (int(x))
j = (int(y))
print('sum of two numbers is:', i+j)

              #read multiple values from key board in a single line
x,y = [int(z) for z in input('enter two numbers').split()]
print('product of two num is:', x*y)

o,p,d = [float(f) for f in input('enter three numbers').split(',')]
print('sum of three float numbers is:', o+p+d)

#eval()
                  #eval() function takes a string and evaluate the result
x = eval(input('enter expression:'))
print(x)


#command line arguments        ( The Argument which are passing at the time of execution are called Command Line Arguments.)
from sys import argv
sum=0
args=argv[1:]
for x in args :
   n=int(x)
   sum=sum+n
print("The Sum:",sum)


#outputs
           #form1   PRINT WITHOUT ARGUMENT
print()
          #form2    print using escape charecters, different operators
print('hello')
print('hello \n world')
print('hello \t world')
print(10*'hello world')
print('hello'+'world')
print('hello','world')
         #form3 print with variable arguments
a,b,c = 10,20,30
print('the values are:',a,b,c)

a,b,c = 10,20,30   # specify seperator using sep attribute
print(a,b,c,sep=',')
print(a,b,c,sep=';')

a,b,c = 10,20,30    # specify seperator using end attribute
print(a,b,c,end='')


