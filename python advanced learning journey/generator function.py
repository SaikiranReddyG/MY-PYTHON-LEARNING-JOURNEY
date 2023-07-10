#GENERATOR FUNCTIONS  (generate a sequence of values)
import time
def countdown(num):
    print('start countdown')
    while num>0:
        time.sleep(1)
        yield num
        num -= 1

values = countdown(5)
for x in values:
    print(x)

#generate first n numbers
import time
def first(num):
    n = 1
    while n<=num:
        time.sleep(1)
        yield n
        n = n + 1

values = first(8)
for x in values:
    print(x)


#generate fibinoochi numbers:

import time
def fib():
    a,b = 0,1
    while True:
        time.sleep(1)
        yield a
        a, b = b, a + b

for f in fib():
    if f>100:
        break
    print(f)



