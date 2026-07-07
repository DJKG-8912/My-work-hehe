from turtle import *
import time
s = Screen()
s.title("Turtle Drawing")
t = Turtle()
mouse_down = False

def base():
    t.shape('circle')
    s.bgcolor('black')
    t.color('red')
    t.speed(0)
    global brush_size
    brush_size = 1
    t.pensize(brush_size)
    t.turtlesize(brush_size / 20)
    instr = Turtle()
    instr.speed(0)
    instr.hideturtle()
    instr.color("white")
    instr.penup()
    instr.goto(-600, 290)
    instr.write("Instructions:", align="left", font=("Arial", 24, "bold"))
    instr.goto(-600, 250)
    instr.write("Arrow Keys = Move", align="left", font=("Arial", 16, "normal"))
    instr.goto(-600, 220)
    instr.write("Q = Move Mode | E = Draw Mode", align="left", font=("Arial", 16, "normal"))
    instr.goto(-600, 190)
    instr.write("[ ] = Hide/Show Turtle", align="left", font=("Arial", 16, "normal"))
    instr.goto(-600, 160)
    instr.write("1 = Clear Screen", align="left", font=("Arial", 16, "normal"))
    instr.goto(-600, 130)
    instr.write("Colors: R G B Y O P W", align="left", font=("Arial", 16, "normal"))
    instr.goto(-600, 100)
    instr.write("Ctrl = Eraser", align="left", font=("Arial", 16, "normal"))
    instr.goto(-600, 70)
    instr.write("Click/Drag = Teleport", align="left", font=("Arial", 16, "normal"))
    instr.goto(-600, 40)
    instr.write("Minus = Decrease Size | Plus = Increase Size", align="left", font=("Arial", 16, "normal"))
    instr.goto(-600, 10)
    instr.write("Also feel free to erase me :)", align="left", font=("Arial", 16, "normal"))
    instr.hideturtle()
    del instr
base()



def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def move_left():
    t.left(15)

def move_right():
    t.right(15)

def size_increase():
    global brush_size
    brush_size += 1
    t.pensize(brush_size)
    t.turtlesize(brush_size / 20)

def size_decrease():
    global brush_size
    if brush_size > 1:
        brush_size -= 1
        t.turtlesize(brush_size / 20)
    t.pensize(brush_size)

def eraser():
    t.color('black', 'white')
    global brush_size
    brush_size = 20
    t.pensize(brush_size)
    t.turtlesize(brush_size / 20)
    t.shape('square')

def blue():
    t.color('blue')
    t.shape('circle')

def red():
     t.color('red')
     t.shape('circle')

def green():
     t.color('green')
     t.shape('circle')

def white():
     t.color("white")
     t.shape('circle')

def yellow():
    t.color('yellow')
    t.shape('circle')

def orange():
    t.color('orange')
    t.shape('circle')

def pink():
    t.color('pink')
    t.shape('circle')

def clear_screen():
    s.reset()
    time.sleep(0.1)
    base()

def penoff():
    t.penup()

def hidepen():
    t.hideturtle()

def showpen():
    t.showturtle()

def penon():
    t.pendown()

def teleport_turtle(x, y):
    t.goto(x, y)

def drag(x, y):
    t.goto(x, y)

t.ondrag(drag)
s.onscreenclick(teleport_turtle)
s.onkey(move_forward, "Up")
s.onkey(move_backward, "Down")
s.onkey(move_left, "Left")
s.onkey(move_right, "Right")
s.onkey(size_decrease, "-")
s.onkey(size_increase, "=")
s.onkey(clear_screen, '1')
s.onkey(penoff, 'q')
s.onkey(penon, 'e')
s.onkey(showpen, ']')
s.onkey(hidepen, '[')
s.onkey(pink, 'p')
s.onkey(orange, 'o')
s.onkey(blue, 'b')
s.onkey(red, 'r')
s.onkey(green, 'g')
s.onkey(white, 'w')
s.onkey(yellow, 'y')
s.onkey(eraser, 'Control_L ')
s.onkey(red, 'Control_R ')

s.listen()

s.mainloop()

