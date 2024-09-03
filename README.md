# Tibia Bot

Este é um bot para o jogo Tibia como objeto de estudo, desenvolvido em Python. Ele automatiza tarefas como matar monstros, coletar loot, se movimentar pelo mapa e gerenciar suprimentos (vida e mana). E para poder utilizar ele é necessário antes de inicilizar o bot utilizar o arquivo do window.py que tem por objetivo retirar a opacidade do Client do jogo. Pois o tibia possui uma proteção que impede capturar imagens do client do jogo assim deixando a tela totalmente preta e para poder utilizar sem ter esse problema também é necessário baixar o obs.studio, criar uma fonte para captura de jogo e marcar o tibia, abrir um projetor em janela e também colocar o tibia em modo de compatibilidade com Windows 8, assim sendo possível pegar as imagens do jogo perfeitamente.

## Funcionalidades

- Mata monstros automaticamente enquanto estiver em batalha
- Coleta loot dos monstros derrotados
- Move-se pelo mapa seguindo marcações pré-definidas (cavebot)
- Gerencia suprimentos, recuperando vida e mana quando necessário
- Permite pausar e retomar a execução do bot a qualquer momento

- ## Requisitos

- Python 3.x
- Bibliotecas necessárias: `pyautogui`, `pynput`, `json`, `os`, `threading`, `ctypes`, `pygetwindow`, `win32gui`
- Gerenciador de pacotes pip: ```bash
pip install -r requirements.txt
- 

## Instalação

1. Certifique-se de ter o Python 3.x instalado em seu sistema.
2. Clone este repositório em sua máquina local.
3. Instale as bibliotecas necessárias usando o gerenciador de pacotes pip
4. Certifique-se de que o jogo Tibia esteja em execução e visível na tela.
5. Execute o arquivo main.py para iniciar o bot.

Uso
Pressione Delete para iniciar o bot.
Pressione Esc para pausar o bot.
O bot irá matar monstros, coletar loot, se movimentar pelo mapa e gerenciar suprimentos automaticamente.

Segue o vídeo do bot em funcionamento: https://youtu.be/I21aDElx7vk

Estrutura do Código
O código está dividido em três arquivos principais:

main.py: Contém a lógica principal do bot, incluindo as funções para matar monstros, coletar loot, se movimentar pelo mapa e gerenciar suprimentos. Também lida com o controle de execução do bot através de teclas de atalho.

actions.py: Contém funções específicas para realizar ações no jogo, como descer e subir buracos, comer comida, verificar se está em batalha e gerenciar suprimentos.

record.py: Responsável por capturar screenshots da tela e registrar as teclas pressionadas durante a execução. Essa funcionalidade é usada para criar um arquivo de configuração que guia o movimento do bot pelo mapa. Após usar o record.py foi criada a pasta Wasp_ab com as flags necessárias para rodar o cavebot com o arquivo infos.json, para criar uma nova pasta ou novo script basta trocar o nome do Folder name no arquivo constants.py 

mt_thread.py: Contém classes personalizadas para criar e gerenciar threads, permitindo que o bot execute tarefas em paralelo, como verificar vida e mana.

Na pasta imgs estão armazenadas recortes feitas pela ferramenta de captura do Windows e as mesmas foram utilizadas  para retornar a região com o parâmetro pg.locateOnScreen e essas regiões estão armanzeadas no arquivo constants.py.

Contribuição
Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

Licença
Este projeto está licenciado sob a MIT License.

