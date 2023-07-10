def sequential_search(lst, value):
    for i in range(len(lst)):
        if lst[i] == value:
            return i

    return -1


lst = list(input('enter the list here:'))

value = input('enter the value needed to be found here')
position = sequential_search(lst, value)

if position != -1:
    print('the value {} was found at the position {}'.format(value, position))

else:
    print("the value {value} was not found in the list {lst}")


