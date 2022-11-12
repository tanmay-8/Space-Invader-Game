import turtle
turtle.register_shape(r"bullet.gif")

class Bullet(turtle.Turtle):
    def __init__(self,xcor):
        super().__init__()
        self.shape(r"bullet.gif")
        self.penup()
        self.goto(xcor,-220)

    def destroy(self):
        self.goto(900,900)

    def move(self):
        self.goto(self.xcor(),self.ycor()+2)

        