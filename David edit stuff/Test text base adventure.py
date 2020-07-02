import cmd
import os
import random
import textwrap
import sys
import time
from turtle import *

screen_width = 100

#player setup
class player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.hp = 20
        self.mp = 20
        self.status_effect = []
        self.location = "a1"
        self.game_over = False
myPlayer = player()

#turtle setup
from time import sleep    
g = Turtle() #make turtle for grid
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


p = Turtle() #make turtle for playerpos
p.hideturtle()
p.speed(0)
def dpl(): #draw player location
    p.penup()
    p.setpos(gridposx[str(myPlayer.location[1])] + 50,gridposy[str(myPlayer.location[0])] + 50)
    p.clear()
    p.pendown()
    for x in range(4):
        p.fd(50)
        p.left(90)
    p.penup()



## title screen

def title_screen_selections():
    option = input(">  ")
    if option.lower() == ("play"):
        start_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        while option.lower() not in ["play", "help", "quit"]:
            print("Please enter a valid command.")
            option = input("> ")
            if option.lower() == ("play"):
                start_game()
            elif option.lower() == ("help"):
                help_menu()
            elif option.lower() == ("quit"):
                sys.exit()

def title_screen():
    os.system('clear')
    print("###########################")
    print("# Welcome to the Text Rpg #")
    print("###########################")
    print("         - Play -          ")
    print("         - Help -          ")
    print("         - Quit -          ")
    print("    - Copyright 2020 -     ")
    title_screen_selections()

def ig_help_menu():
    print("\n\n")
    print("      - Type your commands to do them -      ")
    print("- Use 'up', 'down', 'left', 'right' to move -")
    print("     - Use 'look' to inspect something -     ")
    print("         - Good Luck and have fun! -         ")
    print("\n")
    

def help_menu():
    os.system('clear')
    print("#############################################")
    print("#         Welcome to the Text Rpg           #")
    print("#############################################")
    print("      - Type your commands to do them -      ")
    print("- Use 'up', 'down', 'left', 'right' to move -")
    print("     - Use 'look' to inspect something -     ")
    print("         - Good Luck and have fun! -         ")
    print('\n\n\n')
    print("###########################")
    print("# Welcome to the Text Rpg #")
    print("###########################")
    print("         - Play -          ")
    print("         - Help -          ")
    print("         - Quit -          ")
    print("    - Copyright 2020 -     ")
    title_screen_selections()

ZONENAME = ""
DESCRIPTION = "description"
EXAMINATION = "examine"
SOVLED = False
UP = "up", "north"
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False,
                 }
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
## game interacttivity
dpl()
def print_location():
    print("\n" + ("################################################################################"))
    if len(zonemap[myPlayer.location][ZONENAME])%2 == 1:
        print("#" + (int(((77-len(zonemap[myPlayer.location][ZONENAME]))/2))* (" "))+ str(zonemap[myPlayer.location][ZONENAME]) + (int(((77-len(zonemap[myPlayer.location][ZONENAME]))/2))* (" ")) + " #")
    else:
        print("#" + (int(((78-len(zonemap[myPlayer.location][ZONENAME]))/2))* (" "))+ str(zonemap[myPlayer.location][ZONENAME]) + (int(((78-len(zonemap[myPlayer.location][ZONENAME]))/2))* (" ")) + "#")
    
    if len(zonemap[myPlayer.location][DESCRIPTION])%2 == 1:
        print("#" + (int(((77-len(zonemap[myPlayer.location][DESCRIPTION]))/2))* (" "))+ str(zonemap[myPlayer.location][DESCRIPTION]) + (int(((77-len(zonemap[myPlayer.location][DESCRIPTION]))/2))* (" ")) + " #")
    else:
        print("#" + (int(((78-len(zonemap[myPlayer.location][DESCRIPTION]))/2))* (" "))+ str(zonemap[myPlayer.location][DESCRIPTION]) + (int(((78-len(zonemap[myPlayer.location][DESCRIPTION]))/2))* (" ")) + "#")
    print("################################################################################")
    dpl()


def prompt():
    print ("\n" + "#########################")
    print ("What would you like to do?")
    action = input ("> ")
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look', 'help']
    while action.lower() not in acceptable_actions:
        print('Unknown action, try again.\n')
        action = input('> ')
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() == 'help':
        ig_help_menu()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())
    


