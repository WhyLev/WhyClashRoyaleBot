import keyboard
import time
import pyautogui

def mouselocation():
    while not keyboard.is_pressed("z"):
        if keyboard.is_pressed("q"):
            print(pyautogui.position())
            time.sleep(0.5)
