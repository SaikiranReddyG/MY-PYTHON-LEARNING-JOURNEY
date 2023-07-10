import random
n = 20
guessme = int(n * random.random()) + 1
guess = 0
while guess != guessme :
    guess = int(input('newnumber:'))
    if guess > 0 :
        print('give big')
    elif guess < 0 :
        print('small')
    else :
        print('sorry')
        break
else :
      print('sucess')