from turtle import Turtle
# 常量放在开头便于修改（要不然还得跑到body里面一个个找）
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        # self.segments 存储蛇的身体，不会因为 move() 运行而消失。

        # __init__() 只会在创建 Snake 对象时运行一次，它的作用是：
        # 创建 self.segments 列表（存储蛇的身体部分）。
        # 调用 self.create_snake() 生成初始的蛇。
        # 如果把 move() 加进去，Snake 一创建就会自动 move() 一次，但之后就不会再动，除非你手动调用 move()，这通常不是我们想要的行为。
        self.segments = []
        self.create_snake()
        # 将常用的head定义为snake的属性
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # 在list中的-1，表示list的最后一位
        # 这里的position（）是turtle里面的方法
        self.add_segment(self.segments[-1].position())


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # 为了实现snake里面的重要游戏规则：不能直接以与现在前进的方向相反的方向前进。
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


