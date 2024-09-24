import pyautogui
# import pyscreeze

pyautogui.click(200, 200, interval=.5)
pyautogui.press('space')                               

while True:
    if pyautogui.pixelMatchesColor(232, 429, [83, 83, 83], 70):
        print(pyautogui.pixel(232, 429))
        pyautogui.press('space')
    if pyautogui.pixelMatchesColor(232, 429, [172, 172, 172], 70):
        pyautogui.press('space')
    if pyautogui.pixelMatchesColor(136, 395, [172, 172, 172], 70):
        pyautogui.press('space')
    if pyautogui.pixelMatchesColor(136, 395, [172, 172, 172], 70):
        pyautogui.press('down')
    

    #112, 429