import pyautogui
import time
import os
import colorama
from cords.deck_ingame import deck_ingame

def check_deck():
    time.sleep(2)
    bigtime = time.time()
    is_in_deck = []
    for card in os.listdir("./test/"):
        print(f"Starting {colorama.Fore.BLUE}{card}")
        starttime = time.time()
        card_location = pyautogui.locateOnScreen(f'./test/{card}', confidence=0.5, region=(deck_ingame))
        endtime = time.time()
        print(f"{colorama.Fore.GREEN}{card}:")
        print(f"Insgesamt: {colorama.Fore.RED}{endtime - starttime} Sekuden")
        if card_location:
            print("")
            print(f"{colorama.Fore.RED}KARTE WURDE GEFUNDEN!")
            print("")
            card_name = str(card)
            card_name = card_name.replace(".png", "")
            is_in_deck.append(card_name)
    print(is_in_deck)
    endbigtime = time.time()
    print("")
    print(f"Insgesamt: {endbigtime-bigtime} Sekunden")
    print("")
    pyautogui.click(card_location)
    print("Done")