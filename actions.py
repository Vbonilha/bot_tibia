# Importa a biblioteca pyautogui para interagir com a interface gráfica e capturar imagens na tela
import pyautogui as pg
import constants  # Importa um módulo personalizado que contém constantes utilizadas no código
import pyautogui  # Importa novamente a biblioteca pyautogui (não é necessário, pode ser removido)
import time  # Importa a biblioteca time para manipulação de tempo e atrasos

# Função para mover para um buraco abaixo, se a condição for verdadeira
def hole_down(should_down):
    if should_down:
        print("Indo para o buraco para baixo...")
        box = pg.locateOnScreen('imgs/hole_down.PNG', confidence=0.85)  # Localiza a imagem do buraco para baixo na tela
        if box:
            print(f"Buraco para baixo encontrado: {box}")  # Exibe as coordenadas do buraco encontrado
            x, y = pg.center(box)  # Obtém as coordenadas centrais do buraco
            print(f"Movendo para as coordenadas: ({x}, {y})")
            pg.moveTo(x, y)
            print("Clicando no buraco para baixo...")
            pg.click()
            print("Esperando 5 segundos...")
            pg.sleep(5) 
            print("Concluído.")
        else:
            print("Buraco para baixo não encontrado.")  # Mensagem caso o buraco não seja encontrado
            
# Função para mover para um buraco acima, se a condição for verdadeira
def hole_up(should_up, img_anchor, plus_x, plus_y):
    if should_up:
        print("Indo para o buraco para cima...")
        box = pg.locateOnScreen(img_anchor, confidence=0.85)  # Localiza a imagem âncora na tela
        if box:
            print(f"Âncora encontrada: {box}")  # Exibe as coordenadas da âncora encontrada
            x, y = pg.center(box)  # Obtém as coordenadas centrais da âncora
            print(f"Movendo para as coordenadas: ({x + plus_x}, {y + plus_y})")
            pg.moveTo(x + plus_x, y + plus_y, 3)  # Move o cursor para as coordenadas ajustadas
            print("Pressionando F5...")
            pg.press('F5')
            print("Clicando no buraco para cima...")
            pg.click()
            print("Esperando 5 segundos...")
            pg.sleep(5) 
            print("Concluído.")
        else:
            print("Âncora não encontrada.")  # Mensagem caso a âncora não seja encontrada
            
# Função para pressionar a tecla F12 para comer, hotkey já configurada no tibia para isso.
def eat_food():
    print("Comendo food...")
    pg.press('F12')  

# Função para verificar se está em batalha, retornando none caso tenha monstros ou se estiver vazia retorna a posição do region Battle
def check_battle():
    return pg.locateOnScreen('imgs/region_battle.PNG', confidence=0.85, region=constants.region_battle) 

# Função para calcular a largura com base em uma porcentagem
def calcule_width(percent):
    return int(constants.width * percent / 100)  # Cálculo da porcentagem baseada na região do hp e mana 

# Função para verificar se a cor de um pixel em uma região específica corresponde a uma cor esperada
def pixel_matchs_color(region, percent, color):
    result_percent = calcule_width(percent)  # Calcula a largura correspondente à porcentagem
    x = region[0] + result_percent  # Calcula a posição x do pixel a ser verificado
    y = region[1] + region[3]  # Calcula a posição y do pixel a ser verificado
    return pyautogui.pixelMatchesColor(int(x), int(y), color, 10)  # Verifica se a cor do pixel corresponde à cor esperada com uma tolerância de 10

# Função para gerenciar suprimentos, verificando vida e mana e pressionando teclas conforme necessário
def manager_suplies(event):
    while not event.is_set():  # Continua enquanto o evento não for sinalizado
        # Verificação da vida
        if not pixel_matchs_color(constants.life_region, 50, constants.life_color):  # Verifica se a vida está abaixo de 50%
            print("Vida abaixo de 50%, pressionando F1")
            pyautogui.press('F1')  # Pressiona F1 para recuperar vida
        
        if not pixel_matchs_color(constants.life_region, 90, constants.life_color):  # Verifica se a vida está abaixo de 90%
            print("Vida abaixo de 90%, pressionando F3")
            pyautogui.press('F3')  # Pressiona F3 para recuperar mais vida

        # Verificação da mana
        if pixel_matchs_color(constants.mana_region, 90, constants.mana_color):  # Verifica se a mana está acima de 90%
            pyautogui.press('F3')  # Pressiona F3 para recuperar mana
        elif not pixel_matchs_color(constants.mana_region, 50, constants.mana_color):  # Verifica se a mana está abaixo de 50%
            print("Mana abaixo de 50%, pressionando F2")
            pyautogui.press('F2')  # Pressiona F2 para recuperar mana
        
        time.sleep(1)  # Atraso para evitar chamadas excessivas

# Função para verificar a presença de uma árvore na tela e interagir com ela
def check_arvore():
    box = pg.locateOnScreen('imgs/arvore.PNG', confidence=0.85)  # Localiza a imagem da árvore na tela
    if box:
        pg.moveTo(1894, 8)  # Move o cursor para a posição específica para fechar o client do jogo
        pg.click()  # Clica na posição
        pg.moveTo(1107, 549)  # Move o cursor para outra posição específica que é o exit para fechar o client e assim o personagem deslogar pois vão estar tentando matar ele para monstros
        pg.click()  # Clica na nova posição
        return False  # Retorna False se a árvore foi encontrada e clicada
    return True  # Retorna True se a árvore não foi encontrada