import cmd
import os
import random
import textwrap
import sys
import time
from turtle import *

#turtle setup
from time import sleep    
g = Turtle() #make turtle for grid
g.hideturtle()
space = Screen()
def grid(length): #draws playing grid

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

grid(600)

gridposx={'1': -300,'2': -150,'3': 0,'4': 150}
gridposy={'a': 150,'b': 0,'c': -150,'d': -300}


ZONEPOS = ""
ZONENAME = ""
DESCRIPTION = "description"
EXAMINATION = "examine"
SOVLED = False
UP = "up", "north"
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

zonemap = {
    'a1':{
        ZONEPOS: 'a1',
        ZONENAME: "lol",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "",
        DOWN: 'b1',
        LEFT: '',
        RIGHT: 'a2'
        },
    'a2':{
        ZONEPOS: 'a2',
        ZONENAME: "XD",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "",
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT: 'a3'
        },
    'a3':{
        ZONEPOS: 'a3',
        ZONENAME: "lol",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "",
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT: 'a4'
        },
    'a4':{
        ZONEPOS: 'a4',
        ZONENAME: "lol",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "",
        DOWN: 'b4',
        LEFT: 'a3',
        RIGHT: ''
        },
    'b1':{
        ZONEPOS: 'b1',
        ZONENAME: "lol",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "a1",
        DOWN: 'c1',
        LEFT: '',
        RIGHT: 'b2'
        },
    'b2':{
        ZONEPOS: 'b2',
        ZONENAME: "lol",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "a2",
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'b3'
        },
    'b3':{
        ZONEPOS: 'b3',
        ZONENAME: "Stream",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "a3",
        DOWN: 'c3',
        LEFT: 'b2',
        RIGHT: 'b4'
        },
    'b4':{
        ZONEPOS: 'b4',
        ZONENAME: "Stream",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "a4",
        DOWN: 'c4',
        LEFT: 'b3',
        RIGHT: ''
        },
    'c1':{
        ZONEPOS: 'c1',
        ZONENAME: "lol",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "b1",
        DOWN: 'd1',
        LEFT: '',
        RIGHT: 'c2'
        },
    'c2':{
        ZONEPOS: 'c2',
        ZONENAME: "lol",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "b2",
        DOWN: 'd2',
        LEFT: 'c1',
        RIGHT: 'c3'
        },
    'c3':{
        ZONEPOS: 'c3',
        ZONENAME: "lol",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "b3",
        DOWN: 'd3',
        LEFT: 'c2',
        RIGHT: 'c4'
        },
    'c4':{
        ZONEPOS: 'c4',
        ZONENAME: "lol",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "b4",
        DOWN: 'd4',
        LEFT: 'c3',
        RIGHT: ''
        },
    'd1':{
        ZONEPOS: 'd1',
        ZONENAME: "Stream",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "c1",
        DOWN: '',
        LEFT: '',
        RIGHT: 'd2'
        },
    'd2':{
        ZONEPOS: 'd2',
        ZONENAME: "Stream",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "c2",
        DOWN: '',
        LEFT: 'd1',
        RIGHT: 'd3'
        },
    'd3':{
        ZONEPOS: 'd3',
        ZONENAME: "Stream",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "c3",
        DOWN: '',
        LEFT: 'd2',
        RIGHT: 'd4'
        },
    'd4':{
        ZONEPOS: 'd4',
        ZONENAME: "lol",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "c4",
        DOWN: '',
        LEFT: 'd3',
        RIGHT: ''
        }}


o= Turtle()
o.speed(-100000000000)
o.hideturtle()
o.pu()


l= Turtle()
l.speed(-100000000000)
o.hideturtle()
o.pu()

def dpl(): #draw player location
    p.pu()
    p.setpos(gridposx[str(myPlayer.location[1])] + 50,gridposy[str(myPlayer.location[0])] + 50)
    p.color('blue', 'purple')
    p.pd()
    p.begin_fill()
    for x in range(36):
        p.fd(100)
        p.lt(170)
    p.end_fill()
    p.pu()
def fancypattern():
  p.pu()
  p.setpos(gridposx[str(myPlayer.location[1])] + 50,gridposy[str(myPlayer.location[0])] + 50)
  p.color('blue', 'purple')
  p.pd()
  p.begin_fill()
  for x in range(36):
    p.fd(10)
    p.lt(170)
  p.end_fill()



def drawstream():
  for t in ("a1", "a2", "a3", "a4", "b1", "b2", "b3", "b4", "c1", "c2", "c3", "c4", "d1", "d2", "d3", "d4"):
    if zonemap[t][ZONENAME] == "Stream":
      wave(gridposx[t[1]], gridposy[t[0]])
    

def wave(posx, posy):
  o.color('blue')
  for l in range(5):
    o.setpos(posx, posy+((80*l)/3)+3)
    o.pd()
    for x in range(10):
      o.fd(4.3)
      o.lt(5)
    for x in range(20):
      o.fd(4.3)
      o.rt(5)
    for x in range(10):
      o.fd(4.3)
      o.lt(5)
    o.pu()

drawstream()
input()

