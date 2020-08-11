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

zonemap = {
        'a1':{
            ZONENAME: "City Area"
            },

        'a2':{
      
            ZONENAME: "Bush"
            },

        'a3':{
            ZONENAME: "Stream"
            },

        'a4':{
            ZONENAME: "City Area"
            },

        'b1':{
            ZONENAME: "Bush"
            },

        'b2':{
            ZONENAME: "Stream"
            },

        'b3':{
            ZONENAME: "Stream"
            },

        'b4':{
            ZONENAME: "City Area"
            },

        'c1':{
            ZONENAME: "Stream"
            },

        'c2':{
            ZONENAME: "Stream"
            },

        'c3':{
            ZONENAME: "Bush"
            },

        'c4':{
            ZONENAME: "City Area"
            },

        'd1':{
            ZONENAME: "City Area"
            },

        'd2':{
            ZONENAME: "Bush"
            },

        'd3':{
            ZONENAME: "Bush"
            },

        'd4':{
            ZONENAME: "Shop"
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
