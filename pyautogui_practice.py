import pyautogui
import time

# time.sleep(3.5)

# print(pyautogui.size())
# print(pyautogui.position())

# pyautogui.moveTo(100, 300, 1)
time.sleep(3)
distance = 300
while distance > 0:
    pyautogui.dragRel(distance, 0, 1, button="left")
    distance -= 25
    pyautogui.dragRel(0, distance, 1, button= "left")
    pyautogui.dragRel(-distance, 0, 1, button= "left")
    distance -= 25
    pyautogui.dragRel(0, -distance, 1, button= "left")