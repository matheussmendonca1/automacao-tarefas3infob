import pyautogui

pyautogui.moveTo(479, 438, duration=0.5) # Move to the coordinates (x, y), with a duration of 0.5 seconds

pyautogui.dragRel(150, 0, duration=0.5) 
pyautogui.dragRel(0, 150, duration=0.5) 
pyautogui.dragRel(-150, 0, duration=0.5) 
pyautogui.dragRel(0, -150, duration=0.5) 