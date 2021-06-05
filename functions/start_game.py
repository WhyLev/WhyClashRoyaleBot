import pyautogui
import time
import colorama
import os



# Working to import
def start_game():
        time.sleep(2)
        bigtime = time.time()
        for ok_screen in os.listdir("./pics/end_screen/"):
            print(f"Starting")
            starttime = time.time()
            ok_location = pyautogui.locateOnScreen(f'./pics/end_screen/{ok_screen}', confidence=0.5)
            endtime = time.time()
            print("")
            print(f"Insgesamt: {colorama.Fore.RED}{endtime - starttime} Sekuden")
            if ok_location:
                print("")
                print(f"{colorama.Fore.RED}GAME WURDE GESTARTET")
                print("")
        endbigtime = time.time()
        pyautogui.click(ok_location)
        print("Done")