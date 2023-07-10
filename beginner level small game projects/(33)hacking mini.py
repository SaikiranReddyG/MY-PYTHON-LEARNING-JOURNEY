import random
import sys

# set up yhe constants
# the garbage filler characters for the computer memory display
GARBAGE_CHARS = '~!@#$%^&*()_+-={}[]|;:,.<>?/'

# load the words list from the text file that has 7-letter words
with open('sevenletterwords.txt') as wordListFile:
    WORDS = wordListFile.readlines()

for i in range(len(WORDS)):
    # Convert each word to uppercase and remove the trailing new line:
    WORDS[i] = WORDS[i].strip().upper()


def main():

    """run a single game of hacking"""
    print("Hacking Minigame, by G sai kiran reddy Find the password in the computer's memory."
          " You are given clues aftereach guess. For example, if the secret password is MONITOR"
          " but theplayer guessed CONTAIN, they are given the hint that 2 out of 7 letter were correct,"
          " because both MONITOR and CONTAIN have the letter O and Nas their 2nd and 3rd letter."
          " You get four guesses.\n")

    input("Press Enter to begin...")

    game_words = get_words()

    computer_memory = get_computer_memory_string(game_words)
    secret_password = random.choice(game_words)

    print(computer_memory)

    # start at four tries remaining and going down
    for triesRemaining in range(4, 0, -1):
        player_move = ask_for_player_guess(game_words, triesRemaining)
        if player_move == secret_password:
            print('ACCESS GRANTED')
            return

        else:
            num_matches = num_matching_letters(secret_password, player_move)
            print('ACCESS DENIED ({}/7 CORRECT)'.format(num_matches))

        print('out of tries.secret password was {}'.format(secret_password))


def get_words():
    """return a list of 12 words that could possibly be the
    passwordThe secret password will be the first word in the list.
 To make the game fair, we try to ensure that there are words with
a range of matching numbers of letters as the secret word."""
    secret_password = random.choice(WORDS)
    words = [secret_password]

    # find two more words these have zero matching letters
    while len(words) < 3:
        random_word = get_one_word_except(words)
        if num_matching_letters(secret_password, random_word) == 0:
            words.append(random_word)

    # find two words that have 3 matching letters but give up at
    # 500 tries if not enough can be found

    for k in range(500):
        if len(words) == 5:
            break  # found 5 words so break out of loop

        random_word = get_one_word_except(words)
        if num_matching_letters(secret_password, random_word) == 0:
            words.append(random_word)

    # Find at least seven words that have at least one matching letter
    # (but give up at 500 tries if not enough can be found).

    for j in range(500):
        if len(words) == 12:
            break  # found 7 or more words so break out of loop

        random_word = get_one_word_except(words)
        if num_matching_letters(secret_password, random_word) == 0:
            words.append(random_word)

    # add any random words needed to get 12 total words

    while len(words) < 12:
        random_word = get_one_word_except(words)
        words.append(random_word)

    assert len(words) == 12
    return words


def get_one_word_except(blocklist=None):
    """returns a random words in the words that isn't in blocklist"""
    if blocklist is None:
        blocklist = []

    while True:
        randomword = random.choice(WORDS)
        if randomword not in blocklist:
            return randomword


def num_matching_letters(word1, word2):
    """return the number of matching letters in these two words"""
    matches = 0

    for n in range(len(word1)):
        if word1[i] == word2[i]:
            matches += 1

    return matches


def get_computer_memory_string(words):
    """return  a string representing the computer memory"""
    lines_with_words = random.sample(range(16 * 2), len(words))
    memory_address = 16 * random.randint(0, 4000)

    # create the computer memory string
    computer_memory = []  # will contain 16 strings one of each line
    next_word = 0  # the index in words of the word to put into a line
    for lineNum in range(16):
        # create a half line of garbage characters:
        left_half = ''
        right_half = ''
        for j in range(16):
            left_half += random.choice(GARBAGE_CHARS)
            right_half += random.choice(GARBAGE_CHARS)

        # fill in the password from words
        if lineNum in lines_with_words:
            # find a random place in the half line to insert the words
            insertion_index = random.randint(0, 9)
            left_half = (left_half[: insertion_index] + words[next_word]) + left_half[insertion_index + 7:]
            next_word += 1  # update the word to put in the half line

        if lineNum + 16 in lines_with_words:
            # find a random place in the half line to insert the word
            insertion_index = random.randint(0, 9)
            right_half = (right_half[: insertion_index] + words[next_word]) + right_half[insertion_index + 7:]
            next_word += 1

        computer_memory.append('ox' + hex(memory_address)[2:].zfill(4)
                               + "  " + left_half + '   '
                               + "ox" + hex(memory_address + (16 * 16))[2:].zfill(4)
                               + '  ' + right_half)

        memory_address += 16  # jump from say oxe680 to oxe690

        # each string in the computer memory is joined
        # into one large string to return
        return '\n'.join(computer_memory)


def ask_for_player_guess(words, tries):
    """let the player enter a password guess"""
    while True:
        print('enter password: ({} tries remaining)'.format(tries))
        guess = input('> ').upper()
        if guess in words:
            return guess

        print('that is not one of the possible words listed above')
        print('try entering {} or {}'.format(words[0], words[1]))


if __name__ == "__main__":

    try:
       main()
    except KeyboardInterrupt:
        sys.exit()  # when ctrl + c is pressed end the program