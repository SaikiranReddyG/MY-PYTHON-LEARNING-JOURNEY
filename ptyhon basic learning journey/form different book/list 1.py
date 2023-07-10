my_colours = {'red', 'orange', 'yellow', 'blue' }
notmy_colours = {'black', 'yellow', 'white', 'orange'}
all_colours = my_colours | notmy_colours
some_colours = my_colours & notmy_colours
print(all_colours)
print(some_colours)