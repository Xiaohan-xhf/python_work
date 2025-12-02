from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=500)
user_bet = screen.textinput(title='Make your bet!', prompt='Which turtle will win in the race? Enter a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

y_position = -120
all_turtles = []

# 这里直接用循环创建个体，名字不重要。 学到了：用循环创建有限实例的方法
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y_position)
    y_position += 40
    all_turtles.append(new_turtle)

if user_bet: # if it exists. it means the user entered sth.
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


# jim = Turtle(shape='turtle')
# jen = Turtle(shape='turtle')
# she = Turtle(shape='turtle')
# lee = Turtle(shape='turtle')
# may = Turtle(shape='turtle')
#
# color_number = 0
# y_position = - 120
#
# turtles = [tim, jim, jen, she, lee, may]
#
# for turtle in turtles:
#     turtle.penup()
#     turtle.color(colors[color_number])
#     color_number += 1
#     turtle.goto(-230, y_position)
#     y_position += 40


screen.exitonclick()