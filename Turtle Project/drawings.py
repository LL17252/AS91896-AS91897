import cmd
import os
import random
import textwrap
import sys
import time
from turtle import *

screen = Screen()
screen.setup(600, 600)

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

    'd4': {
        ZONENAME: "Shop",
        DESCRIPTION: "Very rich",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "c4",
        DOWN: '',
        LEFT: 'd3',
        RIGHT: ''
        }}


gridposx = {'1': -300, '2': -150, '3': 0, '4': 150}
gridposy = {'a': 150, 'b': 0, 'c': -150, 'd': -300}

grid_list = [
    "a1", "a2", "a3", "a4", "b1", "b2", "b3", "b4", "c1", "c2", "c3", "c4",
    "d1", "d2", "d3", "d4"
]


def drawstream():
  screen.tracer(0)
  for t in grid_list:
    if zonemap[t][ZONENAME] == "Stream":
      wave(gridposx[t[1]], gridposy[t[0]])
  screen.tracer(1)


def drawbush():
  screen.tracer(0)
  for t in grid_list:
    if zonemap[t][ZONENAME] == "Bush":
      bush(gridposx[t[1]], gridposy[t[0]])
  screen.tracer(1)


def drawcity():
  screen.tracer(0)
  for t in grid_list:
    if zonemap[t][ZONENAME] == "City Area":
      city(gridposx[t[1]], gridposy[t[0]])
  screen.tracer(1)

def drawshop():
  screen.tracer(0)
  for t in grid_list:
    if zonemap[t][ZONENAME] == "Shop":
      shop(gridposx[t[1]], gridposy[t[0]])
  screen.tracer(1)

####################################
o = Turtle() #making a new profile for a seperate set of turtle code
o.speed(0)
o.hideturtle()
o.pu()


def wave(posx, posy): #defining the code for drawing the stream
	o.color('blue')
	for l in range(5):
		o.setpos(posx, posy + ((80 * l) / 3) + 3)
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


def bush(posx, posy): #defining the code for drawing the bush
  o.pu()
  o.color('green')
  bushbush(posx + 20, posy + 10) #calling the smaller drawings and combining them for bush squares
  bushbush(posx + 75, posy + 90)
  bushgrass(posx + 110, posy + 10)
  bushgrass(posx + 90, posy + 50)
  bushgrass(posx + 30, posy + 90)

def bushbush(posx , posy): #defining a smaller drawing for the bush squares
  o.setpos(posx, posy)
  o.seth(0)
  o.color('#32FB1A') #changing the turtle colour using hex code
  o.fillcolor('#32FB1A')
  o.begin_fill() #fill code to colour a whole area rather than just lines
  o.pd()
  o.fd(45)
  for x in range(20):
	  o.fd(2.5/2)
	  o.lt(6.5)
  for x in range(9):
	  o.fd(3/2)
	  o.lt(8)
  o.seth(90)
  for x in range(45):
	  o.fd(2.865/2)
	  o.lt(4)
  o.seth(180)
  for x in range(20):
	  o.fd(2.5/2)
	  o.lt(6.5)
  for x in range(9):
	  o.fd(3/2)
	  o.lt(8)
  o.end_fill() #fill code to colour a whole area rather than just lines
  o.pu()
	
def bushgrass(posx , posy): #defining a smaller drawing for the bush squares
  o.setpos(posx , posy)
  o.seth(0)
  o.pd()
  o.seth(90)
  o.fillcolor('green')
  o.begin_fill() #fill code to colour a whole area rather than just lines
  for x in range(10):
    o.fd(3)
    o.lt(3)
  o.pu()
  o.setpos(posx , posy)
  o.seth(90)
  o.pd()
  for x in range(10):
    o.fd(2.5)
    o.lt(6)
  o.pu()
  o.setpos(posx , posy)
  o.seth(90)
  o.pd()
  for x in range(10):
    o.fd(2)
    o.lt(9)
  o.pu()
  o.setpos(posx , posy)
  o.seth(90)
  o.pd()
  for x in range(10):
    o.fd(3)
    o.rt(2)
  o.pu()
  o.setpos(posx , posy)
  o.seth(90)
  o.pd()
  for x in range(10):
    o.fd(2)
    o.rt(8)
  o.end_fill() #fill code to colour a whole area rather than just lines
  o.pu()

