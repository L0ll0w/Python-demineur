import pygame
import sys
import csv
from grid import Grid
from random import sample

def start_game(w, h, mines, difficulty_name):
    grid = Grid((w, h, mines))

    # Dimensions de la grille et de la fenêtre
    GridSize = 60
    CellCount = w
    WIDTH = w * GridSize + 200  # Ajout pour marges
    HEIGHT = h * GridSize + 200

    # Position pour centrer la grille
    GRID_OFFSET_X = (WIDTH - w * GridSize) // 2
    GRID_OFFSET_Y = (HEIGHT - h * GridSize) // 2

    # Couleurs
    WHITE = (255, 255, 255)
    GRAY = (192, 192, 192)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    LIGHT_BLUE = (136, 162, 193)

    # Matrices pour drapeaux et cases cliquées
    flags = [[0] * CellCount for _ in range(CellCount)]
    clicked_cells = [[0] * CellCount for _ in range(CellCount)]

    # Initialisation de Pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Démineur")
    clock = pygame.time.Clock()

    # Fonts
    font = pygame.font.Font("font/Super Sense.ttf", 20)

    # Variables
    user_text = ""
    input_rect = pygame.Rect((WIDTH // 2) - 250, HEIGHT - 50, 500, 32)
    color_active = pygame.Color('lightskyblue3')

    # État du jeu
    game_screen = True
    running = True

    # Charger les images
    image_flag = pygame.image.load("image/redflag.png").convert_alpha()
    image_flag = pygame.transform.scale(image_flag, (GridSize, GridSize))
    image_bomb = pygame.image.load("image/bombFR.png").convert_alpha()
    image_bomb = pygame.transform.scale(image_bomb, (GridSize, GridSize))
    title_image = pygame.image.load("image/title.png").convert_alpha()
    title_resized = pygame.transform.scale(title_image, (600, 100))
    background_image = pygame.image.load("image/Sans_titre_275_20241219155549.png").convert()
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

    # Variables liées aux mines
    is_first_click = True  # Indique si c'est le premier clic
    mines_positions = grid.indice_mine()  # Charger les positions initiales des mines

    def draw_grid():
        """Dessiner la grille centrée sur l'écran."""
        for x in range(CellCount):
            for y in range(CellCount):
                rect_x = GRID_OFFSET_X + x * GridSize
                rect_y = GRID_OFFSET_Y + y * GridSize
                rect = pygame.Rect(rect_x, rect_y, GridSize, GridSize)
                pygame.draw.rect(screen, GRAY, rect)
                pygame.draw.rect(screen, BLACK, rect, 2)

    def reveal_cells(row, col):
        """Révéler récursivement les cellules adjacentes."""
        if row < 0 or row >= CellCount or col < 0 or col >= CellCount:
            return
        if clicked_cells[row][col] == 1 or (row, col) in mines_positions:
            return

        clicked_cells[row][col] = 1

        if grid.grid[row][col] > 0:
            return

        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for dr, dc in directions:
            reveal_cells(row + dr, col + dc)

    def check_victory():
        """Vérifier si toutes les cases non minées ont été révélées."""
        for row in range(CellCount):
            for col in range(CellCount):
                if (row, col) in mines_positions:
                    continue
                if clicked_cells[row][col] != 1:
                    return False
        return True

    def score():
        """Calculer le score basé sur les cases révélées."""
        return sum(sum(row) for row in clicked_cells)

    def first_case(row, col, mines_positions):
        if (row, col) in mines_positions:
            print(f"First click on the cell ({row}, {col}) contained a mine. Repositioning mines.")
            anciennes_mines = mines_positions.copy()
            mines_positions = sample(
                [(i, j) for i in range(CellCount) for j in range(CellCount) if (i, j) != (row, col)],
                len(mines_positions))
            print(f"Old mines: {anciennes_mines}")
            print(f"New mines: {mines_positions}")
            grid.grid = grid.rebuild_grid(mines_positions)  # Reconstruire la grille avec les nouvelles mines
        return mines_positions

    while running:
        if game_screen:
            # Dessiner l'image de fond
            screen.blit(background_image, (0, 0))

            # Dessiner le titre
            screen.blit(title_resized, ((WIDTH - 600) // 2, 20))

            # Dessiner la grille
            draw_grid()

            # Dessiner le contenu des cases
            for row in range(CellCount):
                for col in range(CellCount):
                    x, y = GRID_OFFSET_X + col * GridSize, GRID_OFFSET_Y + row * GridSize

                    if flags[row][col]:
                        screen.blit(image_flag, (x, y))
                    elif clicked_cells[row][col]:
                        value = grid.grid[row][col]
                        if value == -1:
                            screen.blit(image_bomb, (x, y))
                        elif value > 0:
                            pygame.draw.rect(screen, BLUE, pygame.Rect(x, y, GridSize, GridSize))
                            pygame.draw.rect(screen, BLACK, pygame.Rect(x, y, GridSize, GridSize), 2)
                            text = font.render(str(value), True, WHITE)
                            screen.blit(text, (x + GridSize // 3, y + GridSize // 4))
                        else:
                            pygame.draw.rect(screen, BLUE, pygame.Rect(x, y, GridSize, GridSize))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    col = (mouse_x - GRID_OFFSET_X) // GridSize
                    row = (mouse_y - GRID_OFFSET_Y) // GridSize

                    if 0 <= row < CellCount and 0 <= col < CellCount:
                        if event.button == 3:  # Clic droit
                            flags[row][col] = 1 - flags[row][col]
                        elif event.button == 1:  # Clic gauche
                            if is_first_click:
                                mines_positions = first_case(row, col, mines_positions)
                                is_first_click = False
                            if (row, col) in mines_positions:
                                print("Game Over")
                                for r, c in mines_positions:
                                    bomb_x = GRID_OFFSET_X + c * GridSize
                                    bomb_y = GRID_OFFSET_Y + r * GridSize
                                    screen.blit(image_bomb, (bomb_x, bomb_y))
                                pygame.display.flip()
                                running = False
                            else:
                                reveal_cells(row, col)

            if check_victory():
                print("Victory!")
                game_screen = False
                screen = pygame.display.set_mode((WIDTH, HEIGHT))

        else:
            # Code pour afficher l'écran de victoire et le score...
            pass

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()
