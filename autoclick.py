import pyautogui
import pyperclip
from time import sleep

def escrever(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl', 'v')

pyautogui.click(325,1058, duration=2)
pyautogui.click(363,19, duration=2)
pyautogui.click(215,59, duration=2)
escrever('data')
pyautogui.click(202,143, duration=2)
pyautogui.click(770,429, duration=2)
escrever('viniciuskeglesads@gmail.com')
sleep(2)
pyautogui.press('tab')
escrever('Pernamacabro@2')
pyautogui.click(706,646, duration=2)