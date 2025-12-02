from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
scoreboard = Scoreboard()

screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball((0,0))

screen.listen()
screen.onkey(r_paddle.move_forward, 'Up')
screen.onkey(r_paddle.move_back, 'Down')
screen.onkey(l_paddle.move_forward, 'w')
screen.onkey(l_paddle.move_back, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect the collision with wall, 为什么这里又把if放在ball外面呢
    if ball.ycor() > 280 or ball.ycor() < -275:
        ball.bounce_y()

    # detect the collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x()

    # detect r paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        # 右边失球，左边得分
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()