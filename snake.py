import consts
from cell import Cell


class Snake:

    dx = {'UP': 0, 'DOWN': 0, 'LEFT': -1, 'RIGHT': 1}
    dy = {'UP': -1, 'DOWN': 1, 'LEFT': 0, 'RIGHT': 0}

    def __init__(self, keys, game, pos, color, direction):
        self.keys = keys
        self.cells = [pos]
        self.game = game
        self.game.add_snake(self)
        self.color = color
        self.direction = direction
        game.get_cell(pos).set_color(color)

    def get_head(self):
        return self.cells[-1]

    def val(self, x):
        if x < 0:
            x += self.game.size

        if x >= self.game.size:
            x -= self.game.size

        return x

    def next_move(self):
        nx = self.get_head()[0] + self.dx[self.direction]
        ny = self.get_head()[1] + self.dy[self.direction]
        
        nx = self.val(nx)
        ny = self.val(ny)
        cell = self.game.get_cell((nx, ny))
        
        if not cell or (cell.color != consts.back_color and cell.color != consts.fruit_color):
            self.game.kill(self)
            return
        
        self.cells.append((nx, ny))
        
        if cell.color != consts.fruit_color:
            tail = self.cells.pop(0)
            self.game.get_cell(tail).set_color(consts.back_color)
        
        cell.set_color(self.color)

    
    def is_opposite(self, dir1, dir2):
        if dir1 == 'UP' and dir2 == 'DOWN':
            return True
        if dir1 == 'DOWN' and dir2 == 'UP':
            return True
        if dir1 == 'LEFT' and dir2 == 'RIGHT':
            return True
        if dir1 == 'RIGHT' and dir2 == 'LEFT':
            return True
        return False
            
            
            
    def handle(self, keys):
        for key in keys:
            if key in self.keys:
                new_direction = self.keys[key]
                current_direction = self.direction
                if not self.is_opposite(current_direction, new_direction):
                    self.direction = new_direction
                    break
