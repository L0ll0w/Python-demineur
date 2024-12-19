is_first_click = True
def first_case(row, col):
    """Repositionner les mines si la première case cliquée contient une mine."""
    global mines_positions
    if (row, col) in mines_positions:
        print(f"First click on the cell ({row}, {col}) contained a mine. Repositioning mines.")
        anciennes_mines = mines_positions.copy()
        mines_positions = sample([(i, j) for i in range(CellCount) for j in range(CellCount) if (i, j) != (row, col)], len(mines_positions))
        print(f"Old mines: {anciennes_mines}")
        print(f"New mines: {mines_positions}")



    def first_case(self, clicked_cells):
        mines_positions = self.grid.indice_mine()  # Retrieves the positions of the mines from the grid
        anciennes_mines = mines_positions.copy()  # Creates a copy of the original mine positions
        if self.is_first_click:
            for row in range(CellCount):
                for col in range(CellCount):
                    if clicked_cells[row][col] == 1 and (
                            row, col) in self.mines_positions:  # If a cell is clicked and contains a mine
                        self.mines_positions = sample([(i, j) for i in range(self.rows) for j in range(self.cols) if (i, j) != (row, col)],self.mines)  # Sets the new mine positions
                        self.is_first_click = False  # Sets the first click flag to False after the first click
                        print(f"First click on the cell ({row}, {col})")
                        print(f"Old mines: {anciennes_mines}")
                        print(f"New mines: {self.mines_positions}")
                        break
