#conditional statment in python
x = int(input('enter a number'))
y = int(input('enter a number'))
z = int(input('enter a number'))
if x > y and x > z :
    print('x is the greatest')
elif y > x and y > z :
    print('y is the greatest')
elif z > x and z > y :
    print('z is the greatest')
else :
    print('fuckoff')
