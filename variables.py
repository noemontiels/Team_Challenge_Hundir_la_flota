import numpy as np

'''
Constantes: se escriben en mayúsculas por ser variables que no cambian, para diferenciarlas del resto de variables que sí se modifican durante el juego
- Id jugador
- Id pc
- Barcos: meterlos en un diccionario MIRAR NOMBRES DEL MENSAJE DE BIENVENIDA (funciones --> welcome())
    4 de 1 posición de eslora
    3 de 2 posiciones de eslora
    2 de 3 posiciones de eslora
    1 de 4 posiciones de eslora
- Array de tablero en blanco (dimensiones constantes)

Variables: Esto iría en main.py porque van cambiando durante el juego, sus nombres van en minúscula
- Tableros (jugador + pc)
- Registro de coordenadas de disparo (pc)
- Vidas restantes (start = 20)
'''

# CONSTANTES

# ID del jugador, inicio con nombre predeterminado modificable por el jugador al inicio de la partida
PLAYER_ID = 'human_player'

# ID máquina
PC_ID = 'pc_player'

# Dimensiones del tablero
BOARD_SIZE = 10

# Barcos
SHIPS = {
    'A1': 4,
    'B1': 3,
    'B2': 3,
    'C1': 2,
    'C2': 2,
    'C3': 2,
    'D1': 1,
    'D2': 1,
    'D3': 1,
    'D4': 1
}