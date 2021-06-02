from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con

# pyautogui.displayMousePosition()

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while True:
   
    # Cofres
    if keyboard.is_pressed('space'):
        time.sleep(0.05)
        keyboard.press('shift')
        for i in range(322,1360,115):
            click(i, 640)
        keyboard.release('shift')

    # Pelea
    # if keyboard.is_pressed('z'):
    #     for i in range(700,1001, 150):
    #         for j in range(670, 791, 40):
    #             click(i, j)

    # Minerales
    if keyboard.is_pressed('m'):
        time.sleep(0.05)
        for i in range(370,1291,115):
            click(i, 640)

    if keyboard.is_pressed('e'):
        break
