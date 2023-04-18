def correct_coords(row, col):
    return 0 <= row < 8 and 0 <= col < 8


class Knight:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
    
    def can_move(self, row1, col1):
        if ((row1 == self.row + 1 and col1 == self.col + 2) 
           or (row1 == self.row + 1 and col1 == self.col - 2) 
           or (row1 == self.row - 1 and col1 == self.col + 2) 
           or (row1 == self.row - 1 and col1 == self.col - 2) 
           or (row1 == self.row + 2 and col1 == self.col + 1) 
           or (row1 == self.row + 2 and col1 == self.col - 1) 
           or (row1 == self.row - 2 and col1 == self.col + 1) 
           or (row1 == self.row - 2 and col1 == self.col - 1)):
            if correct_coords(row1, col1):
                return True
            else:
                return False
        else:
            return False
    
    def set_position(self, row1, col1):
        if self.can_move(row1, col1):
            self.row = row1
            self.col = col1
    
    def char(self):
        return 'N'
    
    def get_color(self):
        return self.color


WHITE=1
BLACK=2

row0 = 0
col0 = 1
knight = Knight(row0, col0, BLACK)

print('white' if knight.get_color() == WHITE else 'black')
for row in range(9, -3, -1):
    for col in range(-2, 10):
        if row == row0 and col == col0:
            print(knight.char(), end='')
        elif knight.can_move(row, col):
            print('x', end='')
        else:
            print('-', end='')
    print()