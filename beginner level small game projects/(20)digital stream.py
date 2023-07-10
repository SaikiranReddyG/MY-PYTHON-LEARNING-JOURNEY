import random
import shutil
import sys
import time

# set up constants
MIN_STREAM_LENGTHS = 6
MAX_STREAM_LENGTHS = 14
PAUSE = 0.1
STREAM_CHARS = ['0', '1']

# Density
DENSITY = 0.02

# terminal size
WIDTH = shutil.get_terminal_size()[0]
WIDTH -= 1
print("digital stream by saikiran reddy")
print('press ctrl-c to quit')
time.sleep(2)

try:
    # for each coloumn when the counter is 0, no stream is shown
    # other wise it acts as counter for how many times 0, 1 is shown
    COLOUMNS = [0] * WIDTH
    while True:
        # set up counter for each coloum
        for i in range(WIDTH):
            if COLOUMNS[i] == 0:
                if random.random() <= DENSITY:
                    COLOUMNS[i] = random.randint(MIN_STREAM_LENGTHS, MAX_STREAM_LENGTHS)

            if COLOUMNS[i] > 0:
                print(random.choice(STREAM_CHARS), end=' ')
                COLOUMNS[i] -= 1
            else:
                print(' ', end='')

        print()
        sys.stdout.flush()
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()
