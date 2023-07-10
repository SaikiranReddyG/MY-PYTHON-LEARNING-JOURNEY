"""GAME BETWEEN USER AND COMPUTER BASED ON THE CLASSIC RULES OF ROCK PAPPER AND SICSOOR"""
import random

#initialze the score
user_score = 0
computer_score = 0

"""get user choice"""
while True:
  user_choice = input('rock, papper, sicssor:')

  """check if the user want to exit"""
  if user_choice == 'exit':
      break

  """generate computer choice"""

  computer_choice = random.choice(['rock', 'papper', 'sicssor'])

  """determine thee winner"""

  if user_choice ==  computer_choice:
    print('it is a TIE!!...try again')
    user_score += 1
    computer_score += 1

  elif user_choice == 'rock' and computer_choice == 'sicssor':
    print('you have won this round')
    user_score += 1

  elif user_choice == 'papper' and computer_choice == 'rock':
    print('you have won this round')
    user_score += 1

  elif user_choice == 'sicssor' and computer_choice == 'papper':
    print('you have won this round')
    user_score += 1

  else:
    print('SORRYY!!!....computer have won this round')
    computer_score += 1

  """finalize the score"""
  print("the  scores are:  user_score{}  and computer_score{}".format(user_score, computer_score))

print("the total scores are: user_score{}  and computer_score{}".format(user_score, computer_score))


#practiced:
import random
user_count = 0
computer_count = 0

while True:
    user_choice = input('rock, papper, sicssor:')
    if user_choice == 'exit':
        break
    computer_choice = random.choice(['rock', 'papper', 'sicssor'])

    if user_choice == computer_choice:
        print('it is a TIE')
        user_count += 1
        computer_count += 1

    elif user_choice == 'rock' and computer_choice == 'sicssor':
        print('you have won')
        user_count += 1

    elif user_choice == 'papper' and computer_choice == 'rock':
        print('you have won')
        user_count += 1

    elif user_choice == 'sicssor' and computer_choice == 'papper':
        print('you have won')
        user_count += 1

    else:
        print('the computer have won this round...better luck next time')
        computer_count += 1

    print('the score after this round is: your score {} and computer score {}'.format(user_count, computer_count))

print('the comlete score is your score {} computer score {}'.format(user_count, computer_count))