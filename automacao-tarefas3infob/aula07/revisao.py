from tkinter import LEFT
import pyautogui, time


#mover
# pyautogui.moveTo(512, 540, duration=.5)

# pyautogui.moveRel(100, 0, duration=.5)
# pyautogui.moveRel(0, -100, duration=.5)
# pyautogui.moveRel(-100, 0, duration=.5)
# pyautogui.moveRel(0, 100, duration=.5)

# drag
'''
pyautogui.moveTo(257, 128, duration=.5)
pyautogui.dragTo(27, 19, duration=.5)
'''

#click
'''
pyautogui.click(57, 17, duration=.5)
pyautogui.click(57, 17, duration=.5, clicks=150)

'''

# localizar um item da tela
btnXY = pyautogui.locateCenterOnScreen('./aula07/google_bar.png')
pyautogui.click(btnXY, duration=.5)

