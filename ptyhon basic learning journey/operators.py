#1>>>arthemetic operators
a = 55555
b = 44444
print('a+b=',  a + b )      #addition operator
print('a-b=',  a - b )      #subraction operator
print('a*b=',  a * b )      #multiplication operator
print('a/b=',  a / b )      #division operator
print('a//b=',  a // b )     #floor division operator
print('a%b=',  a % b )
print('a**b=',  a ** b )

#2>>>relational operators
c = 5555
d = 4444
print('c>d=',c>d)
print('c<d=',c<d)
print('c <= d=',c>=d)
print('c >= d=',c>=d)

#3>>>equality operators
print(55 == 555)
print(55 != 555)

#4>>>logical operators

#and operator   If both arguments are True then only result is True
#or operator    If atleast one arugemnt is True then result is True
#not operator   compliment

#5>>> bitwise operator

# (&)  If both bits are 1 then only result is 1 otherwise result is 0
print(5&6)
# (|) If atleast one bit is 1 then result is 1 otherwise result is 0
print(5|6)
# (^)  If bits are different then only result is 1 otherwise result is 0
print(5^6)
#(~)  bitwise complement operator
print(~5)
#(<<)  Bitwise Left Shift
print(5<<6)
#(>>)  Bitwise Right Shift
print(5>>6)

#6>>>assignment operator
y = 55
y += 555
print(y)

a = 55
a &= 555
print(a)

#7>>>conditional operator
a,b = 55,555
x = 5555 if a>b else 6666
print(x)

     #finding min or max value of two numbers using coditional statment
a = int(input('enter 1st number'))
b = int(input('enter 2nd number'))
x = a if a<b   else b
print('minimum number is', x)

c = int(input('enter 1st number'))
d = int(input('enter 2nd number'))
x = c if c>d else d
print('maximum number is', x)

                           #finding min or max value of three numbers using coditional statment
a = int(input('enter the first number'))
b = int(input('enter the second number'))
c = int(input('enter the third number'))
x = a if a<b and a<c else b if b<a and b<c else c
print('the minimum number is:', x)

s = int(input('enter the first number'))
t = int(input('enter the second number'))
u = int(input('enter the third number'))
print('all the numbers are equal' if s==t==u else 'first number is the minimum' if s<t and s<u  else 'seacond number is the minimum' if t<s and t<u else 'third number is the minimum' )


#8>>>special operators
                  #identity operator
a = 55
b = 55
print(a is b)
print(a is not b)

                  #membership operator
v = "gangula saikiran reddy"
print("s" in v)
print("z" in v)