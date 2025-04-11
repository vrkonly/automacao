import pyautogui
import webbrowser
import pyperclip
import time

def escrever(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')

for x in range(30):
    webbrowser.open('https://www.instagram.com/')
    pyautogui.click(1139,361, duration=2)
    time.sleep(2)
    escrever('pizzasoffice')
    pyautogui.press('tab')
    escrever('Paralelepipedada@2')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(69,267, duration=2)
    time.sleep(2)
    escrever('Nike')
    time.sleep(2)
    pyautogui.click(171,256, duration=2)
    time.sleep(2)
    pyautogui.click(784,869, duration=2)
    time.sleep(3)

    try:
        pyautogui.locateOnScreen('curtido.PNG')
        print('Você já curtiu o post do dia de hoje.')
    except pyautogui.ImageNotFoundException:
        pyautogui.click(985,882, duration=2)

    time.sleep(2)

    try:
        pyautogui.locateOnScreen('comentado.PNG')
        print('Já existe um comentário no post de hoje.')
    except pyautogui.ImageNotFoundException:
        pyautogui.click(1073,989, duration=2)
        escrever('Muito Top!')
        pyautogui.press('enter')
    time.sleep(86400)




