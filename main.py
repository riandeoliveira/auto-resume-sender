import pyautogui
import time

print('========== CV-AUTO-SENDER ==========\n')

print('by Rian Oliveira\n')

# Recebe os dados inseridos pelo usuário.
ADDRESSEE = input('E-mail do destinatário: ')
SUBJECT = input('Assunto do e-mail: ')
MESSAGE = input('Mensagem do e-mail: ')
CV_LOCATION = input('Local do currículo na sua máquina: ')

print('\nEnviando o seu currículo...')
print('Por favor, não mexa no mouse ou teclado enquanto o programa estiver rodando.')

# Abre o navegador.
time.sleep(5)
pyautogui.hotkey('win', 'd')
time.sleep(0.5)
pyautogui.press('win')
time.sleep(0.5)
pyautogui.write('Microsoft Edge')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.hotkey('win', 'up')

# Entra no Gmail do usuário.
time.sleep(0.5)
pyautogui.write('https://mail.google.com/mail/u/1/#inbox')
time.sleep(0.5)
pyautogui.press('enter')

# Escreve um novo e-mail.
time.sleep(3)
for i in range(12):
    pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('enter')

# Insere o e-mail do destinatário.
time.sleep(0.5)
pyautogui.write(ADDRESSEE)
time.sleep(0.5)
pyautogui.press('enter')

# Insere o assunto do e-mail.
time.sleep(1)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.write(SUBJECT)
time.sleep(0.5)
pyautogui.press('enter')

# Insere uma mensagem no e-mail.
time.sleep(1)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.write(MESSAGE)
time.sleep(0.5)

# Anexa o currículo no e-mail.
time.sleep(1)
for i in range(3):
    pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(2)
pyautogui.write(CV_LOCATION)
time.sleep(0.5)
pyautogui.press('enter')

# Envia o e-mail.
time.sleep(3)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('enter')

print('\n====================================')