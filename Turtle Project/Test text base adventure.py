import cmd
import os
import random
import textwrap
import sys
import time

screen_width = 100

#player setup
class player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.hp = 20
        self.mp = 20
        self.status_effect = []
        self.location = "start"
        self.game_over = False
myPlayer = player()

## title screen

def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ["play", "help", "quit"]:
        print("Please enter a valid command.")
        option = input(">")
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

def help_menu():
    os.system('clear')
    print("#############################################")
    print("#         Welcome to the Text Rpg           #")
    print("#############################################")
    print("      - Type your commands to do them -      ")
    print("- Use 'up', 'down', 'left', 'right' to move -")
    print("     - Use 'look' to inspect something -     ")
    print("         - Good Luck and have fun! -         ")
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
        ZONENAME: "lol",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "a3",
        DOWN: 'c3',
        LEFT: 'b2',
        RIGHT: 'b4'
        },
    'b4':{
        ZONENAME: "lol",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "a4",
        DOWN: 'c4',
        LEFT: 'b3',
        RIGHT: ''
        },
    'c1':{
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
        ZONENAME: "lol",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "c1",
        DOWN: '',
        LEFT: '',
        RIGHT: 'd2'
        },
    'd2':{
        ZONENAME: "lol",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "c2",
        DOWN: '',
        LEFT: 'd1',
        RIGHT: 'd3'
        },
    'd3':{
        ZONENAME: "lol",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "c3",
        DOWN: '',
        LEFT: 'd2',
        RIGHT: 'd4'
        },
    'd4':{
        ZONENAME: "lol",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        SOVLED: False,
        UP: "c4",
        DOWN: '',
        LEFT: 'd3',
        RIGHT: ''
        }}
## game interacttivity
    
def print_location():
    print("\n" + ("#" * (4 * len(myplayer.location))))
    print("# " + myplayer.location.upper() + '#')
    print('# ' + zonemap[myplayer.position][DESCRIPTION] + ' #')
    print("\n" + ("#" * (4 * len(myplayer.location))))


def prompt():
    print ("\n" + "#########################")
    print ("What would you like to do?")
    action = input (">")
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look']
    while action.lower() not in acceptable_actions:
        print('Unknow action, try again.\n')
        action = input('> ')
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())


def player_move(myAction):
    ask = "where would you like to move to?\n"
    dest = input(ask)
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
    print("\n" + "You have moved to the " + destination + ".")
    myPlayer.location = destination
    print_location()

def player_examine(action):
    if zonemap[myPlayer.location][SOLVED]:
        print("You have already exhausted this zone.")
    else:
        print("You can activate a puzzle.")

def start_game():
    setup_game()

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
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name

    question2 = "Hello, what role do you want to play?\n"
    question2added = "(You can player as a warrior, mage, or priest)?\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_job = input("> ")
    valid_jobs = ['warrior', 'mage', 'priest']
    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print("You are now a " + player_job + "!\n")
    while player_job.lower() not in valid_jobs:
        player_job = input("> ")
        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
            print("You are now a " + player_job + "!\n")

    ### INTRO
    question3 = "Welcome. " + player_name
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    
title_screen()

