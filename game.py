import pygame
import sys
import csv
from random import sample
from grid import Grid


def start_game(w, h, mines, difficulty_name):
    from menu import Menu

    WIDTH = w * 60
    HEIGHT = h * 60
    GridSize = 60
    CellCount = w
    grid = Grid((w, h, mines))
    mines_positions = grid.indice_mine()

    WHITE = (255, 255, 255)
    GRAY = (192, 192, 192)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)

    flags = [[0] * CellCount for _ in range(CellCount)]
    clicked_cells = [[0] * CellCount for _ in range(CellCount)]

    menu = Menu()

    def draw_grid(screen):
        for x in range(0, WIDTH, GridSize):
            for y in range(0, HEIGHT, GridSize):
                rect = pygame.Rect(x, y, GridSize, GridSize)
                pygame.draw.rect(screen, GRAY, rect)
                pygame.draw.rect(screen, BLACK, rect, 2)

    def check_victory():
        for row in range(CellCount):
            for col in range(CellCount):
                if (row, col) in mines_positions:
                    continue
                if clicked_cells[row][col] != 1:
                    return False
        return True

    def reveal_cells(row, col):
        """
        Révéler les cellules adjacentes récursivement si elles n'ont pas de mines adjacentes.
        """
        # Vérifie les limites de la grille
        if row < 0 or row >= CellCount or col < 0 or col >= CellCount:
            return

        # Arrête la récursion si la case est déjà cliquée ou contient une mine
        if clicked_cells[row][col] == 1 or (row, col) in mines_positions:
            return

        # Révéler la case actuelle
        clicked_cells[row][col] = 1

        # Si la case a des mines adjacentes, on arrête ici
        if grid.grid[row][col] > 0:
            return

        # Révéler les cases adjacentes si aucune mine adjacente
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for dr, dc in directions:
            reveal_cells(row + dr, col + dc)

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Démineur")
    clock = pygame.time.Clock()

    image_flag = pygame.image.load("image/redflag.png").convert_alpha()
    image_flag = pygame.transform.scale(image_flag, (GridSize, GridSize))
    image_bomb = pygame.image.load("image/bombFR.png").convert_alpha()
    image_bomb = pygame.transform.scale(image_bomb, (GridSize, GridSize))

    game_screen = True
    running = True

    while running:
        if game_screen:
            screen.fill(WHITE)
            draw_grid(screen)

            font = pygame.font.Font("font/Super Sense.ttf", 20)

            # Dessiner les drapeaux et le contenu des cellules
            for row in range(CellCount):
                for col in range(CellCount):
                    if flags[row][col] == 1:
                        screen.blit(image_flag, (col * GridSize, row * GridSize))
                    elif clicked_cells[row][col] == 1:
                        value = grid.grid[row][col]
                        if value == -1:
                            screen.blit(image_bomb, (col * GridSize, row * GridSize))
                        elif value > 0:
                            pygame.draw.rect(screen, (BLUE), pygame.Rect(col * GridSize, row * GridSize, GridSize, GridSize)) 
                            pygame.draw.rect(screen, BLACK, pygame.Rect(col * GridSize, row * GridSize, GridSize, GridSize), 2)
                            text = font.render(str(value), True, (WHITE))
                            screen.blit(text, (col * GridSize + GridSize // 3, row * GridSize + GridSize // 4))
                        elif value == 0: 
                            pygame.draw.rect(screen, (BLUE), pygame.Rect(col * GridSize, row * GridSize, GridSize, GridSize))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    row, col = y // GridSize, x // GridSize

                    if event.button == 3:
                        flags[row][col] = 1 - flags[row][col]
                    elif event.button == 1:
                        if (row, col) in mines_positions:
                            print("Game Over")

                            for r, c in mines_positions:
                                screen.blit(image_bomb, (c * GridSize, r * GridSize))

                            pygame.display.flip()

                            running = False
                        else:
                            reveal_cells(row, col)

            if check_victory():
                print("Victory!")
                game_screen = False
                VICTORY_WIDTH = menu.screenw
                VICTORY_HEIGHT = menu.screenh
                screen = pygame.display.set_mode((VICTORY_WIDTH, VICTORY_HEIGHT))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()