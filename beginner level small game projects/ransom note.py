"""create a  ransom note"""
def create_ranson_note(message, letters):
    """convert the message and letters to lowercase to ignore case sensitivity"""
    message = message.lower()
    letters = letters.lower()

    """crealte a dictionary to store the count of each letter in the letter string"""
    letter_count = {}
    for letter in letters:
        if letter.isalpha():
            letter_count[letter] = letter_count.get(letter, 0) + 1


    """check if there are enough letters in the ransom note"""
    for letter in message:
        if letter.isalpha():
            if letter not in letter_count or letter_count[letter] == 0:
                return False
            letter_count[letter] -= 1


    return True


message = 'give me all your MONEYYYY!!!!'
letter = 'mneiallvgouwyryoedlsjvnndlsfblmgivemeallyourmoney!11!!!cmum'

if create_ranson_note(message, letter):
    print('ransom note can be created!!!!')

else:
    print('not enough letters to create a ransom note!!!')

