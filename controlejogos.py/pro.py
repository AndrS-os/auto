import pyautogui
import time

def controlar_jogo():
    """
    Função para controlar um jogo simples usando o teclado com PyAutoGUI.
    Este é um exemplo básico e precisará ser adaptado ao jogo específico.
    """
    try:
        print("O script vai começar em 5 segundos. Prepare a janela do jogo!")
        time.sleep(5)
        print("Iniciando o controle...")

        # pressionar teclas para movimentação (W, A, S, D)
        print("Pressionando 'W' (para cima) por 2 segundos...")
        pyautogui.keyDown('w')
        time.sleep(2)
        pyautogui.keyUp('w')

        print("Pressionando 'D' (para a direita) por 1 segundo...")
        pyautogui.keyDown('d')
        time.sleep(1)
        pyautogui.keyUp('d')

        print("Pressionando a barra de espaço (ação) uma vez...")
        pyautogui.press('space')
        time.sleep(0.5)

        print("Pressionando 'A' (para a esquerda) repetidamente...")
        for _ in range(3):
            pyautogui.press('a')
            time.sleep(0.2)

        # combinação de teclas (Shift para correr)
        print("Pressionando e segurando 'Shift' e depois 'W'...")
        pyautogui.keyDown('shift')
        pyautogui.keyDown('w')
        time.sleep(3)
        pyautogui.keyUp('w')
        pyautogui.keyUp('shift')

        print("Controle finalizado.")

    except KeyboardInterrupt:
        print("\nScript interrompido pelo usuário.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    controlar_jogo()

    
    
