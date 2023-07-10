#EXCEPTIONAL HANDLING
#using try except
try:
    x = int(input('enetr 1st number'))
    y = int(input('enter your 2nd number'))
    print(x/y)
except ZeroDivisionError :
    print('zero division is not possible!!!')
except ValueError:
    print('enter only interger vlaues!!!!')


#using default except block
try:
    x = int(input('enetr 1st number'))
    y = int(input('enter your 2nd number'))
    print(x/y)
except ZeroDivisionError :
    print('zero division is not possible!!!')
except :
    print('enter only interger vlaues!!!!')

  #using finally block     ( main purpose of finally block is to maintain clean up code.)

try:
    print('try')

except:
    print('except')

finally:
    print('finally')


try :
    print('try')
    print(10/0)
except ZeroDivisionError :
    print('except')

finally :
    print('finally')

#raise exception
class too_younge_excpetion(Exception):
    def __init__(self,arg):
        self.msg = arg

class too_old_exception(Exception):
    def __init__(self,arg):
        self.msg = arg

class perfect_age(Exception):
    def __init__(self,arg):
        self.msg = arg

age = int(input('enter your age here='))
if age <= 18:
    raise too_younge_excpetion('you are too younge to get married....walt a little longer!!!')
elif age >= 60:
    raise too_old_exception('you are too old to get married!!!!')
else:
    raise perfect_age('you are in the right age to get married....')


