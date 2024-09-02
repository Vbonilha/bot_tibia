# Importa a biblioteca pyautogui para capturar screenshots e interagir com a interface gráfica
import pyautogui as pg
# Importa o Listener da biblioteca pynput para monitorar eventos de teclado
from pynput.keyboard import Listener
from pynput import keyboard  # Importa a classe keyboard para acessar as teclas
import json  # Importa a biblioteca json para manipulação de dados em formato JSON
import os  # Importa a biblioteca os para interações com o sistema de arquivos (criação, movimentação e deleção de arquivos)
import constants  # Importa um módulo personalizado que contém constantes, como o nome da pasta para armazenar screenshots

# Função para criar uma pasta se ela não existir
def create_folder():
    if not os.path.isdir(constants.FOLDER_NAME):
        os.mkdir(constants.FOLDER_NAME)

# Classe principal para gerenciar a gravação de screenshots e teclas pressionadas
class Rec:
    def __init__(self):
        # Chama a função create_folder para garantir que a pasta de armazenamento exista
        create_folder()  
        self.count = 0  # Inicializa um contador para nomes de arquivos de screenshot
        self.coordinates = []  # Inicializa uma lista para armazenar informações sobre as coordenadas dos screenshots

    # Função para tirar um screenshot da região em torno do cursor do mouse
    def photo(self):
        x, y = pg.position()  # Obtém a posição atual do cursor do mouse
        photo = pg.screenshot(region=(x - 3, y - 3, 6, 6))  # Captura uma região de 6x6 pixels em torno do cursor
        path = f'{constants.FOLDER_NAME}/flag_{self.count}.PNG'  # Define o caminho do arquivo para salvar a screenshot
        photo.save(path)  # Salva a screenshot no caminho especificado
        self.count += 1  # Incrementa o contador para o próximo nome de arquivo
        infos = {
            "path": path,  # Armazena o caminho da screenshot
            "down_hole": 0,  # Inicializa o marcador de descida de buraco
            "up_hole": 0,  # Inicializa o marcador de subida de buraco
            "wait": 15  # Define um tempo de espera padrão
        }
        self.coordinates.append(infos)  # Adiciona as informações da screenshot à lista de coordenadas

    # Função para lidar com as teclas pressionadas
    def key_code(self, key):
        if key == keyboard.Key.esc:  # Cancela o listener se a tecla Esc for pressionada
            with open(f'{constants.FOLDER_NAME}/infos.json', 'w') as file:
                file.write(json.dumps(self.coordinates))  # Salva as coordenadas em um arquivo JSON
            return False  # Interrompe o listener
        print('key', key)  # Exibe a tecla pressionada no console
        if key == keyboard.Key.insert:  # Tira um screenshot se a tecla Insert for pressionada
            self.photo()
        if key == keyboard.Key.page_down:  # Marca a necessidade de descer um buraco se a tecla Page Down for pressionada
            self.down_hole()
        if key == keyboard.Key.page_up:  # Marca a necessidade de subir um buraco se a tecla Page Up for pressionada
            self.up_hole()

    # Função para iniciar o listener de teclas
    def start(self):
        with Listener(on_press=self.key_code) as listener:
            listener.join()  # Aguarda eventos de teclado

    # Função para marcar a necessidade de descer um buraco
    def down_hole(self):
        last_coordinates = self.coordinates[-1]  # Obtém as informações da última screenshot
        last_coordinates['down_hole'] = 1  # Marca que houve uma descida de buraco

    # Função para marcar a necessidade de subir um buraco
    def up_hole(self):
        last_coordinates = self.coordinates[-1]  # Obtém as informações da última screenshot
        last_coordinates['up_hole'] = 1  # Marca que houve uma subida de buraco

# Cria uma instância da classe Rec e inicia o listener de teclas
record = Rec()
record.start()