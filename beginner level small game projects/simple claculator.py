"""create a simple calculator that performs basic arthrematic operations"""
import  math
def calculator(num1, num2, operation):
    if operation == '+':
        return num1 + num2

    elif operation == '-':
        return num1 - num2

    elif operation == '*':
        return num1 * num2

    elif operation == '**':
        return num1 ** num2

    elif operation == '/':
        return num1 / num2

    elif operation == 'sqrt':
        return  math.sqrt(num1), math.sqrt(num2)

    else:
        return 'I dont recognize this operation'

try:

    num1 = float(input('enter the 1st number'))
    num2 = float(input('enter the 2nd number'))
    operation = input('enter the operation among ((+ - * ** /  sqrt)) ')

except ValueError:
    print('invalid input please enter a an integer only')
    exit()


result = calculator(num1, num2, operation)
if type(result) == str:
    print(result)
else:
    print('the result is:', result)



#practiced:
import math


def claclulator(num1, num2, operation):
    if operation == '+':
        print('ohh you chose addition!,, the result is')
        return num1 + num2

    elif operation == '-':
        print('ohh you chose subraction!,, the result is')
        return num1 - num2

    elif operation == '*':
        print('ohh you chose multiplication!,, the result is')
        return num1 * num2

    elif operation == '**':
        print('ohh you chose square!,, the result is')
        return num1 ** num2

    elif operation == '/':
        print('ohh you chose division!,, the result is')
        return num1 / num2

    elif operation == 'sqrt':
        print('ohh you chose square root!,, the result is')
        return math.sqrt(num1), math.sqrt(num2)

    else:
        return 'invalid operation......it cant be done'


try:
    num1 = float(input('enter the 1st num here!!'))
    num2 = float(input('enter the 2nd num here'))
    operation = input('enter the operation you need to perform here!!!! ((+ - * ** / sqrt)) ')

except ValueError:
    print('enter only integer value')
    exit()

result = claclulator(num1, num2, operation)
if type(result) == str:
    print(result)

print('the result you need is', result)
