from math import ceil
from random import randint

from settings import Settings

class Mine_matrix():
    def __init__(self) -> None:
        self.number_of_mines = self.get_number_of_mines()
        
        self.matrix = self.generate_empty_matrix()
        self.generate_matrix()
        
        
    
    def generate_matrix(self):
        # self.matrix = self.generate_empty_matrix()
        self.place_mines()
        self.place_numbers_on_cells()
    
    
    def generate_empty_matrix(self):
        matrix = []
        for i in range(Settings.size_y):
            row = []
            for j in range(Settings.size_x):
                row.append(0)
            matrix.append(row)
        return matrix
        
    
    def place_mines(self):
        m = 0
        while m <= self.number_of_mines:
            x = randint(0, Settings.size_x - 1)
            y = randint(0, Settings.size_y - 1)
            
            if self.matrix[y][x] != 0:
                continue
            
            # value -1 mean that here is mine (bomb)
            self.matrix[y][x] = -1
            m += 1
    
    
    def get_neighbour_dictionary(self, position):
        neighbor_dictionary = {'row': {'min': -1, 'max': 1},
                           'col': {'min': -1, 'max': 1}}
        # rows
        if position[0] <= 0:
            neighbor_dictionary['row']['min'] = 0
        if position[0] >= len(self.matrix) - 1:
            neighbor_dictionary['row']['max'] = 0
        # columns
        if position[1] <= 0:
            neighbor_dictionary['col']['min'] = 0
        if position[1] >= len(self.matrix[0]) - 1:
            neighbor_dictionary['col']['max'] = 0
        return neighbor_dictionary
    
    
    def add_number_to_neighbor(self, position):
        if self.matrix[position[0]][position[1]] >= 0:
            self.matrix[position[0]][position[1]] += 1
    
    
    def walk_throu_neghbors(self, position, neighbors):
        for neighbor_row in range(position[0] + neighbors['row']['min'], position[0] + neighbors['row']['max'] + 1):
            for neighbor_col in range(position[1] + neighbors['col']['min'], position[1] + neighbors['col']['max'] + 1):
                # print(neighbor_row, neighbor_col)
                print(neighbor_row, neighbor_col)
                self.add_number_to_neighbor([neighbor_row, neighbor_col])
    
    
    def place_numbers_on_cells(self):
        for i, row in enumerate(self.matrix):
            for j, cell in enumerate(row):
                if cell == -1:
                    neighbors = self.get_neighbour_dictionary([i, j])
                    print(f'bomb is at position {i}, {j}')
                    print(f'{neighbors}')
                    self.walk_throu_neghbors(position=[i, j], neighbors=neighbors)
    
    
    def get_number_of_mines(self):
        matrix_size = Settings.size_x * Settings.size_y
        return ceil(matrix_size * Settings.mines_ratio)