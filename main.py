import clases
import funciones
import numpy as np
import time
import variables

# Game variables
exit_game = False
turn = 'player'
succesful_shot = False

# Player variables
player_lives = sum(variables.SHIPS.values())
player_board = clases.Board(variables.PLAYER_ID, variables.BOARD_SIZE, variables.SHIPS)

# PC variables
pc_lives = sum(variables.SHIPS.values())
pc_shots = []
pc_board = clases.Board(variables.PC_ID, variables.BOARD_SIZE, variables.SHIPS)


# Game initialization
funciones.welcome()
player_id = funciones.player_name()

if player_id == 'exit':
    exit_game = True

# The game starts. It will end if the player writes 'exit' in any input
while exit_game == False:
    if turn == 'player':
        print('Tu tablero')
        player_board.print_board(reveal_ships = True)
        
        print('Tablero oponente')
        pc_board.print_board(reveal_ships = False)
        
        coordinates = funciones.get_shot_coordinates()
        if coordinates == ():
            # exit_game = True
            break
        
        shot_result = funciones.shoot(player_board, pc_board, coordinates)
        succesful_shot = shot_result[2]
        
        if succesful_shot == True:
            print('¡Has tocado!')
            print(pc_board)
            pc_lives -= 1
            if pc_lives == 0:
                print('¡Has ganado!')
                break
            else:
                time.sleep(.5)
                continue
        else:
            print('¡Agua!')
            turn = 'pc'
            time.sleep(.5)
            continue
        
    else:
        print('Tu tablero')
        player_board.print_board(reveal_ships = True)
        print('Tablero oponente')
        pc_board.print_board(reveal_ships = False)
        
        pc_shots, coordinates = funciones.generate_shot(pc_shots)
        shot_result = funciones.shoot(player_board, pc_board, coordinates)
        succesful_shot = shot_result[2]
        # mensaje de si has tocado/hundido
        # succesful_shot 
        if succesful_shot == True:
            player_lives -= 1
            if player_lives == 0:
                print('¡Has perdido!')
                break # probar return
            else:
                continue
        else:
            turn = 'player'
            continue
        

print('\n¡Hasta pronto!')