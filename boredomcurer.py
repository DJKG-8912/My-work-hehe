from turtle import *
import random

title('cooly cool spirals')
shape('turtle')
bgcolor('black')
pensize(1)
speed(0)

def check_boundaries():
    width = window_width()
    height = window_height()

    max_x = width / 2
    max_y = height / 2

    x = xcor()
    y = ycor()

    return x > max_x or x < -max_x or y > max_y or y < -max_y

for i in range(10000):
    for c in ("red", "orange", "yellow", "green", "blue", "purple", "pink", "white", "cyan"):
        color(c)
        forward(random.randrange(50))
        right(random.randint(1, 360))

        if check_boundaries():
            penup()
            home()
            pendown()

