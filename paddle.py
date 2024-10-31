from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,p):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.penup()
        self.goto(p)
    # def one(self):
    #     if self.a.heading()!=90:
    #         self.a.setheading(90)
    #     self.a.forward(10)
    # def onedown(self):
    #     if self.heading()!=270:
    #         self.a.setheading(270)
    #     self.a.forward(10)
    # def two(self):
    #     if self.b.heading()!=90:
    #         self.b.setheading(90)
    #     self.b.forward(10)
    # def twodown(self):
    #     if self.b.heading()!=270:
    #         # pass
    #         self.b.setheading(270)
    #     self.b.forward(10)
    def up(self):
        n_y=self.ycor()+20
        self.goto(self.xcor(),n_y)
    def down(self):
        n_y=self.ycor()-20
        self.goto(self.xcor(),n_y)