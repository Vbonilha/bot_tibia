# Importação de módulos necessários
import pynput
import pyautogui

from vida_mana import manager_suplies
pyautogui.ImageNotFoundException(False)
import threading
import imgs
import constants

# Definição de variáveis globais
# Define as teclas de atalho a serem usadas
full_defensive_hotkey = '-'
full_offensive_hotkey = '='
use_ring_hotkey = 'F10'
list_hotkey_before = [full_offensive_hotkey, use_ring_hotkey]
list_hotkey_after = [full_defensive_hotkey, use_ring_hotkey]
list_hotkey_attacks = [{"hotkey":'F8',"delay": 0.5}, {"hotkey": 'F5', "delay": 1.5}, {"hotkey": 'F4', "delay": 1.5},{"hotkey":'F6',"delay": 1}]
running = False

# Função para rotacionar as habilidades
def rotate_skills():
    while not event_rotate_skills.is_set():
        for attack in list_hotkey_attacks:
            if event_rotate_skills.is_set():
                return
            if pyautogui.locateOnScreen('imgs/region_battle.PNG', confidence=0.85, region=constants.region_battle):
                continue
            print('Executando: ', attack["hotkey"])
            pyautogui.press('space')
            pyautogui.press(attack["hotkey"])
            pyautogui.sleep(attack["delay"])

# Função para executar uma hotkey específica  
def execute_hotkey(hotkey):
    pyautogui.press(hotkey)

# Função que será chamada quando uma tecla for pressionada
def key_code(key):
    global running
    print('Key ->', key)
    if key == pynput.keyboard.Key.delete:
        return False
    if hasattr(key, 'char') and key.char == 'f':
        if running == False:
            running = True
            global th_rotate_skills, event_rotate_skills, th_suplies, event_suplies
            event_suplies = threading.Event()
            th_suplies = threading.Thread(target=manager_suplies, args=(event_suplies, ))
            event_rotate_skills = threading.Event()
            th_rotate_skills = threading.Thread(target=rotate_skills) # para nao travar o terminal
            print('Iniciando a rotação de skills')
            for hotkey in list_hotkey_before:
                execute_hotkey(hotkey)
            th_rotate_skills.start()
        else:
            running = False
            event_suplies.set()
            th_suplies.join()
            event_rotate_skills.set()
            th_rotate_skills.join()
            print('Parando rotação de skills')
            for hotkey in list_hotkey_after:
                execute_hotkey(hotkey)

# Criação do listener de teclado
with pynput.keyboard.Listener(on_press=key_code) as listener:
    listener.join()
