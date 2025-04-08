import pyautogui

pyautogui.alert(text='Estamos entrando em nossa Automação', title='Aviso')

email = pyautogui.prompt(text='Digite seu e-mail', title='Informações Obrigatórias')
print(f'você digitou {email}')

pyautogui.confirm(text=f'Continuar rodando nossa automação com o email {email}?', title='Confirmação', buttons=['Sim', 'Não', 'Cancelar'])

pyautogui.password(text='Digite sua senha:', title='Senha de Login', mask='*')
