import random
from turtle import Turtle, Screen
import turtle

timmy_turtle = Turtle()
timmy_turtle.shape("turtle")
# timmy_turtle.color("coral")
turtle.colormode(255)

# use forloop to simplify codes
# for i in range(4):
#     timmy_turtle.forward(50)
#     timmy_turtle.right(90)

# for i in range(50):
#     timmy_turtle.pendown()
#     timmy_turtle.forward(3)
#     timmy_turtle.penup()
#     timmy_turtle.forward(3)

# game_on = True
# i = 3
#
# while game_on:
#     i += 1
#     current_x = timmy_turtle.xcor()
#     current_y = timmy_turtle.ycor()
#     if abs(current_x) < 0.1 and abs(current_y) < 0.1:
#         for num in range(i):
#             timmy_turtle.forward(50)
#             timmy_turtle.right(360 / i)

# colours = ["spring green", 'lemon chiffon', 'dark orange', 'chocolate', 'rosy brown']

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

for i in range(0, 100):
    timmy_turtle.color(random_color())
    timmy_turtle.circle(100)
    # timmy_turtle.right(3.6)
    timmy_turtle.setheading(timmy_turtle.heading() + 10)


# def draw_shape(num_sides):
#   angle = 360 / num_sides
#   for _ in range(num_sides):
#       timmy_turtle.forward(100)
#       timmy_turtle.right(angle)
#
# #def function is convenient
#
# for shape_side_n in range(3,11):
#       timmy_turtle.color(random.choice(colours))
#       draw_shape(shape_side_n)
# angle = [ 0, 90, 180, 270]
# timmy_turtle.speed(0)
# timmy_turtle.width(9)
#
# game_on = True
# while game_on:
#     timmy_turtle.setheading(random.choice(angle))
#     timmy_turtle.pencolor(random.choice(colours))
#     timmy_turtle.forward(9)

screen = Screen()
screen.exitonclick()