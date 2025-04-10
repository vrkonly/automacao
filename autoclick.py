import pyautogui
import webbrowser
import pyperclip
import time


def escrever(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')

webbrowser.open('https://cursoautomacao.netlify.app/?_gl=1*1edetzk*_ga*MTM4NTczNTY2NS4xNzQzMTcwMzA0*_ga_37GXT4VGQK*MTc0NDI5ODg3MC4yOS4xLjE3NDQyOTk2OTMuMC4wLjA.')
pyautogui.click(1912,183, duration=2)
pyautogui.scroll(-500)
pyautogui.click(pyautogui.locateOnScreen('captura.PNG'), duration=2)
escrever('Vinícius Romeu Kegles')
pyautogui.click(1472,733, duration=2)
pyautogui.click(1126,207, duration=2)
pyautogui.scroll(1000)
time.sleep(1.5)
pyautogui.scroll(-2000)
pyautogui.click(pyautogui.locateCenterOnScreen('excel.PNG'), duration=2)
pyautogui.click(pyautogui.locateCenterOnScreen('pdf.PNG'), duration=2)