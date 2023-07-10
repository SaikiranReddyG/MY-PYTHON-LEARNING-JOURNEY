import datetime
current_year = datetime.date.today().year

birth_year = int(input('what year were you born????'))
age = current_year - birth_year

print('your age is:', age, 'years old!!')


#another form
current_date = datetime.date.today()
try:
    birthdate_str = input('enter your birth date')
    birthdate = datetime.datetime.strptime(birthdate_str, "%y-%m-%d").date()
    if birthdate > current_date:
        print("invalid input wrong date")

    else:
        age = current_date.year - birthdate.year
        print('your age is : ', age)

except ValueError:
    print('invalid input wrong syntax')


