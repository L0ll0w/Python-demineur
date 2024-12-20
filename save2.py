import random

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
    random.seed(difficulty_name)  # Fixer la graine de génération pour chaque niveau

    mines_positions = grid.indice_mine()  # Charger les positions initiales des mines

    def first_case(row, col, mines_positions):
        """Si c'est le premier clic, reconfigurer les mines de manière déterminée"""
        if is_first_click:
            print(f"Premier clic à la cellule ({row}, {col}). Les mines vont être positionnées de manière cohérente.")
            random.seed(f"{row}{col}")  # Utilisation de la position du premier clic comme graine
            anciennes_mines = mines_positions.copy()
            # Générer les nouvelles positions des mines basées sur la graine
            mines_positions = sample(
                [(i, j) for i in range(CellCount) for j in range(CellCount) if (i, j) != (row, col)],
                len(mines_positions))  # Redistribution basée sur la graine
            print(f"Anciennes mines: {anciennes_mines}")
            print(f"Nouvelles mines: {mines_positions}")
            grid.grid = grid.rebuild_grid(mines_positions)  # Reconstituer la grille avec les nouvelles mines
        return mines_positions
