import pyautogui
import time


def elexier_check():
    positions = [
        (846, 988),
        (883, 988),
        (921, 988),
        (959, 988),
        (997, 988),
        (1032, 988),
        (1072, 988),
        (1108, 988),
        (1146, 988),
        (1180, 988)
    ]
    time.sleep(4)
    for position in positions:
        screen = pyautogui.screenshot()
        pixel = screen.getpixel(position)
        print(pixel)
        #noch in Beta