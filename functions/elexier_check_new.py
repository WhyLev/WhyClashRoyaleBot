from main import *
from cords.elexier_cords import *

def elexier_check_new():
    time.sleep(2)
    bigtime = time.time()
    is_in_deck = []
    for card in os.listdir("./pics/elexier_numbers/"):
        print(f"Starting {colorama.Fore.BLUE}{card}")
        starttime = time.time()
        card_location = pyautogui.locateOnScreen(f'./pics/elexier_numbers/{card}', confidence=0.5) #, region=(760, 1025, 860, 1075)
        endtime = time.time()
        print(f"{colorama.Fore.GREEN}{card}:")
        print(f"Insgesamt: {colorama.Fore.RED}{endtime - starttime} Sekuden")
        if card_location:
            print("")
            print(f"{colorama.Fore.RED}Elexier gefunden!")
            print("")
            card_name = str(card)
            card_name = card_name.replace(".png", "")
            is_in_deck.append(card_name)
    print(is_in_deck)
    endbigtime = time.time()
    print("")
    print(f"Insgesamt: {endbigtime-bigtime} Sekunden")
    print("")
    print("Done")