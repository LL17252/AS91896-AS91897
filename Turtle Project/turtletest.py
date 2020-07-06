import cmd
import os
import random
import textwrap
import sys
import time
from turtle import *

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
        ZONENAME: "City Area",
        DESCRIPTION: "The upper left most City Area",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "",
        DOWN: 'b1',
        LEFT: '',
        RIGHT: 'a2'
        },

    'a2':{
  
        ZONENAME: "Bush",
        DESCRIPTION: "A place with many trees, almost like a forest",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "",
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT: 'a3'
        },

    'a3':{
        ZONENAME: "Stream",
        DESCRIPTION: "The main Stream connected to the City Area",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "",
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT: 'a4'
        },

    'a4':{
        ZONENAME: "City Area",
        DESCRIPTION: "Your starting point",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "",
        DOWN: 'b4',
        LEFT: 'a3',
        RIGHT: ''
        },

    'b1':{
        ZONENAME: "Bush",
        DESCRIPTION: "Very damp and very dark",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "a1",
        DOWN: 'c1',
        LEFT: '',
        RIGHT: 'b2'
        },

    'b2':{
        ZONENAME: "Stream",
        DESCRIPTION: "The centre of the stream",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "a2",
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'b3'
        },

    'b3':{
        ZONENAME: "Stream",
        DESCRIPTION: "A large area with quick flowing water",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "a3",
        DOWN: 'c3',
        LEFT: 'b2',
        RIGHT: 'b4'
        },

    'b4':{
        ZONENAME: "City Area",
        DESCRIPTION: "A very urban place with lots of cars passing by",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "a4",
        DOWN: 'c4',
        LEFT: 'b3',
        RIGHT: ''
        },

    'c1':{
        ZONENAME: "Stream",
        DESCRIPTION: "An area with eels due to it's slow flowing water",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "b1",
        DOWN: 'd1',
        LEFT: '',
        RIGHT: 'c2'
        },

    'c2':{
        ZONENAME: "Stream",
        DESCRIPTION: "A small area with lots of overflowing water",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "b2",
        DOWN: 'd2',
        LEFT: 'c1',
        RIGHT: 'c3'
        },

    'c3':{
        ZONENAME: "Bush",
        DESCRIPTION: "Much of the area is covered by a layer of water",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "b3",
        DOWN: 'd3',
        LEFT: 'c2',
        RIGHT: 'c4'
        },

    'c4':{
        ZONENAME: "City Area",
        DESCRIPTION: "An area with lots of litter thrown around",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "b4",
        DOWN: 'd4',
        LEFT: 'c3',
        RIGHT: ''
        },

    'd1':{
        ZONENAME: "City Area",
        DESCRIPTION: "Very quiet, not a very active place",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "c1",
        DOWN: '',
        LEFT: '',
        RIGHT: 'd2'
        },

    'd2':{
        ZONENAME: "Bush",
        DESCRIPTION: "An area with damp long grass",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "c2",
        DOWN: '',
        LEFT: 'd1',
        RIGHT: 'd3'
        },

    'd3':{
        ZONENAME: "Bush",
        DESCRIPTION: "Much green",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "c3",
        DOWN: '',
        LEFT: 'd2',
        RIGHT: 'd4'
        },

    'd4':{
        ZONENAME: "City Area",
        DESCRIPTION: "Very city like",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "c4",
        DOWN: '',
        LEFT: 'd3',
        RIGHT: ''
        }}

gridposx={'1': -300,'2': -150,'3': 0,'4': 150}
gridposy={'a': 150,'b': 0,'c': -150,'d': -300}


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
    
o = Turtle()
o.speed(0)
o.hideturtle()
o.pu()

def wave(posx, posy):
  screen.tracer(0)
  o.color('blue')
  for l in range(5):
    o.setpos(posx, posy+((80*l)/3)+3)
    o.pd()
    for x in range(100):
      o.fd(.43)
      o.lt(.5)
    for x in range(200):
      o.fd(.43)
      o.rt(.5)
    for x in range(100):
      o.fd(.43)
      o.lt(.5)
    o.pu()
  screen.tracer(1)
