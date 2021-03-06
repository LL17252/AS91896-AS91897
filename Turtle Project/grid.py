from turtle import *
g = Turtle() #make turtle for grid

screen = Screen()
screen.setup(600,600)

def grid(length): #draws playing grid
    screen.tracer(0)
    g.hideturtle()
    g.speed(0)
    g.pensize(0)
    g.penup()
    g.setpos(-length/2, -length/2)
    g.pendown()
    g.fd(length)
    g.penup()
    g.setpos(-length/2, -length/4)
    g.pendown()
    g.fd(length)
    g.penup()
    g.setpos(-length/2, 0)
    g.pendown()
    g.fd(length)
    g.penup()
    g.setpos(-length/2, length/4)
    g.pendown()
    g.fd(length)
    g.penup()
    g.setpos(-length/2, length/2)
    g.pendown()
    g.fd(length)
    g.penup()

    g.seth(90)

    g.setpos(-length/2, -length/2)
    g.pendown()
    g.fd(length)
    g.penup()
    g.setpos(-length/4, -length/2)
    g.pendown()
    g.fd(length)
    g.penup()
    g.setpos(0, -length/2)
    g.pendown()
    g.fd(length)
    g.penup()
    g.setpos(length/4, -length/2)
    g.pendown()
    g.fd(length)
    g.penup()
    g.setpos(length/2, -length/2)
    g.pendown()
    g.fd(length)
    g.seth(0)
    g.penup()
    screen.tracer(1)
