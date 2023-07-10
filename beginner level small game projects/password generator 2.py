import random
import string
# define the function to generate


def password_generator(length, lower_case, upper_case, digits, special):
    """define the charecters used"""
    required_length = length
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

#combine the charecters based on the users choice
    choices = ''
    if lower_case:
        choices += lower_case

    elif upper_case:
        choices += upper_case

    elif digits:
        choices += digits

    elif special:
        choices += special

    password = ''.join(random.choices(choices))

    return password

try:
    length = int(input('enter the length of password you need'))
except ValueError:
    print('invalid input enter a valid i/p')
    exit()

lower_case = input('include lower case letters? (y/n): ').lower() == 'y'
upper_case = input('you want to include upper case letters? (y/n): ') == 'y'
digits = input('you want to include digits? (y/n): ') == 'y'
special = input('include special chars? (y/n) : ') == 'y'


password = password_generator(length, lower_case, upper_case, digits, special)
print("your password is:", password)



