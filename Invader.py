import random
from time import sleep
import turtle

turtle.register_shape(r"alien.gif")

class Invader(turtle.Turtle):
    def __init__(self,pos,movedown,movehor):
        super().__init__()
        self.shape(r"alien.gif")
        self.penup()
        self.goto(pos[0],pos[1])
        self.speed(1)
        self.moverandom = movehor
        self.movedown = movedown

    def todown(self):
        if(self.ycor()>-230):
            self.goto(self.xcor(),self.ycor()-self.movedown)

    def random(self):
        self.goto(self.xcor()+self.moverandom,self.ycor())


    def bouncex(self):
        self.moverandom *= -1 

    def destroy(self):
        self.goto(900,900)