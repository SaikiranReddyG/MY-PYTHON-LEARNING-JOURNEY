import math
import sys

print("factor finder by saikiran reddy g")

while True:  # main program loop
    print('enter a positive whole number to factor or QUIT')
    response = input('> ')
    if response.upper() == 'QUIT':
        print('thank you for playing')
        sys.exit()

    if not (response.isdecimal() and int(response) > 0):
        continue

    number = int(response)

    factors = []

    # find the factors of the number
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:  # if there is no remainder it is a factor.
            factors.append(i)
            factors.append(number // i)

    # convert to a set to get rid oof duplicate factors
    factors = list(set(factors))
    factors.sort()

    # display the results
    for i, factors in enumerate(factors):
        print(factors)
