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
        self.hp = 20
        self.mp = 20
        self.status_effect = []
my_player = player()

## title screen

def title_screen_selections():
    option = input(">")
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
    print("        - Play -           ")
    print("        - Help -           ")
    print("        - Quit -           ")
    title_screen_selections()

def help_menu():
    os.system('clear')
    print("##################################")
    print("#    Welcome to the Text Rpg     #")
    print("##################################")
    print("- Use up, down, left, right to move -")
    print("- Type your commands to do them  -")
    print("-Use 'look' to inspect something -")
    print("-Good Luck and have fun!-")
    title_screen_selections()
title_screen()
