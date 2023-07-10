#"Invent Your Own Computer Games with Python"

"""a deductive logic game where you must guess
 a three digit secret number based on clues"""

import random
num_digits = 3
max_gusses = 15

def main():
    print("""Bagels, a deductive logic game. By G SAIKIRAN REDDY
I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
 When I say:         That means:
 Pico                 One digit is correct but in the wrong position.
 Fermi                One digit is correct and in the right position.
 Bagels               No digit is correct.

 For example, if the secret number was 248 and your guess was 843, the
 clues would be Fermi Pico.""".format(num_digits))
    while True: #main game loop.
        #this stores the secret number the player need to guess
        SecretNum = getSecretNum()
        print('i have thought of a number!!')
        print('you have {} gusses to get it.'.format(max_gusses))

        numGusses = 1
        while numGusses <= max_gusses:
            guess = ""
            #keep looping until a valid guess
            while len(guess) != num_digits or not  guess.isdecimal():
                print('guess #{}:'.format(numGusses))
                guess = input(">")

            clues = getClues(guess, SecretNum)
            print(clues)
            numGusses += 1

            if guess == SecretNum:
                break #it is correct, so break out of this loop

            if numGusses > max_gusses:
                print('you have ran out of gusses')
                print('the answer was {}'.format(SecretNum))

        #ask player if they want to play again
        print('do you want to play again? (y/n)')
        if not input('>').lower().startswith('y'):
            break

    print('thanks for playing!!!')


def getSecretNum():
    """returns a string of digits up of num_digits unique random digits"""

    numbers = list('0123456789')  #create a list of digits 0 to 9
    random.shuffle(numbers)    #shuffle them into a random order

    #get the first num_digits into the list for the secret numbers
    secretNum = ''
    for i in range(num_digits):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """returns a string with the pico, fermi, bagels clues
     for the guess and a secret number pair"""
    if guess == secretNum:
        return "you got it!!!!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            #A correct digit is in the correct place
            clues.append('fermi')

        elif guess[i] in secretNum:
            """a correct digit is in the incorrect num"""
            clues.append('pico')

    if len(clues) == 0:
        return 'bagels'  #there are no correct digits at all

    else:
        #sort the clues into alphabetical order so their
        # original doesnt give information away
        clues.sort()
        #make a single string from the list of string clues

        return " ".join(clues)

#if the programm is run (insted of imported), run the game:

if __name__ == '__main__':
    main()



#practiced:
import random
numdigits = int(input('enter no of digits you need '))
maxgusses =  int(input('enter no of gusses'))

def main():
    while True:
        secretnum = getsecretnum()
        print('i have gussed a number!!!')
        print('you have {} gusses left to find out that num!!!'.format(maxgusses))

        numgusses = 1
        while numgusses <= maxgusses:
            guess = ''
            while len(guess) != numdigits or not guess.isdecimal():
                print('guess #{}'.format(numgusses))
                guess = input('> ')

            clues = getclues(guess, secretnum)
            print(clues)
            numgusses += 1

            if guess == secretnum:
                break

            if numgusses > maxgusses:
                print('you ran out of gusses')
                print('the secret number is {}'.format(secretnum))

        print('do you want to play again!! (y/n)')
        if not  input('> ').lower().startswith('y'):
            break

    print('thank you for playing!!!')

def getsecretnum():
    numbers = list('1234567890')
    random.shuffle(numbers)
    secretnumber = ""
    for i in range(numdigits):
        secretnumber += str(numbers[i])

    return secretnumber

def getclues(guess, secretnumber):

    if guess == secretnumber:
        print("you have got it, the number was: {}".format(secretnumber))

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretnumber[i]:
            clues.append('fermi')

        elif guess[i] in secretnumber[i]:
            clues.append('pico')

    if len(clues) == 0:
        return 'bagels'

    else:
        clues.sort()

        return ''.join(clues)

if __name__ == '__main__':
    main()


