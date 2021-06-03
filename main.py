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

colorama.init(autoreset=True)
decks = [["rage", "valkyrie", "wizard", "rage_barbarian", "baby_dragon", "chr_balloon", "skeleton_horde", "minion_horde"]]

while True:
    command = input(">>")
    if command not in commands_list:
        print("That is not a command")
    if command in commands_list:
        if command == "mouselocation":
            while not keyboard.is_pressed("z"):
                if keyboard.is_pressed("q"):
                    print(pyautogui.position())
                    time.sleep(0.5)
        elif command == "startscan":
            time.sleep(4)
            while True:
                starttime = time.time()
                location = pyautogui.locateOnScreen(f'./pics/baby_dragonq.png', confidence=0.5)
                if location:
                    pyautogui.click(location)
                    pyautogui.click(778, 667)
                    endtime = time.time()
                    print(f"time: {endtime - starttime}")

                endtime = time.time()
                print(f"time: {endtime-starttime}")
                time.sleep(2)


        elif command == "checkend":
            check_game_end()
        elif command == "checkdeck":
            check_deck()
        elif command == "help":
            help_commands()
        elif command == "elexiercheck":
            elexier_check_new()

