import pyautogui
import pyperclip

def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl', 'v')

pyautogui.click(406,182, duration=2)
escrever_frase('Mãe')
pyautogui.click(422,330, duration=2)
pyautogui.click(900,993, duration=2)
escrever_frase('Te amo mãe <3')
pyautogui.click(1648,993, duration=2)