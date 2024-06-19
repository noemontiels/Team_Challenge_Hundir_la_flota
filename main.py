import numpy as np
import variables
import clases
import funciones

# Variables de la partida
pc_shots = []

# Inicio del juego
funciones.welcome()
variables.PLAYER_ID = funciones.player_name()

# Si PLAYER_ID es distinto de 'exit', se inicia el juego
while variables.PLAYER_ID != 'exit':
    print('Dentro de while')
    break


print('\n¡Hasta pronto!')