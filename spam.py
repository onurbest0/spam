import pyautogui
import time

time.sleep(4)
f = open("file.txt", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
