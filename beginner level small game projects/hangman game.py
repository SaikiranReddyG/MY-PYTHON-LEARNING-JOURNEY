import random
"""list of words for the game"""
words = []

"""function to select a random word"""
def get_word():
    word = random.choice(words)
    return  word

"""to create the dispaly for the hidden word"""
def display_word(word, gussed_letters):
    dispaly = ""
    for letter in word:
        if letter in gussed_letters:
            dispaly += letter

        else:
            dispaly += "_"

    return dispaly
"""main functoin for the game"""
def play_game():
    """select a random word from the list"""
    word = get_word()

    """initialize variables"""
    gussed_letters = []
    attempts = 6

    """loop until the player gusses right"""
    while True:
        """display the hidden  word and the reamining attempts"""
        print('word: ' + display_word(word, gussed_letters))
        print('attempts remaining: ' + str(attempts))

        """ask the player to guess the letter"""
        guess = input("write the letter you gussed")

        """check if the guess is valid"""
        if len(guess) != 1 or not guess.isalpha():
            print('invlid input. please enter a single letter!!!!')
            continue

        """add the gussed letter to the list of gussed letters"""
        gussed_letters.append(guess)

        """check if the letter is in the word"""
        if guess in word:
            print("correct!!")

            """check if the player has gussed all the letters"""
            if set(word) == set(gussed_letters):
                print('congratulations you have gussed the word!!!!' + word)
                break

        else:
            print("incorrect!!!!")
            attempts -= 1

            """check if the player has run out of attempts"""
            if attempts == 0:
                print('sorry you have ran out of attempts, the word was    ' + word)
                break

"""call the main function to start the game"""
play_game()