# Importa a biblioteca pyautogui para interagir com a interface gráfica
import pyautogui as pg
import pyautogui  # Importa novamente a biblioteca pyautogui (não é necessário, pode ser removido)
pyautogui.ImageNotFoundException(False)  # Desativa a exceção de imagem não encontrada
pg.ImageNotFoundException(False)  # Desativa a exceção de imagem não encontrada
import actions  # Importa o módulo actions que contém funções relacionadas a ações do bot
import constants  # Importa o módulo constants que contém constantes utilizadas no código
import json  # Importa a biblioteca json para manipulação de dados em formato JSON
from pynput.keyboard import Listener  # Importa o Listener para monitorar eventos de teclado
from pynput import keyboard  # Importa a classe keyboard para acessar as teclas
import threading  # Importa a biblioteca threading para criar e gerenciar threads
import mt_thread  # Importa um módulo personalizado para gerenciar grupos de threads

def kill_monster():        
    while actions.check_battle() == None:# Enquanto o region battle estiver com monstros aparecendo ele irá retornar none e assim dando sequência aos comandos de ataque.
        if event_th.is_set():  # Condição para cortar a execução dentro do looping
            return
        print('Matando monstros')
        pg.press('space')# Atalho configurado para entrar em combate e pegar um alvo ao ser pressionada.
        while pg.locateOnScreen('imgs/red_target.PNG', confidence=0.9, region=constants.region_battle) != None:  #Para manter o target(alvo) ao entrar em batalha, sem esse while o personagem fica apertando espaço e não mantem o foco em um unico alvo especifico.
            if event_th.is_set():
                return
            print('Esperando o monstro morrer.')
        print('Procurando outro monstro.')

def get_loot():
    pg.press('q')    #O tibia agora possui uma função de autoloot que pode ser configurado em qualquer hotkey

def go_to_flag(path, wait):  # função criada para garantir que ele vai clicar somente no mini mapa para o cavebot
    flag = pg.locateOnScreen(path, confidence=0.8, region=constants.region_mini_map)#Localiza as marcações na região do mini mapa
    if flag:
        x, y = pg.center(flag)
        if event_th.is_set():
            return
        pg.moveTo(x, y)
        pg.click() 
        pg.sleep(wait)

def check_player_position(): # Essa função serve para verificar se o personagem chegou na flag, caso não ele reinicia o looping do run, caso ele ache a img que está com o ponto do personagem no mini mapa.
    return pg.locateOnScreen('imgs/point_player.PNG', confidence=0.80, region=constants.region_mini_map)

def run():
    with open(f'{constants.FOLDER_NAME}/infos.json', 'r') as file:  # Rodando as marcações do record em ordem
        data = json.loads(file.read())
    print('data', data[0])
    while not event_th.is_set():
        for item in data:  # Pegando as funções do cavebot
            if not actions.check_arvore():
                return
            if event_th.is_set():  # Condição para cortar a execução dentro do looping
                return
            kill_monster()
            if event_th.is_set():
                return
            pg.sleep(1)
            get_loot()
            if event_th.is_set():
                return
            go_to_flag(item['path'], item['wait']) # Move para a bandeira
            if event_th.is_set():
                return
            if check_player_position(): # Verifica se o jogador chegou à bandeira
                kill_monster()  # Repetindo as funções por conta de ter algum monstro trapando(impedindo do personagem chegar a flag que foi clickada na região do mini mapa).
                if event_th.is_set():
                    return
                pg.sleep(1)
                get_loot()
                if event_th.is_set():
                    return
                go_to_flag(item['path'], item['wait'])
            actions.eat_food()
            actions.hole_down(item['down_hole'])
            actions.hole_up(item['up_hole'], f'{constants.FOLDER_NAME}/anchor_floor_2.PNG', 423, 0) # Ancoras(imagens recortadas proximas aos locais que o boneco tem que subir) para evitar problemas caso tenha algum bixo morto em cima das posições de subir com a posição exata do local que é para subir
            actions.hole_up(item['up_hole'], f'{constants.FOLDER_NAME}/anchor_floor_3.PNG', 130, 130)

# Função para lidar com as teclas pressionadas
def key_code(key, th_group):
    if key == keyboard.Key.esc: # Se a tecla Esc for pressionada
        event_th.set()  # Sinaliza para pausar o bot
        th_group.stop() # Para o grupo de threads
        return False
    if key == keyboard.Key.delete:  # iniciar o bot
        th_run.start() # Inicia a thread do bot
        th_group.start() # Inicia o grupo de threads

global event_th  # Variável global para controle de eventos
event_th = threading.Event() # Cria um evento para controle de execução
th_run = threading.Thread(target=run)  # Cria uma thread para executar a função run, como se fosse outro terminal

#threads para verificar o hp e a mana e ser possivel pausar a qualquer momento
th_full_mana = threading.Thread(target=actions.manager_suplies, args=(event_th,))
th_hp_check = threading.Thread(target=actions.manager_suplies, args=(event_th,))  

# Agrupa as threads para gerenciamento
group_thread = mt_thread.ThreadGroup([th_full_mana, th_hp_check])

# Inicia o listener de teclado para monitorar as teclas pressionadas
with Listener(on_press=lambda key: key_code(key, group_thread)) as listener:
    listener.join() # Aguarda eventos de teclado
         

