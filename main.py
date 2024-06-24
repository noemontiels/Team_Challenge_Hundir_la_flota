import numpy as np
import variables
import clases
import funciones

# Game variables
player_lives = 20
pc_lives = 20
pc_shots = []
exit_game = False
player_board = clases.Board(variables.PLAYER_ID)
pc_board = clases.Board(variables.PC_ID)
player_turn = 'player' # pc
succesful_shot = False

# Game initialization
funciones.welcome()
variables.PLAYER_ID = funciones.player_name()

if variables.PLAYER_ID == 'exit':
    exit_game = True

# The game starts. It will end if the player writes 'exit' in any input
while exit_game == False:
    if player_turn == 'player':
        print('Tu tablero')
        player_board.print_board(reveal_ships = True)
        print('Tablero oponente')
        pc_board.print_board(reveal_ships = False)
        
        coordinates = funciones.get_shot_coordinates()
        # funciones.shoot(coordinates)
        
        # mensaje de si has tocado/hundido
        # succesful_shot True o False
        if succesful_shot == True:
            pc_lives = pc_lives - 1
            if pc_board.all_ships_sunk() == True:
                print('¡Has ganado!')
                break  # probar return
            else:
                continue
        else:
            player_turn = 'pc'
            continue
        
    else:
        print('Tu tablero')
        player_board.print_board(reveal_ships = True)
        print('Tablero oponente')
        pc_board.print_board(reveal_ships = False)
        
        funciones.generate_shot()
        # mensaje de si has tocado/hundido
        # succesful_shot 
        if succesful_shot == True:
            player_lives = player_lives - 1
            if player_board.all_ships_sunk():
                print('¡Has perdido!')
                break # probar return
            else:
                continue
        else:
            player_turn = 'player'
            continue
        

print('\n¡Hasta pronto!')