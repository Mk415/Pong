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


