import pyautogui
import time

# Teste para saber a localização do mouse
# Abrir navegador
time.sleep(2)
pyautogui.press("win")
time.sleep(1)
pyautogui.write("chrome")
time.sleep(1)
pyautogui.press("enter")
time.sleep(2)
local = pyautogui.position()
print(local)
