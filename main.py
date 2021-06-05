import colorama

#Import from Functions
from functions.check_new_deck import check_deck
from functions.check_end import check_game_end
from functions.elexier_check import elexier_check
from functions.help import help_commands
from functions.elexier_check_new import elexier_check_new
from functions.start_game import start_game
from functions.mouselocation import mouselocation
from functions.test_command import test_command

#Import from Commandlist
from commands_list import commands_list

#Import from GUI
        #from gui.programmer import *
        #from gui.functions import *

#colors
colorama.init(autoreset=True)


while True:
    command = input(">>")
    command = command.lower()
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
        elif command == "startgame":
            start_game()
        elif command == "testcommand":
            test_command()

