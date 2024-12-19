class Grid:
    def __init__(self, config):
        self.width, self.height, self.mines = config
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]

    def indice_mine(self):
        # Place the mines and return their positions
        from random import sample
        mine_positions = sample(
            [(row, col) for row in range(self.height) for col in range(self.width)],
            self.mines
        )
        for row, col in mine_positions:
            self.grid[row][col] = -1  # Mark mine position
        return mine_positions
