from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score
import random
s=Screen()
s.bgcolor("black")
s.title("pong")
s.setup(width=800,height=600)
s.tracer(0)
score=Score()

# a=Turtle("square")
# a.setheading(-90)
# a.shapesize(1,3)
# a.color("white")
# a.penup()
# a.speed("fastest")
# a.goto(-280,0)
# b=Turtle("square")
# b.setheading(90)
# b.shapesize(1,3)
# b.color("white")
# b.penup()
# b.speed("fastest")
# b.goto(280,0)

# line.color("white")
# cor=[(0),(80),(40),(120),(160),(200),(240),(280),(-40),(-80),(-120),(-160),(-200),(-240),(-280)]
# pad=[]
# for i in range(len(cor)):

#     line=Turtle("square")
#     line.color("white")
#     line.penup()
#     line.shapesize(1,0.5)
#     line.speed('fastest')
#     line.goto(x=0,y=cor[i])
# a_cor=(280,0)
# b_cor=(-280,0)
# a=Paddle(a_cor)
# b=Paddle(b_cor)
# s.listen()
# # def one():
# #     if a.heading()!=90:
# #         a.setheading(90)
# #     a.forward(10)
# # def onedown():
# #     if a.heading()!=270:
# #         a.setheading(270)
# #     a.forward(10)
# # def two():
# #     if b.heading()!=90:
# #         b.setheading(90)
# #     b.forward(10)
# # def twodown():
# #     if b.heading()!=270:
# #         # pass
# #         b.setheading(270)
# #     b.forward(10)
# s.onkey(a.one,"Up")
# s.onkey(a.onedown,"Down")
# s.onkey(b.twodown,"Right")
# s.onkey(b.two,"Left")
# points = Turtle()
# points.color("yellow")
# style = ('Courier', 30, 'italic')
# points.penup()
# points.goto(0, 280)
# # points.write("Points: 0", font=style)
# points.hideturtle()

# ball=Turtle("circle")
# ball.color("white")
# ball.shapesize(0.5,0.5)
# # if ball.xcor() or ball.ycor()==0:
# ball.penup()
# score=0
# xcor=[0,180,140,10,20,30,40,50,300,310,320,330,340,350,360]
# i=1
# ball.setheading(random.choice(xcor))
# while i:
#     ball.forward(10)
#     if ball.distance(a)<5 or ball.distance(b)<5:
#         score+=1
#         points.clear()
#         points.write(f"Score:{score}",align="center",font=("Arial",10,"normal"))
#     # if ball.xcor()<=250 and ball.ycor()<=250:
        
#     #     ball.forward(10)
#     elif ball.xcor()>=290 or ball.ycor()>=290:
#         ball.goto(0,0)
#         ball.setheading(random.choice(xcor))  
#         # i=0
#     # i=0
#     # if ball.xcor()>=-250 and ball.xcor()>=-250:
#     #     ball.forward(10)
#     elif ball.xcor()<=-290 or ball.ycor()<=-290:
#         ball.goto(0,0)
#         ball.setheading(random.choice(xcor))
#             # i=0
# # i=0
    
a_cor=(380,0)
b_cor=(-380,0)
a=Paddle(a_cor)
b=Paddle(b_cor)
ball=Ball()
s.listen()
s.onkey(a.up,"Up")
s.onkey(a.down,"Down")
s.onkey(b.up,"Left")
s.onkey(b.down,"Right")
i=1
while i:
    time.sleep(0.1)
    s.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()
    if ball.distance(a)<50 and ball.xcor()>320 or ball.distance(b)<50 and ball.xcor()<-320:
        ball.bouncex()
        
    if ball.xcor()>280:
        ball.reset()
        score.l_p()
    if ball.xcor()<-280:
        ball.reset() 
        score.r_p()





 


















s.exitonclick()


