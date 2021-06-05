import pyautogui
import time
import os
import colorama
from cords.end_screen_cord import end_screen_cord

#Working to import

def check_game_end():
    time.sleep(2)
    bigtime = time.time()
    for ok_screen in os.listdir("./pics/end_screen/"):
        print(f"Starting")
        starttime = time.time()
        ok_location = pyautogui.locateOnScreen(f'./pics/end_screen/{ok_screen}', confidence=0.5, region=(end_screen_cord))
        endtime = time.time()
        print("")
        print(f"Insgesamt: {colorama.Fore.RED}{endtime - starttime} Sekuden")
        if ok_location:
            print("")
            print(f"{colorama.Fore.RED}ENDSCREEN WURDE GEFUNDEN! SPIEL VORBEI")
            print("")
    endbigtime = time.time()
    pyautogui.click(ok_location)
    print("Done")