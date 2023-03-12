import pyautogui
import time
import threading
import keyboard  # using module keyboard


def printit():
    threading.Timer(2.0, printit).start()
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')


while True:
    try: 
        if keyboard.is_pressed('q') and keyboard.is_pressed('c'):
            print('start!')
            printit()
            break 
    except:
        break