from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def forward():
    tim.forward(10)

def backward():
    tim.backward(10)

def counter_clockwise():
    tim.left(10)

def clockwise():
    tim.right(10)

def clear():
    tim.clear()

    # 补充答案：
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(forward,'w')
screen.onkey(backward, 's')
screen.onkey(counter_clockwise, 'a')
screen.onkey(clockwise, 'd')
screen.onkey(clear, 'c')


screen.exitonclick()