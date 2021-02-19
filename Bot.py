from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #pause for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(550, 400)[0] == 0:
        click(550, 400)
    if pyautogui.pixel(640, 400)[0] == 0:
        click(640, 400)       
    if pyautogui.pixel(730, 400)[0] == 0:
        click(730, 400)
    if pyautogui.pixel(820, 400)[0] == 0:
        click(820, 400)