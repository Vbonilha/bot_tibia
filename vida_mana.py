import pyautogui
import keyboard
import threading
import time

# Definições da nova função para gerenciar suprimentos
life_region = (1766, 304, 92, 5)
life_color = (240, 97, 97)

mana_region = (1766, 316, 92, 5)
mana_color = (83, 80, 217)  # Atualize conforme necessário

width = 92

def calcule_width(percent):
    return int(width * percent / 100)  # Cálculo da porcentagem baseada na região

def pixel_matchs_color(region, percent, color):
    result_percent = calcule_width(percent)  # Verificação da porcentagem baseada na cor
    x = region[0] + result_percent
    y = region[1] + region[3]
    return pyautogui.pixelMatchesColor(int(x), int(y), color, 10)

def manager_suplies(event):
    while not event.is_set():
        # Verificação da vida
        if not pixel_matchs_color(life_region, 50, life_color):
            print("Vida abaixo de 50%, pressionando F1")
            pyautogui.press('F1')
        
        if not pixel_matchs_color(life_region, 90, life_color):
            print("Vida abaixo de 90%, pressionando F3")
            pyautogui.press('F3')

        # Verificação da mana
        if pixel_matchs_color(mana_region, 90, mana_color):
            pyautogui.press('F3')
        elif not pixel_matchs_color(mana_region, 50, mana_color):
            print("Mana abaixo de 50%, pressionando F2")
            pyautogui.press('F2')
        
        time.sleep(1)  # Atraso para evitar chamadas excessivas

#def check_color(region, percent):
 #   result_percent = calcule_width(percent)  # Verificação da porcentagem baseada na cor
  #  x = region[0] + result_percent
   # y = region[1] + region[3]
    #print(pyautogui.pixel(x, y))

#keyboard.wait('h')
#check_color(mana_region, 100)

 #Teste da função
#keyboard.wait('h')  # Aguarda a tecla 'h' para iniciar
#event_th = threading.Event()
#test_thread = threading.Thread(target=manager_suplies, args=(event_th,))
#test_thread.start()

 #Deixe o teste rodar por 10 segundos
#time.sleep(10)
#event_th.set()  # Para a execução da função
#test_thread.join()  # Aguarda o término da thread
#print("Teste concluído.")