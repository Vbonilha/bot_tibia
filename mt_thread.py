import threading  # Importa a biblioteca threading para criar e gerenciar threads

# Classe que representa uma thread personalizada
class MyThread():
    def __init__(self, work):
        self.event = threading.Event()  # Cria um evento para controlar a execução da thread
        self.thread = threading.Thread()  # Inicializa a thread (ainda não associada a uma função)
        self.work = work  # Armazena a função de trabalho que a thread deve executar

    # Método para iniciar a thread
    def start(self):
        self.event.clear()  # Limpa o evento, permitindo que a thread execute
        self.thread = threading.Thread(target=self.run)  # Cria uma nova thread associada ao método run
        self.thread.start()  # Inicia a execução da thread

    # Método para parar a thread
    def stop(self):
        self.event.set()  # Sinaliza para a thread que ela deve parar
        self.thread.join()  # Aguarda a thread terminar sua execução

    # Método que contém o loop de execução da thread
    def run(self):
        while not self.event.is_set():  # Continua executando enquanto o evento não estiver sinalizado
            self.work()  # Chama a função de trabalho passada na inicialização


# Classe que representa um grupo de threads
class ThreadGroup:
    def __init__(self, list_threads):
        self.my_threads = list_threads  # Armazena a lista de threads

    # Método para iniciar todas as threads do grupo
    def start(self):
        for thread in self.my_threads:
            thread.start()  # Inicia cada thread no grupo

    # Método para parar todas as threads do grupo
    def stop(self):
        for thread in self.my_threads:
            thread.stop()  # Para cada thread no grupo
    