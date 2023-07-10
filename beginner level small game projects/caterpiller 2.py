import random
import turtle as t

t.bgcolor('yellow')  # this adds a yellow background

caterpillar = t.Turtle()  # create a new-turtle for the caterpillar
caterpillar.shape('square')
caterpillar.color('red')
caterpillar.speed(0)  # we don't want the turtle to move before the game starts

"""penup()  allow you to move the turtle around the screen 
without drawing the line along the way"""
caterpillar.penup()
caterpillar.hideturtle()  # hide the turtle

caterpillar2 = t.Turtle()  # create a new-turtle for the caterpillar
caterpillar2.shape('square')
caterpillar2.color('blue')
caterpillar2.speed(0)
caterpillar2.penup()
caterpillar2.hideturtle()

leaf = t.Turtle()  # draw the leaves

"""co ordinates for the leaf shape"""
laf_shape = ((0, 0), (14, 2), (18, 6), (20, 20), (6, 18), (2, 14))
t.register_shape('leaf', laf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed(0)

game_started = False  # you need to know if the game has started
text_turtle = t.Turtle()
text_turtle.write('press space to START', align='center', font=('Arial', 16, 'bold'))
text_turtle.hideturtle()  # hide the turtle but  not the text

score_turtle = t.Turtle()  # add a turtle to write the score
score_turtle.hideturtle()
score_turtle.speed(0)  # to keep the scorecard constant and update it

""" to get a basic version of the program running sooner you can use place holders
 for functions that you will coding later """


def outside_window(caterpillar):
    left_wall = -t.window_width() / 2
    right_wall = t.window_width() / 2
    top_wall = -t.window_height() / 2
    bottom_wall = t.window_height() / 2

    (x, y) = caterpillar.pos()
    outside = \
        x < left_wall or \
        x < right_wall or \
        x < bottom_wall or \
        x < top_wall
    """ any of the four above conditions is true the  outside is true"""
    return outside


def game_over():
    caterpillar.color('yellow')
    caterpillar2.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER!!!', align='center', font=('Arial', 30, 'normal'))


def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()

    x = (t.window_width() / 2) - 50  # 50 pixels from the right
    y = (t.window_height() / 2) - 50  # 50 pixels from the top
    score_turtle.setpos(x, y)
    score_turtle.write(str(current_score), align='right', font=('Arial', 40, 'bold'))


def place_leaf():
    leaf.hideturtle()
    """choose random coordinates to move the leaf"""
    leaf.setx(random.randint(-200, 200))
    leaf.sety(random.randint(-200, 200))
    leaf.showturtle()


def start_game():
    global game_started
    if game_started:
        return
    game_started = True

    score = 0
    text_turtle.clear()  # clear the text from the screen

    caterpillar_speed = 2
    caterpillar_length = 3
    caterpillar.shapesize(1, caterpillar_length, 1)
    caterpillar2.shapesize(1, caterpillar_length, 1)# stretch the turtle into a caterpillar shape
    caterpillar2.showturtle()
    caterpillar2.setheading(180)
    display_score(score)
    place_leaf()  # place the first leaf on the screen

    while True:
        caterpillar.forward(caterpillar_speed)
        caterpillar2.forward(caterpillar_speed)
        if caterpillar.distance(leaf) < 20:  # caterpillar eats the leaf if it is less than 20 pixels away
            place_leaf()  # current leaf has been eaten so add a new leaf

            """make the caterpillar grow longer"""
            caterpillar_length = caterpillar_length + 1
            caterpillar.shapesize(1, caterpillar_length, 1)
            caterpillar2.shapesize(1, caterpillar_length, 1)
            caterpillar_speed = caterpillar_speed + 1
            score = score + 10
            display_score(score)

        #if outside_window(caterpillar) or outside_window(caterpillar2):
            #game_over()


def move_up():
    """check if caterpillar heading left or right"""
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(90)


def move_down():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(270)  # 270 heading send the caterpillar down the screen


def move_left():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(180)


def move_right():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(0)


def caterpillar2_move_up():
    """check if caterpillar heading left or right"""
    if caterpillar2.heading() == 0 or caterpillar2.heading() == 180:
        caterpillar2.setheading(90)


def caterpillar2_move_down():
    if caterpillar2.heading() == 0 or caterpillar2.heading() == 180:
        caterpillar2.setheading(270)  # 270 heading send the caterpillar down the screen


def caterpillar2_move_left():
    if caterpillar2.heading() == 90 or caterpillar2.heading() == 270:
        caterpillar2.setheading(180)


def caterpillar2_move_right():
    if caterpillar2.heading() == 90 or caterpillar2.heading() == 270:
        caterpillar2.setheading(0)


t.onkey(start_game, 'space')  # start the game when space bar is pressed
t.onkey(move_up, "Up")
t.onkey(move_right, "Right")
t.onkey(move_down, 'Down')
t.onkey(move_left, "Left")
t.onkey(move_up, "w")
t.onkey(move_right, "d")
t.onkey(move_down, 's')
t.onkey(move_left, "a")
t.listen()  # allow the program to receive signals from the keyboard
t.mainloop()