from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x=10
        self.y=10
        self.m=0.1
    def move(self):
        n_x=self.xcor() + self.x
        n_y=self.ycor() + self.y
        self.goto(n_x,n_y)
    def bounce(self):
        self.y *= -1

    def bouncex(self):
        self.x *= -1
        self.m*=0.9

    def reset(self):
        self.goto(0,0)
        self.bouncex()