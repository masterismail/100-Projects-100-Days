from turtle import *
from random import *

max = Turtle()
max.speed(0)
for i in range(0,360,5):
 max.pencolor("pink")
 max.circle(radius=120)
 max.penup()
 max.pencolor("blue")
 max.seth(i)

 max.pendown()

 max.circle(radius=120)

exitonclick()

