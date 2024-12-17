import pygame
from random import sample

pygame.init()
ecran = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
rows = 5
columns = 5

def afficher_tab(rows, columns, mines):
    tab = [[0 for _ in range(rows)] for _ in range(columns)]


    all_positions = [(i, j) for i in range(rows) for j in range(columns)]
    mine_positions = sample(all_positions, mines)

    for i, j in mine_positions:
        tab[i][j] = 'B'
    for rows in tab:
        print(' '.join(str(cell) for cell in rows))
    return tab




pygame.display.flip()


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)




continuer = True
pygame.display.flip()
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False
pygame.quit()






print(afficher_tab(5, 5, 2))
