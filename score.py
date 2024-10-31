from turtle import Turtle
class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()

        self.hideturtle()
        self.l_s=0
        self.r_s=0
        self.update()
    def update(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_s,align="center",font=("Courier",80,"normal"))
        self.goto(100,200)
        self.write(self.r_s,align="center",font=("Courier",80,"normal"))
    def l_p(self):
        self.l_s+=1
        self.update()
    def r_p(self):
        self.r_s+=1
        self.update()