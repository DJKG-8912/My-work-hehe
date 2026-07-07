from turtle import *
number = int(input('Pick a number from 1-10'))
number1 = int(input("Pick a number from 1-5"))
number2 = int(input('How magnified do you want it to be'))
name = input('What do you want the name to be')

def check_boundaries():
    width = window_width()
    height = window_height()

    max_x = width / 2
    max_y = height / 2

    x = xcor()
    y = ycor()

    return x > max_x or x < -max_x or y > max_y or y < -max_y

for steps in range(1, 100000, number):
    for c in ('white', 'white'):
        title(name)
        bgcolor('black')
        pensize(1)
        speed(100)
        forward(steps/number2)
        color(c)
        right(steps ** number1)
        if check_boundaries():
            penup()
            home()
            pendown()
