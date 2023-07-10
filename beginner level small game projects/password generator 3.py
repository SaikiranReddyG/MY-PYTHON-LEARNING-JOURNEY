import random
import string


def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    password_chars = f"{letters}{digits}{special_chars}"
    password = "".join(random.choice(password_chars) for i in range(length))
    return password

password_length = int(input('enter the length of the password you need'))
n = password_length
passwords = generate_password(n)
print(f"generated password is: {passwords}")
