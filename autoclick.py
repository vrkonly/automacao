#pyautogui.alert(text='Estamos entrando em nossa Automação', title='Aviso')
#email = pyautogui.prompt(text='Digite seu e-mail', title='Informações Obrigatórias')
#print(f'você digitou {email}')
#pyautogui.confirm(text=f'Continuar rodando nossa automação com o email {email}?', title='Confirmação', buttons=['Sim', 'Não', 'Cancelar'])
#pyautogui.password(text='Digite sua senha:', title='Senha de Login', mask='*')

import pyautogui
import pyperclip

def escrever(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')

operacao = True

while operacao == True:
    selecao = pyautogui.confirm(text='Você deseja continuar com o sistema?', title='Automação', buttons=['Continuar', 'Sair'])
    if selecao == 'Continuar':
        email = pyautogui.prompt(text='Digite seu E-mail: ', title ='Informações Obrigatórias.')
        senha = pyautogui.password(text='Digite sua Senha: ', title='Senha de Acesso', mask='*')
    elif selecao == 'Sair':
        operacao = False

    if email == 'automacao@gmail.com' and senha == 'Testes@2':
        print('Parabéns, você acessou sua conta e agora vamos imprimir seus dados criando um bloco de notas.')
        pyautogui.click(x=813,y=26, duration=1.5, button='right')
        pyautogui.click(858,304, duration=1.5)
        pyautogui.moveTo(1244,307, duration=1.5)
        pyautogui.click(1240,532, duration=1.5)
        escrever('Automação')
        for x in range (1, 3):        
            pyautogui.click(871,36)
        escrever(f'E-mail: {email}\nSenha: {senha}')
        confirma = pyautogui.confirm(f'Você deseja continuar com a conta {email} e salvar estas informações neste bloco de notas?', title='Confirmação', buttons=['Sim', 'Não'])
        if confirma == 'Sim':
            pyautogui.click(19,82, duration=1.5)
            pyautogui.click(46,169, duration=1.5)
            operacao = False
    elif email != 'automacao@gmail.com':
        pyautogui.alert(text='Infelizmente você digitou um e-mail que não corresponde ao cadastrado neste sistema, favor tentar novamente.', title='Atenção!')
       
    

    

