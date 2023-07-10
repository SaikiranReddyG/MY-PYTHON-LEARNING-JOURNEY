import sys
print('number of arguments:', len(sys.argv), 'arguments.')
print('argument lists:', str(sys.argv))
x = int(sys.argv[1])
y = int(sys.argv[2])
z = x + y
print('x=',x,'y=',y,'z=',z)