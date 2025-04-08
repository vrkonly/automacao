import pyautogui
import pyperclip

def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl', 'v')

pyautogui.click(403,572, duration=3)
pyautogui.click(880,994, duration=3)
pyautogui.typewrite('Oi amor, estou te enviando essa mensagem via codigo! Te amo <3')
pyautogui.click(1647,992, duration=3)