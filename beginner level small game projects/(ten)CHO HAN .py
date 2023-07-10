"""Cho-Han, by Al Sweigart al@inventwithpython.com
 2. The traditional Japanese dice game of even-odd.
 3. View this code at https://nostarch.com/big-book-small-python-projects
 4. Tags: short, beginner, game"""

import random
import sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print("""CHO-HAN, by saikiranreddy.g  
in this traditional japanese dice game, two dices are rolled in a bamboo
cup by the dealer  sitting on the floor, the player must guess 
if the dice total is even(cho), or odd(han)""")

purse = 5000

while True:
    print('you have :', purse, 'how much would you like to bet???? or QUIT')
    while True:
        pott = input('> ')
        if pott.upper() == 'QUIT':
            print('thanks for playing!!!')
            sys.exit()

        elif not pott.isdecimal():
            print('enter a number')

        elif int(pott) > purse:
            print('you do not have enough to make the bet')



        else:
            pott = int(pott)
            break

        #roll the dice

        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print('the dealer swirls the cup and you hear the rattle of the cup')
        print('the dealer slams the cup on the floor, still covering')
        print('dice and asks for your bet')
        print()
        print('     CHO(even)  or HAN(odd)???')

        # leet the player bet cho or han
        while True:
            bet = input('> ').upper()
            if bet != 'CHO' and bet != 'HAN':
                print('please enter cho or han')
                continue

            else:
                break

        # reveal the dice results
        print('the dealer lifts the cup to reveal!!')
        print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
        print(('  ', dice1, '-', dice2))

        # determine if the player has won
        rolliseven = (dice1 + dice2) % 2 == 0
        if rolliseven:
            correctbet = 'CHO'

        else:
            correctbet = 'HAN'

        playerwon = bet == correctbet

        # display the bet results
        if playerwon:
            print('you won!!! you take', pott, 'money')
            purse += (pott)  # add the pot from players purse
            print('the house collects a :', int(pott) // 10, 'as fee')

            purse = purse - int(pott) // 10  # the house fee is 10%

        else:
            purse = purse - int(pott)  # Subtract the pot from player's purse.
        print('you have lost')

        # check if the player has run out of money
        if purse == 0:
            print("you have ran out of money!!!")
            print('thanks for playing!!!!')
            sys.exit()
