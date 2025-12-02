from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake game')
# 关闭动画效果，需要及时刷新屏幕，否则屏幕一片漆黑，什么都没有
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right ')

game_is_on = True
while game_is_on:
    # 当 segment移动的时候，屏幕就会刷新。
    #  放在循环之外，则在蛇身整体向前移动之后，屏幕才会刷新。（所以不会出现蛇身分离移动的情况）
    screen.update()
    # 在每个segment移动之后添加n秒的延迟
    time.sleep(0.1)
    snake.move()

    # detect the collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # detect collisions with tail: if head collides with any segment in the tail, trigger game_over
    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            game_is_on = False
            scoreboard.game_over()

# 利用元组自定义，使用方法类似列表。但元组是不可变的，意味着你不能修改它的元素。
screen.exitonclick()