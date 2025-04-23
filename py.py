import pyautogui
import time
import keyboard
import pyperclip

def escrever(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl', 'v')

lista = ['Pai', 'Mãe']

for x in lista:
    time.sleep(1.5)
    pyautogui.click(383,180, duration=2)
    time.sleep(1.5)
    pyautogui.hotkey('ctrl','a')
    time.sleep(1)
    pyautogui.press('delete')
    time.sleep(1.5)
    pyautogui.write(f'{x}')
    time.sleep(1.5)
    pyautogui.click(458,332, duration=2)
    time.sleep(1.5)
    pyautogui.click(873,993, duration=2)
    time.sleep(1.5)
    escrever('Teste')
    pyautogui.press('enter')



