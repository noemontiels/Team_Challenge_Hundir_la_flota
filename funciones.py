import numpy as np
import random
import variables
import main

'''
- Colocar barco
- Pedir coordenadas si jugador humano
- Marcar tablero
- Mostrar tablero actualizado después del disparo (los 2 tableros)
- Determinar si se ha tocado / hundido un barco
- Determinar turno: si ha tocado continua el mismo jugador, si no, pasa al otro
- Fin del juego si todos los barcos de un jugador están hundidos
- Salida del juego voluntaria
- Verificar que coordenadas están en el tablero
- Verifcar que pc no dispara 2 veces al mismo sitio
- Mostrar tablero (reveal_ship): cada jugador tiene 2, uno donde tiene sus barcos colocados y otro donde dispara. Solo se muestra el tablero de los disparos
- Vidas restantes (start = 20 porque hay 20 posiciones del tablero ocupadas por barcos al inicio de la partida)
'''

def welcome():
    # Imprime mensaje de bienvenida con las instrucciones del juego.
    print(f'{'_'*100}\n\n¡Bienvenido a Battleship: Golden Hind Edition!\n\n' \
        'Cómo jugar:\n'\
        '   1. Introduzca su nombre de jugador para iniciar la partida.\n'\
        '   2. Introduzca la posición de sus barcos en el tablero de sus barcos en el tablero mediante coordenadas (X,Y) y orientación (N, E, S, W)\n'\
        '      Los barcos a colocar son, en este orden:\n'\
        '       - A1: 4 posiciones de eslora.\n'\
        '       - B1 y B2: 3 posiciones de eslora.\n'\
        '       - C1, C2 y C3: 2 posiciones de eslora.\n'\
        '       - D1, D2, D3 y D4: 1 posición de eslora.\n'\
        '   3. El primer turno es suyo, introducza las coordenadas de disparo. Si acierta, continúa jugando, sino el turno pasa a la máquina.\n'\
        '   4. El juego finaliza cuando todos sus barcos o los de la máquina están hundidos.\n\n'\
        'Puede salir del juego escribiendo "exit" en cualquier input.\n\n'\
        f'¡Buena suerte!\n{'_'*100}\n')


def player_name():
    # Solicita el nombre del jugador.
    return input('Introduzca su nombre: ')


def player_is_human(player):
    # Devuelve True si el argumento player coincide con la constante que guarda el nombre del jugador.
    return player == variables.PLAYER_ID

    
def get_shot_coordinates():
    '''
    - Solicita al jugador las coordenadas de disparo sin tener en cuenta las coordinadas de los disparos previos.
    - Asegura que el valor introducido sea tipo int para la fila (row) y para la columna (col).
    - Asegura que el valor introducido está dentro del rango permitido. 
    '''
    coordinates = []
    for i in range(2):
        coordinate = int(float(input(f'{'Fila' if i == 0 else 'Columna'} del disparo (1-10): '))) - 1
        if coordinate > 9:
            print('¡La coordenada introducida están fuera del tablero!')
            return get_shot_coordinates()
        else:
            coordinates.append(coordinate)
    return coordinates

def generate_shot():
    # Genera de forma aleatoria las coordenadas del disparo que realiza la máquina.
    # FALTA ACTUALIZAR EL LISTADO DE DISPAROS REALIZADO POR LA MÁQUINA
    # main.pc_shots
    shot = np.random.randint(0, 9, (2,))
    return shot