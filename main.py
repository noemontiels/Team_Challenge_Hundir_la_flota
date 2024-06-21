import numpy as np
import variables
import clases
import funciones

# Game variables
player_lives = 20
pc_lives = 20
pc_shots = []
exit_game = False

# Game initialization
funciones.welcome()
variables.PLAYER_ID = funciones.player_name()

if variables.PLAYER_ID == 'exit':
    exit_game = True

# The game starts. It will end if the player writes 'exit' in any input
while exit_game == False:
    print('Dentro de while')
    break
    
  


print('\n¡Hasta pronto!')