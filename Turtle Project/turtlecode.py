from time import sleep
from turtle import *    

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
    seth(0)
    penup()

grid(600)

gridposx={'a': -300,'b': -150,'c': 0,'d': 150}
gridposy={'1': 150,'2': 0,'3': -150,'4': -300}

def drawsquare():
    pendown()
    for x in range(4):
        fd(50)
        left(90)
    penup()
setpos(gridposx[str(myPlayer.location[0])] + 50,gridposy[str(myPlayer.location[1])] + 50)
drawsquare()
    
input()