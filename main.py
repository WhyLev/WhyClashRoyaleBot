import pyautogui
import keyboard
import time
import colorama
import os
from functions.check_new_deck import check_deck
from functions.check_end import check_game_end
from functions.elexier_check import *
from functions.help import help_commands
from commands_list import *
from functions.elexier_check_new import *
from functions.start_game import *
from functions.mouselocation import *

colorama.init(autoreset=True)

while True:
    command = input(">>")
    if command not in commands_list:
        print("Das ist kein Command")
    if command in commands_list:
        if command == "checkend":
            check_game_end()
        elif command == "checkdeck":
            check_deck()
        elif command == "help":
            help_commands()
        elif command == "elexiercheck":
            elexier_check_new()
        elif command == "mouselocation":
            mouselocation()
        elif command == "start_game":
            startgame()


