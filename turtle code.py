score=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
global attempts
attempts = 0
from random import randint
from time import sleep



def grid(): #draws playing grid
    hideturtle()
    speed(0)
    pensize(0)
    penup()
    setpos(-200, -67)
    pendown()
    fd(400)
    penup()
    setpos(-200, 66)
    pendown()
    fd(400)
    penup()
    seth(90)
    setpos(-67, -200)
    pendown()
    fd(400)
    penup()
    setpos(66, -200)
    pendown()
    fd(400)

from turtle import *
grid()
