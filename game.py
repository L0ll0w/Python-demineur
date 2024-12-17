import pygame
from grid import Grid
import sys

def start_game(w, h, mines):
    WIDTH = w * 40
    HEIGHT = h * 40
    GridSize = 40
    CellCount = w

    grid = Grid(h, w, mines)
    mines_positions = grid.indice_mine()

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (192, 192, 192)

    flags = [[0] * CellCount for _ in range(CellCount)]

    def draw_grid(screen):
        for x in range(0, WIDTH, GridSize):
            for y in range(0, HEIGHT, GridSize):
                rect = pygame.Rect(x, y, GridSize, GridSize)
                pygame.draw.rect(screen, GRAY, rect)
                pygame.draw.rect(screen, BLACK, rect, 2)

    def main_game():
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Démineur")
        clock = pygame.time.Clock()

        running = True
        while running:
            screen.fill(WHITE)
            draw_grid(screen)

            for row in range(CellCount):
                for col in range(CellCount):
                    if flags[row][col] == 1:
                        rect = pygame.Rect(col * GridSize, row * GridSize, GridSize, GridSize)
                        pygame.draw.rect(screen, (255, 0, 0), rect)

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
                            print(f"Bombe détectée à ({row}, {col})!")
                            running = False

            pygame.display.flip()
            clock.tick(10)

        pygame.quit()
        sys.exit()

    main_game()