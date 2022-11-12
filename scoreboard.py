from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.highscore = 0
        self.score = 0
        self.penup()
        self.color("black")
        self.hideturtle()
        self.update()


    # for writing score
    def update(self):
        self.highscore = int(open(r"highscore.txt",mode="r").read())
        self.clear()
        self.goto(0,-120)
        self.write(f"HS:{self.highscore}    SCORE:{self.score}",align="center",font=("Courier",25,"bold"))

    # for increase score
    def increase(self):
        self.score += 5
        if(self.score>self.highscore):
            with open(r"highscore.txt",mode="w") as file:
                file.write(str(self.score))
        self.update()

    #Game Over
    # for writing score
    def gameover(self):
        self.goto(0,100)
        self.write(f"Game Over",align="center",font=("Courier",30,"bold"))

    def refreshscoreboard(self):
        self.clear()
        self.score = 0
        self.update()
