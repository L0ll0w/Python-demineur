class Grid:
    def __init__(self, config):
        self.width, self.height, self.mines = config
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]

    def indice_mine(self):
        # Place the mines and return their positions
        from random import sample
        mine_pos = sample(
            [(row, col) for row in range(self.height) for col in range(self.width)],
            self.mines
        )
        for row, col in mine_pos:
            self.grid[row][col] = -1  # Mark mine position

        # Calculate adjacent mines for all the grid
        self.calc_adjc_mines()
        return mine_pos
    
    def calc_adjc_mines(self):

        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] == -1:
                    continue

                adjc_mines = 0
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if 0 <= new_row < self.height and 0 <= new_col < self.width:
                        if self.grid[new_row][new_col] == -1: # Checking if mine
                            adjc_mines += 1
                self.grid[row][col] = adjc_mines
