from math import ceil

from settings import Settings

class Mine_matrix():
    def __init__(self) -> None:
        self.matrix = self.generate_matrix()
        self.mines_number = self.get_mines_number()
        
        print(self.matrix)
        
    
    def generate_matrix(self):
        matrix = []
        for i in range(Settings.size_y):
            row = []
            for j in range(Settings.size_x):
                row.append(0)
            matrix.append(row)
        return matrix
    
    
    def get_mines_number(self):
        matrix_size = Settings.size_x * Settings.size_y
        return ceil(matrix_size * Settings.mines_ratio)