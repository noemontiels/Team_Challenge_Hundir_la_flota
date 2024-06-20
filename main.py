import numpy as np
import variables
import clases
import funciones

# Variables de la partida
player_lives = 20
pc_lives = 20
pc_shots = []
exit_game = False

# Inicio del juego
funciones.welcome()
variables.PLAYER_ID = funciones.player_name()

if variables.PLAYER_ID == 'exit':
    exit_game = True

# El juego se inicia y se ejecuta mientras el jugador no escriba 'exit' en algún imput
while exit_game == False:
    print('Dentro de while')
    break
    
  


print('\n¡Hasta pronto!')