# Team Challenge: Hundir la flota 🛳️💥

### ¡Bienvenido a [Hundir la flota](https://es.wikipedia.org/wiki/Batalla_naval_(juego))!
Este es un juego clásico de estrategia naval donde tu objetivo es hundir todos los barcos de tu oponente (la máquina) antes de que él hunda los tuyos.

## **Índice**   
1. [Descripción](#id1)
2. [Instalaciones previas](#id2)
3. [El tablero](#id3)
4. [Cómo jugar](#id4)
5. [Estructura del código](#id5)

## Descripción<a name="id1"></a>
### Reglas básicas
1. **Jugadores**: Es un juego de dos jugadores: la máquina y tú.
2. **Tablero**: Cada jugador tiene un tablero de 10 x 10 posiciones donde colocará sus barcos.
3. **Los barcos y su colocación**: Los barcos se colocan aleatoriamente en el tablero de cada jugador sin restricciones de espacio entre ellos.
   
    - 4 barcos de 1 posición de eslora
    - 3 barcos de 2 posiciones de eslora
    - 2 barcos de 3 posiciones de eslora
    - 1 barco de 4 posiciones de eslora
      
### Objetivo
El objetivo es hundir todos los barcos del oponente.

En cada turno, los jugadores se alternan para disparar al tablero del oponente. Si aciertas, sigues jugando. El juego termina cuando un jugador ha hundido todos los barcos del oponente.

## Instalaciones previas<a name="id2"></a>
### Prerrequisitos

- Tener instalado Python 3.x
- Tener instalado Numpy

## El tablero<a name="id3"></a>
El tablero consta de 10 columnas y 10 filas (1 - 10).

                    1 2 3 4 5 6 7 8 9 10
                    -------------------
                 1 |1                  |
                 2 |          2 2      |
                 3 |            1   2  |
                 4 |                2  |
                 5 |                   |
                 6 |                   |
                 7 |    3 3 3     4    |
                 8 |  3 3 3   1   4    |
                 9 |              4    |
                10 |  2 2         4   1|
                    -------------------

## Cómo jugar<a name="id4"></a>
1. Al iniciar el juego, se te pedirá que introduzcas tu nombre.
2. Los tableros de ambos jugadores se inicializan automáticamente con los barcos colocados aleatoriamente.
3. En tu turno, introduce las coordenadas para disparar en el formato 'x y'.
4. Si tu disparo ha impactado en un barco del oponente, te vuelve a tocar; si no, el turno pasa a tu contrincante.
5. El juego continuará hasta que uno de los jugadores haya hundido todos los barcos del oponente.
6. Puedes salir del juego con el comando 'exit'.

## Estructura del código<a name="id5"></a>
- **'main.py'**: controla el flujo principal del juego.
- **'funciones.py'**: contiene funciones auxiliares necesarias para el desarrollo del juego (dar la bienvenida, pedir coordenadas, mostrar tableros, etc).
- **'variables.py'**: define las constantes del juego.
