score=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
global attempts
attempts = 0
from random import randint
from time import sleep
    

def grid(length): #draws playing grid
    hideturtle()
    speed(0)
    pensize(0)
    penup()
    setpos(-length/2, -length/2)
    pendown()
    fd(length)
    penup()
    setpos(-length/2, -length/4)
    pendown()
    fd(length)
    penup()
    setpos(-length/2, 0)
    pendown()
    fd(length)
    penup()
    setpos(-length/2, length/4)
    pendown()
    fd(length)
    penup()
    setpos(-length/2, length/2)
    pendown()
    fd(length)
    penup()

    seth(90)

    setpos(-length/2, -length/2)
    pendown()
    fd(length)
    penup()
    setpos(-length/4, -length/2)
    pendown()
    fd(length)
    penup()
    setpos(0, -length/2)
    pendown()
    fd(length)
    penup()
    setpos(length/4, -length/2)
    pendown()
    fd(length)
    penup()
    setpos(length/2, -length/2)
    pendown()
    fd(length)

from turtle import *
grid(600)
input()
