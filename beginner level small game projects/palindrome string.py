x = int(input('enter a number to check if it is a palindrome'))
if x <= 0:
    print("enter a number grater than zero")
elif x == int(str(x)[::-1]):
    print('the given number {} is a palindrome'.format(x))
else:
    print('the number entered is not a palindrome')
