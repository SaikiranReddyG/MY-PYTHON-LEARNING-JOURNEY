"""Birthday paradox by G saikiran reddy
exploring the surprising probabilities of the birthday paradox"""

import datetime
import random


def getbirthdays(numberofbirthdays):
    """returns a list of random date objects for birthdays"""
    birthdays = []
    for k in range(numberofbirthdays):
        """the year is unimportant for our simulation as long as birthdays have the same year"""
        startofyear = datetime.date(2001, 1, 1)

        #        #get a random day into the year
        random_number_Of_days = datetime.timedelta(random.randint(0, 364))
        birthday = startofyear + random_number_Of_days
        birthdays.append(birthday)

    return birthdays


def getmatch(birthdays):
    """return the date object of the birthday that occurs more than once
    in the birthdays list"""
    if len(birthdays) == len(set(birthdays)):
        return None  # all birthdays are unique so return none

    #    #compare each birthday to every other birthday
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA  # return the matching birthday


# display the intro:


print("""birthday paradox by G saikiran reddy
thr birthday paradox shows us that in a group of N people, the odds 
that two of them have matching birthdays si suprisingly large.
this program does a monte carlo simulation(that is, repeated random simulations)
to explore this concept.
(it is not actually a paradox but just a surprising result)""")

# set up a tuple of month names in order
MONTHS = ('jan', 'feb', 'mar', 'apr', 'may', 'jun',
          'jul', 'aug', ';sep', 'oct', 'nuv', 'dec')

while True:  # (keep asking until the user enters a valid amount)
    print('how many birthdays shall i generate? (max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBdays = int(response)
        break  # user has entered a valid amount

print()

# generate and d
# isplay the birthdays
print('here are', numBdays, 'birthdays:')
birthdays = getbirthdays(numBdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # dispaly a comma for each birthday after the first birthday.
        print(',', end='')
        monthname = MONTHS[birthday.month - 1]
        datetext = "{} {}".format(monthname, birthday.day)
        print(datetext, end='')

print()
print()

# determine if there are two birthdays that match
match = getmatch(birthdays)

# display the results:
print('in this simulation, ', end='')
if match is not None:
    monthname = MONTHS[match.month - 1]
    datetext = "{} {}".format(monthname, match.day)
    print('multiple have birthday on', datetext)

else:
    print('there are no matching birthdays!!!!')
print()

# run through 100000 simulations:
print('generating...', numBdays, 'random birthdays 100000 times....')
input("press enter to begin.....")

print('lets run another 100000 simulations...')
simMatch = 0  # how many simulations have matching birthdays in them
for i in range(100_000):

    # report on the progress on every 100000 simulations
    if i % 10_000 == 0:
        print(i, 'simulations run....')
    birthdays = getbirthdays(numBdays)
    if getmatch(birthdays) is not None:
        simMatch = simMatch + 1

print('100,000 simulations run.')

# display simulations result:

probability = round(simMatch / 100_000 * 100, 2)
print('Out of 100000 simulations of', numBdays, 'people there was a')
print('matching birthdays in that group', simMatch, 'times, this means')
print('that', numBdays, 'people have a ', probability, '%chance of')
print('having a matching birthday in their group')
print('that\'s probably more than you think!!!!!')
