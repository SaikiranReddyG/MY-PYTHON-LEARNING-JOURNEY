import random
import string
"""define the function"""
def generate_password(length):
    """define the charecters to use"""
    chars = string.ascii_letters + string.digits + string.punctuation
    """generate the password using defines charecters"""
    for i in range(0, length):
        password = ''.join(random.choices(chars))

        return password

while True:
  try:
      length = int(input('enter the password length you need!!! '))
      break

  except ValueError:
      print('enter the valid input')
      exit()


password = generate_password(length)
print('your password is>>>', password)
