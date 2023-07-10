"""create a simple game where the user has to guess a randomly generated number
after each guess the programm tells the the user if the number is too high or low or close
the user has limited no of guesses"""
import random
#generate a random nuber bw 1 to 100
number = random.randint(1, 100)

#set the num of gusses allowed
max_gusses = 5
num_gusses = 0

#loop until the user runs out of gusses or guess the num correct

while num_gusses < max_gusses:
    # get the users guess
    guess = int(input('guess the generated number bw 1 to 100!!!'))

    if guess == number:
        print('congrats......you have gussed it correct!!!')
        break
    #check if the guess is too high or loww
    elif guess > number:
        print('sorry....your guess is too high!!! TRY AGAIN')

    else:
        print('sorry.......your guess is too loww!!!!TRY AGAIN')

    num_gusses += 1


# if the user runs out of gusses
if num_gusses == max_gusses:
    print('sorry.....you have ran out of choices!!!!!')
    print('the random nuber is:', number)


#practiced
import random
"""select a random number bw 1 to 100"""
magic_number = random.randint(1, 100)
"""specify the max gusses and no of gusses"""
max_gusses = 5
num_gusses = 0


while num_gusses < max_gusses:
    """guess the number"""
    guess = int(input('enter your guess for the random number!!!!'))
    if guess == magic_number:
        print('hurrah!!!!!....you have gussed the number')
        break

    elif guess > magic_number:
        print('SORRYY...your guess is too high try a lower number')

    else:
        print('SORRY!....your number is tooo low guess a higher number')

    """increment the guess num counter"""
    num_gusses += 1

if num_gusses == max_gusses:
    print('you have ran out of your choicess....')
    print('anyway THANK U FOR PLAYING THE GAME... ')
    print('incase you are wondering....the random number is.....', magic_number)