import turtle
from itertools import cycle


colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])

# set up the turtle
turtle.bgcolor('black')  # background colour
turtle.speed('fast')  # the turtle speed
# turtle.pensize(4)  # thickness of the turtle trail
turtle.pensize(20)

# choose pen colour and draw a circle
turtle.pencolor('red')  # pen color
turtle.circle(30)


def draw_circle(size, angle, shift):
    turtle.bgcolor(next(colors))  # set the bg colurs to the loop
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size + 5, angle + 1, shift + 1)


turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(20)
draw_circle(30, 0, 1)


# experiment with different shapes
"""import turtle
from itertools import cycle


colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])

# set up the turtle
turtle.bgcolor('black')  # background colour
turtle.speed('fast')  # the turtle speed
# turtle.pensize(4)  # thickness of the turtle trail
turtle.pensize(20)

# choose pen colour and draw a circle
turtle.pencolor('red')  # pen color
turtle.circle(30)


def draw_circle(size, angle, shift, shape):
    turtle.bgcolor(next(colors))  # set the bg colurs to the loop
    turtle.pencolor(next(colors))
    next_shape = ''
    if shape == 'circle':
        turtle.circle(size)
        # next_shape == 'square'
    elif shape == 'square':
        for i in range(4):
            turtle.forward(size * 2)
            turtle.left(90)
        # next_shape == 'circle'
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size + 5, angle + 1, shift + 1, next_shape)


turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(20)
draw_circle(30, 0, 1, 'circle')"""