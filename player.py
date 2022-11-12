import turtle

turtle.register_shape(r"spaceship.gif")

class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape(r"spaceship.gif")
        self.penup()
        self.goto(0,-220)
    
    def toleft(self):
        if(self.xcor()>=-180):
            self.goto(self.xcor()-20,self.ycor())

    def toright(self):
        if(self.xcor()<=180):
            self.goto(self.xcor()+20,self.ycor())
