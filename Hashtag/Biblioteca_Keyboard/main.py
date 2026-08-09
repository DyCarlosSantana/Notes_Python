import pyautogui # Biblioteca para automação de mouse e teclado
import keyboard # Biblioteca para capturar teclas
import time 

# Criar uma função

def reuniao():
    time.sleep(2)
    print("Iniciando execução")

    # Abrir navegador
    pyautogui.press("win")
    time.sleep(1)
    pyautogui.write("chrome")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(2)
    # Selecionar Conta
    pyautogui.click(x=1046, y=499)
    time.sleep(1)
    
    # Acessar Link
    pyautogui.write("https://meet.google.com/landing")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(3)
    
    # Entrar na reunião
    pyautogui.press("enter")
    time.sleep(1)
    
    # Ajustar microfone e camera

# Associar essa função a uma combinação de teclas
    # hotkey se refere a combinação de teclas
    # add_hotkey se refere a adicionar uma combinação de teclas, e o segundo parametro é a função que será executada
keyboard.add_hotkey("ctrl + space", reuniao)

keyboard.wait("esc") # Esperar o usuario pressionar a tecla esc para sair