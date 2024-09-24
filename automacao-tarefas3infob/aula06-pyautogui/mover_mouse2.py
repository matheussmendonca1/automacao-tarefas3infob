import pyautogui

pyautogui.moveTo(960, 590, duration=0.5) # Move to the coordinates (x, y), with a duration of 0.5 seconds

pyautogui.moveRel(150, 0, duration=0.5) 
pyautogui.moveRel(0, 150, duration=0.5) 
pyautogui.moveRel(-150, 0, duration=0.5) 
pyautogui.moveRel(0, -150, duration=0.5) 