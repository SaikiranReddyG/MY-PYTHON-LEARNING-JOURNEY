"""variable N follows 3 three rules
   if n is even >>>next n is n/2
   if n is odd  >>>next n is n*3+1
   if n is 1>>>> stop"""
import sys
import time
print('enter a string number (greater than 0) or QUIT')
response = input('> ')

if not response.isdecimal() or response == '0':
    print('enter an integer greater than zero')
    sys.exit()

n = int(response)
print(n, end='', flush=True)
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1

    print(',' + str(n), end=' ', flush=True)
    time.sleep(1)


print()
