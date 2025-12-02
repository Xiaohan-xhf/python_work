from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        # 注意设置color的顺序!
        self.color('white')
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    # problem: 不显示文字，只有海龟的初始形状! 注意代码顺序，要在设置颜色之前write
    def update_scoreboard(self):
        self.write(f"Score = {self.score} ", False, align= ALIGNMENT, font= FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
