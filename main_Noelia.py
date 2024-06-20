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
    PLAYER_BOARD = board(PLAYER_ID)

# Variables de la partida
pc_shots = []




# Si PLAYER_ID es distinto de 'exit', se inicia el juego
while variables.PLAYER_ID != 'exit':
    print('Dentro de while')
    break


print('\n¡Hasta pronto!')
