#flow control explains the order in which the statments will be executed
                         #conditional statments
#if()
name = input('enter your name')
if name ==('saikiran'):
    print('hi sai hw are u')
print('good morning')

#if else()
name = input('enter ur name')
if name == 'saikiran':
    print('hello sai hw r u')
else:
    print('hi guest hw r u')
print('good morning')

#if elif else
mobile_brand = input('the brand name of the mobile you need')
if mobile_brand ==('iphone'):
    print('its tooo expensive')
elif mobile_brand ==('android'):
    print('in what range do you need')
else:
    print('we donot have that brand sir')
print('thank u')

   #program to find the biggest of three numbers
num1 = int(input('enter the 1st num'))
num2 = int(input('enter the 2nd num'))
num3 = int(input('enter the 3rd num'))
if num1>num2 and num1>num3:
    print('num1 is the biggest num')
elif num1==num2 and num1==num3:
    print('all the numbers are equal')
elif num1==num2 and num1<num3:
    print('num3 is the biggest number')
elif num1==num2 and num1>num3:
    print('num3 is the smallest number')
elif num2==num3 and num1>num2:
    print('num1  is the biggest number')
elif num2==num3 and num1<num2:
    print('num1  is the smallest number')
elif num3>num1 and num3>2:
    print('num3 is the biggest num')
elif num2>num1 and num2>num3:
    print('num2 is the biggest num')
else:
    print('enter only positive integers')

   #program to check whether the given number is even or odd
num = int(input('enter any positive integer'))
if num % 2 == 0:
    print('the given number is even')
if num % 2 != 0:
   print('the given num is odd')
else:
    print('the given num is neither even or odd')

      #program to check if the given num is betweem 1 to 100
int1 = int(input('enter any positive integer'))
if int1>=0 and int1<=100:
    print('the given num lies between 1 and 100')
else:
    print('the num is not in the given range')

    #program to print given num in english
z = int(input('enter the integer num'))
if z==0:
    print('zero')
elif z==1:
    print('one')
elif z==2:
    print('two')
elif z==3:
    print('three')
elif z == 4:
    print('four')
elif z==5:
    print('five')
elif z==6:
    print('six')
elif z == 7:
    print('seven')
elif z ==8:
    print('eight')
elif z==9:
    print('nine')
else:
    print('enter a valid integer')

