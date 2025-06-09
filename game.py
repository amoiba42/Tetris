from grid import Grid                                                                       # type: ignore
from blocks import *                                                                        # type: ignore
import random

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), TBlock(), ZBlock(), SBlock()] # type: ignore
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()                                             
        self.game_over = False
        self.score = 0
    
    
    def update_score(self, lines_cleared,move_down_points):
        if lines_cleared==1:
            self.score+=100
        elif lines_cleared==2:
            self.score+=300
        elif lines_cleared==3:
            self.score+=500
        elif lines_cleared==4:
            self.score+=800
        self.score+=move_down_points
        
    def rotate(self):
        self.current_block.rotate_block()
        if not self.block_inside():
            self.current_block.rotate_block()
            self.current_block.rotate_block()
            self.current_block.rotate_block() 
        
    def move_left(self):
        self.current_block.move(0, -1)
        if not self.block_inside():
            self.current_block.move(0, 1)
        
    def move_right(self):
        self.current_block.move(0, 1)
        if not self.block_inside():
            self.current_block.move(0, -1)
        
    def move_down(self):
        self.current_block.move(1, 0)
        if not self.block_inside():
            self.current_block.move(-1, 0)
            self.lock_block()
            
    def lock_block(self):
        tiles=self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column]=self.current_block.id
        self.next_block=self.get_random_block()
        self.current_block=self.next_block
        rows_cleared=self.grid.clear_full_row()
        self.update_score(rows_cleared,0)
        
        if self.block_inside()==False:
            self.game_over=True
         
    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_inside(tile.row, tile.column) or not self.grid.is_empty(tile.row,tile.column):
                return False
        return True
     
    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), TBlock(), ZBlock(), SBlock()] # type: ignore
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def draw(self, screen):
        self.grid.draw_grid(screen)
        self.current_block.draw(screen,12,12)
        self.next_block.draw(screen, 400, 400)

    def reset(self):
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), TBlock(), ZBlock(), SBlock()] # type: ignore
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score=0

        