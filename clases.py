# Recomendable tener una clase barco
import numpy as np
import random
import variables

# Variables: 
board_size = variables.BOARD_SIZE
ships = variables.SHIPS

class Board:
    '''Defines the class as Board
    '''
    def __init__(self, player_id):  # initializes instances of 'Board' class
        self.player_id = player_id  # A way to store the ID of player or computer
        self.size = board_size  # Sets the board size. This could be a good variable to store in the variables script
        self.ships = ships  # Ship lengths stored as values in a dictionary, also in variables script
        self.board = np.full((self.size, self.size), '~')   # creates the actual board in whatever size is stores in 'size' variable (10)
        self.shots_board = np.full((self.size, self.size), '~') # creates the second board for tracking where you have fired
        self.ship_positions = []    # Stores the positions of the ships as tuples
        self.lives = sum(self.ships.values()) # idea here is to make a way to track when all of the ships have been destroyed (not sure this will work??)
        self.generate_ships()  # calls the first method (which chain calls the others to place ships on the board)

    def generate_ships(self):
        for length in self.ships.values():  # for loop iterates over the ship lengths in the SHIPS dictionary
            placed = False  # initiates the coordinates as False
            while not placed:
                x, y = random.randint(0, self.size -1), random.randint(0, self.size -1) # generates an (x, y) set of coordinates using random
                orientation = random.choice(['H', 'V']) # randomly selects if the orientation will be horiz or verti
                if self.check_position(x, y, length, orientation): # calls the next method to check if ship can be placed on the board
                    self.place_ships(x, y, length, orientation) # calls method to place the ships on the board
                    placed = True   # if position is good, placed is set to True

    def check_position(self, x, y, length, orientation):
        if orientation == 'H':
            if y + length > self.size:  # checks if length of ship is valid and fits within the board
                return False
            return all(self.board[x, y + i] == '~' for i in range(length))  # checks that all spaces within the ship's length are empty (e.g. contain '~')
        else:   # same check but in vertical orientation
            if x + length > self.size: 
                return False
            return all(self.board[x + i, y] == '~' for i in range(length))
        
    def place_ships(self, x, y, length, orientation):   # actually places the ships on the board
        if orientation =='H':
            for i in range(length):
                self.board[x, y + i] = 'S'   # places horizontal ship on the board
                self.ship_positions.append((x, y, + i))  # updates coordinates of the ship in the ship_positions list
        else:   # does same for the vertical ships
            for i in range(length):
                self.board[x + i, y] = 'S'
                self.ship_positions.append((x + i, y))

    def all_ships_sunk(self):
        return self.total_lives == 0

    def print_board(self, reveal_ships = False):
        if reveal_ships:    # prints board with ships
            for row in self.board:
                print(" ".join(row))
        else:   # prints board without ships
            for row in self.shots_board:
                print(" ".join(row))