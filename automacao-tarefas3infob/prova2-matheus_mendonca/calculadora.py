import pyautogui, time

# abrindo windows
pyautogui.press("win", interval=.8)

# abrindo calculadora
pyautogui.write("calculadora", interval=.1)
pyautogui.press("enter")

time.sleep(1.5)

# abrindo aba de modos
pyautogui.click(75, 85, interval=1)

time.sleep(.5)

# abrindo modo programador
pyautogui.click(69, 284, interval=1.2)

# digitando numero
pyautogui.write("255")

time.sleep(1)

# mudando para BIN
pyautogui.click(69, 329, interval=1.2)


