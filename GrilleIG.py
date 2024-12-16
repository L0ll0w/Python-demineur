import pygame
import sys

# Settings
WIDTH, HEIGHT = 600, 600
GridSize = 60
CellSize = WIDTH / GridSize

# Colors

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# draw empty grid

def drawGrid(screen):
    for x in range(0, WIDTH, GridSize):
        for y in range(0, HEIGHT, GridSize):
            rect = pygame.Rect(x, y, GridSize, GridSize)
            pygame.draw.rect(screen, GRAY, rect)
            pygame.draw.rect(screen, BLACK, rect, 2)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Démineur")
    clock = pygame.time.Clock()

    running = True
    while running:
        screen.fill(WHITE)

        drawGrid(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


    #clique souris
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row = x // GridSize
            col = y // GridSize
            print(f"Clic sur la case ({row},{col})")

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
    sys.exit()

#lunchGame
main()