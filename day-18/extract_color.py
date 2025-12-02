# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("Hirst.jpeg", number_of_colors=90)
# for color in colors:
#     # rgb_colors.append(color.rgb)
# #关键一步，创建空列表，color.rgb
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color =(r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

# requirement:
#   1. 10 * 10
#   2. size: 20, space: 50

import random
from turtle import Turtle, Screen
import turtle

t = Turtle()
t.shape("turtle")
turtle.colormode(255)
t.speed("fastest")

color_list =  [(249, 248, 246), (249, 245, 248), (240, 243, 248), (243, 249, 246), (192, 172, 127), (156, 177, 192),
               (190, 163, 176), (155, 183, 174), (215, 204, 128), (167, 206, 188), (206, 182, 193), (191, 164, 51),
               (179, 190, 209), (166, 202, 209), (107, 119, 170), (99, 111, 144), (209, 185, 179), (211, 205, 35),
               (188, 107, 123)]

def movement():
    t.pendown()
    t.dot(20, random.choice(color_list))
    t.penup()
    t.forward(50)

# t.penup()
# t.goto(-200, -200)
# t.pendown()
#
# for i in range(10):
#     for i in range(10):
#         movement()

start_x = -200  # 左上角 x 坐标
start_y = -200   # 左上角 y 坐标
dot_size = 20   # 点的直径
spacing = 50    # 点之间的间隔

# 画 10*10 的点阵
for row in range(10):  # 控制行数
    for col in range(10):  # 控制每行的点数
        t.penup()
        t.goto(start_x + col * spacing, start_y + row * spacing)  # 移动到正确位置
        t.pendown()
        t.dot(dot_size, random.choice(color_list))  # 画点

# how to let turtle to paint a circle python
screen = Screen()
screen.exitonclick()

# the last problems:
# 1. 开始的位置
# 2. 适当换行
# 必要的时候停止