def player_move(myAction):
    ask = "Where would you like to move to?\n> "
    dest = input(ask)
    while dest.lower() not in ["left", "west", 'right', 'east', 'up', 'north', 'down', 'south']:
        print("\nThat is not a valid direction.")
        dest = input("\nPlease select a new direction\n> ")
            
    if myPlayer.location in ["a1","b1","c1","d1"] and dest.lower() in ["left", "west"]:
        while dest.lower() in ["left", "west"]:
            print("\nYou're on the edge of the board.")
            dest = input("\nPlease select a new direction\n> ")
            if dest.lower() in ['right', 'east']:
                destination = zonemap[myPlayer.location][RIGHT]
                movement_handler(destination)
            elif dest.lower() in ['up', 'north']:
                destination = zonemap[myPlayer.location][UP]
                movement_handler(destination)
            elif dest.lower() in ['down', 'south']:
                destination = zonemap[myPlayer.location][DOWN]
                movement_handler(destination)
            while dest.lower() not in ["left", "west", 'right', 'east', 'up', 'north', 'down', 'south']:
                print("\nThat is not a valid direction.")
                dest = input("\nPlease select a new direction\n> ")

                
    elif myPlayer.location in ["a4","b4","c4","d4"] and dest.lower() in ["right", "east"]:
        while dest.lower() in ["right", "east"]:
            print("\nYou're on the edge of the board.")
            dest = input("\nPlease select a new direction\n> ")
            if dest.lower() in ['left', 'west']:
                destination = zonemap[myPlayer.location][LEFT]
                movement_handler(destination)
            elif dest.lower() in ['up', 'north']:
                destination = zonemap[myPlayer.location][UP]
                movement_handler(destination)
            elif dest.lower() in ['down', 'south']:
                destination = zonemap[myPlayer.location][DOWN]
                movement_handler(destination)
            while dest.lower() not in ["left", "west", 'right', 'east', 'up', 'north', 'down', 'south']:
                print("\nThat is not a valid direction.")
                dest = input("\nPlease select a new direction\n> ")

                
    elif myPlayer.location in ["a1","a2","a3","a4"] and dest.lower() in ["up", "north"]:
        while dest.lower() in ["up", "north"]:
            print("\nYou're on the edge of the board.")
            dest = input("\nPlease select a new direction\n> ")
            if dest.lower() in ['right', 'east']:
                destination = zonemap[myPlayer.location][RIGHT]
                movement_handler(destination)
            elif dest.lower() in ['left', 'west']:
                destination = zonemap[myPlayer.location][LEFT]
                movement_handler(destination)
            elif dest.lower() in ['down', 'south']:
                destination = zonemap[myPlayer.location][DOWN]
                movement_handler(destination)
            while dest.lower() not in ["left", "west", 'right', 'east', 'up', 'north', 'down', 'south']:
                print("\nThat is not a valid direction.")
                dest = input("\nPlease select a new direction\n> ")

                
    elif myPlayer.location in ["d1","d2","d3","d4"] and dest.lower() in ["down", "south"]:
        while dest.lower() in ["down", "south"]:
            print("\nYou're on the edge of the board.")
            dest = input("\nPlease select a new direction\n> ")
            if dest.lower() in ['right', 'east']:
                destination = zonemap[myPlayer.location][RIGHT]
                movement_handler(destination)
            elif dest.lower() in ['up', 'north']:
                destination = zonemap[myPlayer.location][UP]
                movement_handler(destination)
            elif dest.lower() in ['left', 'west']:
                destination = zonemap[myPlayer.location][LEFT]
                movement_handler(destination)
            while dest.lower() not in ["left", "west", 'right', 'east', 'up', 'north', 'down', 'south']:
                print("\nThat is not a valid direction.")
                dest = input("\nPlease select a new direction\n> ")

    else:
        if dest.lower() in ['left', 'west']:
            destination = zonemap[myPlayer.location][LEFT]
            movement_handler(destination)
        elif dest.lower() in ['right', 'east']:
            destination = zonemap[myPlayer.location][RIGHT]
            movement_handler(destination)
        elif dest.lower() in ['up', 'north']:
            destination = zonemap[myPlayer.location][UP]
            movement_handler(destination)
        elif dest.lower() in ['down', 'south']:
            destination = zonemap[myPlayer.location][DOWN]
            movement_handler(destination)


def movement_handler(destination):
    print("\n" + "You have moved to " + destination + ".")
    myPlayer.location = destination
    print_location()

def player_examine(action):
    if zonemap[myPlayer.location][SOVLED]:
        print("You have already exhausted this zone.")
    else:
        print("You can activate a puzzle.")

def start_game():
    setup_game()
    printplayerlocation()

def main_game_loop():
    while myPlayer.game_over is False:
        prompt()
        #blah handle

def setup_game():
    os.system("clear")

    question1 = "Hello, what's your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_name = input(">  ")
    myPlayer.name = player_name

    ### INTRO
    question3 = "Welcome, " + player_name + "\n"
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)

    speech1 = "Welcome to the something game.\n"
    speech2 = "The aim of the game is to manage the stream.\n"
    speech3 = "The map of the game is shown on the Turtle module which should've opened up.\n"
    speech4 = "Good Luck.\n"
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    main_game_loop()
title_screen()
