from turtle import Turtle

class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(position)
        # 将常用变量设置为属性
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # if self.ycor() > 280 or self.ycor() < -280:
        #     angle = self.heading()
        #     new_angle = 360 - self.heading()
        #     self.setheading(new_angle)
        # 由于球是靠着goto来实现移动的，所以直接改变角度不会对运动方向产生任何影响

        # ！值得学习 没有涉及到角度，只是改变了y—move数值
        self.y_move *= -1


    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
        # self.speed += 1
        # self.speed(self.speed) 无法调用，我要问问怎么回事

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write('GAME OVER', False, align=ALIGNMENT, font=FONT)

    def reset_position(self):
        self.goto(0,0)
        # when the ball gets missed, it will start off in the center and goes off in the opposite direction
        self.move_speed = 0.1
        self.bounce_x()
