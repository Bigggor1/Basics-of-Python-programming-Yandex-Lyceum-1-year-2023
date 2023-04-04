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
            return True
        else:
            return False
    
    def set_position(self, row1, col1):
        if can_move(row1, col1):
            self.row = row1
            self.col = col1
    
    def char(self):
        return 'N'
    
    def get_color(self):
        return self.color


WHITE=1
BLACK=2

row0_W = 0
col0_W = 1
knight_W = Knight(row0_W, col0_W, WHITE)

row0_B = 7
col0_B = 6
knight_B = Knight(row0_B, col0_B, BLACK)

print('white' if knight_W.get_color() == WHITE else 'black')
print('white' if knight_B.get_color() == WHITE else 'black')
for row in range(7, -1, -1):
    for col in range(8):
        if (row0_W, col0_W) == (row, col):
            print(knight_W.char(), end='')
        elif (row0_B, col0_B) == (row, col):
            print(knight_B.char(), end='')
        elif knight_W.can_move(row, col) or knight_B.can_move(row, col):
            print('x', end='')
        else:
            print('-', end='')
    print()