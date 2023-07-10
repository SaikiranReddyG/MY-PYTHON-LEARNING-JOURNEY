import time

CLEAR = "\033[23"
CLEAR_AND_RETURN = "\033[H"


def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60
        print(f'{CLEAR_AND_RETURN}ALARM WILL SOUND IN:{minutes_left:02d}:{seconds_left:02d}')


minutes = int(input('how many minutes to wait:   '))
seaconds = int(input('how many seaconds to wait: '))
total_seconds = minutes + 60 + seaconds
alarm(total_seconds)