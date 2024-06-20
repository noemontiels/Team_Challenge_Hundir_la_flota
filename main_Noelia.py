import numpy as np
import variables
import clases
import funciones

# Cuerpo principal del juego
def main():
    
    # Inicio del juego
    funciones.welcome()
    variables.PLAYER_ID = funciones.player_name()

    # Inicializar los tableros
    PLAYER_BOARD = clases.Board(player_id = variables.PLAYER_ID)
    PC_BOARD = clases.Board(player_id = 'PC')

    # Variables de la partida
    player_lives = 20
    pc_lives = 20
    pc_shots = []

    # Si PLAYER_ID es distinto de 'exit', se inicia el juego
    while variables.PLAYER_ID != 'exit':
        print('Dentro de while')
        break
    
    # Bucle principal del juego
    player_turn = True
    while True:
        if player_turn:
            print('Tu tablero')
            funciones.print_board(PLAYER_BOARD, show_shots = True)
            print('Tablero del oponente')
            funciones.print_board(PC_BOARD, show_shots = True)

            action, x, y = funciones.get_shot_coordinates()
            if action == 'exit':
                print('Saliendo del juego...')
                break
            elif action == 'print'
            







print('\n¡Hasta pronto!')