def city (posx , posy): #defining the code for drawing the city area
  o.pu()
  o.seth(0)
  o.color('black')
  o.fillcolor('silver')
  o.setpos(posx + 75, posy + 10)
  o.pd()
  o.begin_fill() #fill code to colour a whole area rather than just lines
  o.seth(150)
  o.fd(40)
  o.seth(90)
  o.fd(80)
  o.seth(330)
  o.fd(40)
  o.seth(30)
  o.fd(40)
  o.seth(270)
  o.fd(80)
  o.seth(210)
  o.fd(40)
  o.end_fill() #fill code to colour a whole area rather than just lines
  o.pu()
  o.fillcolor('lightgrey')
  o.begin_fill() #fill code to colour a whole area rather than just lines
  o.setpos(posx + 40,posy + 110)
  o.pd()
  o.seth(30)
  o.fd(40)
  o.seth(330)
  o.fd(40)
  o.seth(210)
  o.fd(40)
  o.seth(150)
  o.fd(40)
  o.end_fill() #fill code to colour a whole area rather than just lines
  o.pu()
  o.setpos(posx + 75, posy + 10)
  o.seth(90)
  o.pd()
  o.fd(80)
  o.pu()
  leftwindow(posx + 60, posy + 70)
  leftwindow(posx + 45, posy + 77.5)
  leftwindow(posx + 60, posy + 50)
  leftwindow(posx + 45, posy + 57.5)
  rightwindow(posx + 80, posy + 65)
  rightwindow(posx + 95, posy + 72.5)
  rightwindow(posx + 80, posy + 45)
  rightwindow(posx + 95, posy + 52.5)

def leftwindow (posx , posy): #defining one of the windows so it is repeatable
  o.setpos(posx, posy)
  o.seth(90)  
  o.pd()
  o.fd(10)
  o.seth(330)
  o.fd(10)
  o.seth(270)
  o.fd(10)
  o.seth(150)
  o.fd(10)
  o.pu()

def rightwindow (posx , posy): #defining one of the windows so it is repeatable
  o.setpos(posx, posy)
  o.seth(90)  
  o.pd()
  o.fd(10)
  o.seth(30)
  o.fd(10)
  o.seth(270)
  o.fd(10)
  o.seth(210)
  o.fd(10)
  o.pu()

def shop (posx , posy): #defining the code for drawing the shop
  o.color('black')
  o.fillcolor('#EEAC33') #changing the turtle colour using hex code
  o.setpos(posx + 40, posy + 25)
  o.seth(90)
  o.begin_fill() #fill code to colour a whole area rather than just lines
  o.pd()
  o.fd(45)
  o.seth(0)
  o.fd(10)
  o.seth(270)
  o.fd(30)
  o.seth(0)
  o.fd(50)
  o.seth(90)
  o.fd(30)
  o.seth(0)
  o.fd(10)
  o.seth(270)
  o.fd(45)
  o.seth(180)
  o.fd(70)
  o.end_fill() #fill code to colour a whole area rather than just lines
  o.pu()
  o.fillcolor('#C88912') #changing the turtle colour using hex code
  o.begin_fill() #fill code to colour a whole area rather than just lines
  o.setpos(posx + 52.5, posy + 45)
  o.pd()
  o.seth(225)
  o.fd(10)
  o.seth(0)
  o.fd(60)
  o.seth(135)
  o.fd(10)
  o.seth(180)
  o.fd(45)
  o.end_fill() #fill code to colour a whole area rather than just lines
  o.pu()
  o.setpos(posx + 36, posy + 100)
  o.fillcolor('#FA3333') #changing the turtle colour using hex code
  o.begin_fill() #fill code to colour a whole area rather than just lines
  o.seth(268.5)
  o.pd()
  o.fd(30)
  o.seth(0)
  o.fd(80)
  o.seth(91.5)
  o.fd(30)
  o.seth(180)
  o.fd(80)
  o.end_fill() #fill code to colour a whole area rather than just lines
screen.tracer(1)
def drawmap():
  drawstream()
  drawbush()
  drawcity()
  drawshop()
drawmap()
