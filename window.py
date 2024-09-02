# Importa a biblioteca ctypes para interagir com a API do Windows
import ctypes
# Importa a biblioteca pygetwindow para obter informações sobre as janelas abertas
import pygetwindow as gw
import pyautogui  # Importa a biblioteca pyautogui para interagir com a interface gráfica
import win32gui  # Importa a biblioteca win32gui para obter informações sobre as janelas do Windows

GWL_EXSTYLE = -20  # Constante para obter o estilo estendido da janela
WS_EX_LAYERED = 0x00080000  # Constante para verificar se a janela é uma janela de camada (layered window)
LWA_ALPHA = 0x00000002  # Constante para definir a opacidade da janela

# Função para obter a opacidade atual de uma janela
def get_window_opacity(hwnd):
    ex_style = win32gui.GetWindowLong(hwnd, GWL_EXSTYLE)  # Obtém o estilo estendido da janela
    if ex_style & WS_EX_LAYERED:  # Verifica se a janela é uma janela de camada
        style = ctypes.c_ulong()
        opacity = ctypes.c_byte()
        ctypes.windll.user32.GetLayeredWindowAttributes(hwnd, None, ctypes.byref(opacity), ctypes.byref(style))  # Obtém a opacidade atual da janela
        return opacity.value
    else:
        return None  # Retorna None se a janela não for uma janela de camada

# Função principal para ocultar o cliente do Tibia
def hidden_client():
    windows = pyautogui.getAllWindows()  # Obtém todas as janelas abertas
    for window in windows:
        try:
            window_name = window.title.split('Tibia -')[1]  # Extrai o nome da janela do Tibia
            if window_name:
                WINDOW_TITLE = window.title  # Armazena o título da janela do Tibia
        except:
            continue

    try:
        target_window = [item for item in gw.getWindowsWithTitle(WINDOW_TITLE) if item.title == WINDOW_TITLE][0]  # Encontra a janela do Tibia
    except:
        pyautogui.alert(title="Hidden Client Tibia", text='Janela do Tibia não localizada')  # Exibe um alerta se a janela não for encontrada
        raise ValueError('Janela do Tibia não localizada')

    target_hwnd = target_window._hWnd  # Obtém o handle da janela do Tibia

    OPACITY = 255  # Define a opacidade desejada (255 = 100% opaco)
    current_opacity = get_window_opacity(target_hwnd)  # Obtém a opacidade atual da janela
    if current_opacity == -1:
        OPACITY = 1  # Define a opacidade para 1 se a janela não for uma janela de camada
    print('OPACITY', OPACITY)
    ex_style = ctypes.windll.user32.GetWindowLongA(target_hwnd, GWL_EXSTYLE)  # Obtém o estilo estendido da janela
    ctypes.windll.user32.SetWindowLongA(target_hwnd, GWL_EXSTYLE, ex_style | WS_EX_LAYERED)  # Define a janela como uma janela de camada
    ctypes.windll.user32.SetLayeredWindowAttributes(target_hwnd, 0, OPACITY, LWA_ALPHA)  # Define a opacidade da janela
    print("Opacidade da janela modificada.")
    if current_opacity is not None:
        print(f"Opacidade atual da janela: {current_opacity}")  # Exibe a opacidade atual da janela
    else:
        print("A janela não é uma janela de camada (layered window).")  # Mensagem se a janela não for uma janela de camada
    return OPACITY

# Chama a função principal para ocultar o cliente do Tibia
hidden_client()