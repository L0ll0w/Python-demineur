import pygame

# Dimensions de la grille
WIDTH, HEIGHT, GridSize = 600, 600, 60
CellCount = WIDTH // GridSize

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)

# Grille pour les drapeaux
flags = [[0] * CellCount for _ in range(CellCount)]


def draw_grid(screen):
    """
    Dessine la grille sur l'écran.
    """
    for x in range(0, WIDTH, GridSize):
        for y in range(0, HEIGHT, GridSize):
            rect = pygame.Rect(x, y, GridSize, GridSize)
            pygame.draw.rect(screen, GRAY, rect)
            pygame.draw.rect(screen, BLACK, rect, 2)