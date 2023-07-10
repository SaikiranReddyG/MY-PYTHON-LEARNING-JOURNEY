import  random


def roll_dice():
    return random.randint(1, 6)


print('welcome to the dice roller!!!')

while True:
    input('press enter to roll the dice......')
    roll_result = roll_dice()
    print('you rolled a', roll_result)
    play_again = input('would you like to play again (y/n)')
    if play_again.lower() != "y":
        break

print('thanks for playing!!!!')