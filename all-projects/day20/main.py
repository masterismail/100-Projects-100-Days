from turtle import *
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600,height=600)
screen.title("snake game")

starting_position = ((-40,20),(-20,20),(0,20))
segments = []
for position in starting_position:
  segment = Turtle('square')
  segment.color('white')
  segment.penup()
  segment.goto(position)
  segments.append(segment)

game = True
while game:
 for segment in segments:
  segment.forward(20)
  onclick('')

exitonclick()