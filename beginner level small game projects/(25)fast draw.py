import random
import sys
import time

print('fast draw by saikiran')
print()
print('time to test your reflexes and see if you are the fastest')
print('draw in the west!!!')
print('but you loose if you draw before the  DRAW appears ')
print()
print('press enter to begin')

while True:
    print()
    print('its high time noon')
    time.sleep(random.randint(20, 50) / 10.0)
    print('DRAW!!!!')
    drawtime = time.time()
    input()
    timeelapsed = time.time() - drawtime

    if timeelapsed < 0.01:
        print('you drew before srew appeared.....you loose!!!')

    elif timeelapsed > 0.3:
        print('you took', timeelapsed, 'seconds to draw too sloww')

    else:
        timeelapsed = round(timeelapsed, 4)
        print('you took', timeelapsed, 'to draw!!!!')
        print('you are the fastest draw in the west.....YOU WINNN!!!')

    print('enter quit to stop, or press enter to play again!!!')
    response = input('> ').upper()
    if response == 'QUIT':
        print('thanks for playing!!')
        sys.exit()


#practised
import random
import time
import sys

print('fast draw by g saikiran''')
print('press enter before draw')
print()
print('press enter to begin')

while True:
    print()
    print('its high time noon')
    time.sleep(random.randint(20, 50)  / 10.0)
    print('draw')
    drwatime = time.time()
    input()
    timeelapsed = time.time() - drwatime

    if timeelapsed < 0.01:
        print('you drew too early.......you loose!!!')

    elif timeelapsed > 0.03:
        print('you took', timeelapsed, 'tooo sloww')

    else:
        timeelapsed = round(timeelapsed, 4)
        print('YOU TOOK',timeelapsed,'to draw')
        print('you win')

    print('do you want to play again or quit')
    response = input('> ').upper()
    if response == 'quit':
        print('thank u for playing')
        sys.exit()
