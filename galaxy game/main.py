#!/usr/bin/python


#Imports
import turtle
import os
import math
import random


turtle.setundobuffer(1)
turtle.tracer(1)

#Set Up Screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("dfs.png")

#Register Shape
turtle.register_shape("invader.gif")
turtle.register_shape("face2.gif")

#Draw Border
border_pen = turtle.Turtle()
border_pen.speed(0)
#border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(5)
for side in range(4):
  border_pen.fd(600)
  border_pen.lt(90)
border_pen.hideturtle()
