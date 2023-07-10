print('multipluication tables by saikiran reddy G')
# print the horizontal number lables
print('  |  0  1  2  3  4  5  6  7  8  9  10  11  12')
print('--+------------------------------------------')

# display each ro of products

for number1 in range(0, 13):
    # print the vertcal numbers label
    print(str(number1).rjust(2), end='')

    # print a saperating bar
    print('|', end='')

    for number2 in range(0, 13):
        # print the product followed by a space:
        print(str(number1 * number2).rjust(3), end='')

    print()
    # finish the row by printing a new line

