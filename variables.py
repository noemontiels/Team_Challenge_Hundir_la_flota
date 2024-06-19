import numpy as np

'''
Constantes: se escriben en mayúsculas para diferenciarlas del resto de variables
- Id jugador
- Id pc
- Barcos: meterlos en un diccionario MIRAR NOMBRES DEL MENSAJE DE BIENVENIDA (funciones --> welcome())
    4 de 1 posición de eslora
    3 de 2 posiciones de eslora
    2 de 3 posiciones de eslora
    1 de 4 posiciones de eslora
- Array de tablero en blanco (dimensiones constantes)

Variables: Esto iría en main.py porque van cambiando durante el juego
- Tableros (jugador + pc)
- Registro de coordenadas de disparo (pc)
- Vidas restantes (start = 20)
'''

# CONSTANTES

# ID del jugador
PLAYER_ID = input('Introduzca su nombre: ') # ESTO NO SÉ SI SERÍA ASÍ
# ID máquina
PC_ID = 'player_pc'
# Dimensiones del tablero
BOARD_DIMENSION = 10
# Barcos
BOATS = {                             
    'A': ['A1'],
    'B': ['B1', 'B2'],
    'C': ['C1', 'C2', 'C3'],
    'D': ['D1', 'D2', 'D3', 'D4']
}
# Tablero vacío
EMPTY_BOARD = np.full((BOARD_DIMENSION, BOARD_DIMENSION), ' ')
