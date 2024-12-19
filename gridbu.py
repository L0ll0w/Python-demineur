import pygame
import sys
from random import sample


class Grid:
    def __init__(self, niveau, rows, cols, mines):
        self.niveau = niveau
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.tableau = self.creer_tableau()

    def creer_tableau(self):
        tableau = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        mines_positions = sample([(i, j) for i in range(self.rows) for j in range(self.cols)], self.mines)
        for i, j in mines_positions:
            tableau[i][j] = 'B'
        return tableau

    def afficher_tableau(self):
        for ligne in self.tableau:
            print(' '.join(str(cell) for cell in ligne))

    def indice_mine(self):
        tab = []
        for i in range(self.rows):
            for j in range(self.cols):
                if self.tableau[i][j] == 'B':
                    tab.append((i, j))
        print(f"Position mines : {tab}")
        return tab



class Game:
    def __init__(self):
        self.grid = None

    def demarrer(self, niveau, rows, cols, mines):
        try:
            self.grid = Grid(niveau, rows, cols, mines)
            self.grid.afficher_tableau()
            return self.grid.niv
        except ValueError as e:
            print(e)
            print("Erreur lors de l'initialisation de la grille.")


# Initialisation du jeu
jeu = Game()

# Configuration selon le niveau
config = {
    1: (600, 600, 60),
    2: (800, 800, 40),
    3: (900, 900, 20),
}
if niv2 not in config:
    print("Erreur : Niveau non valide.")
    sys.exit()

WIDTH, HEIGHT, GridSize = config[niv2]
CellCount = WIDTH // GridSize

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)
BLUE = (0, 0, 255)

# Grille pour les drapeaux
flags = [[0] * CellCount for _ in range(CellCount)]
clicked_cells = [[0] * CellCount for _ in range(CellCount)]



def draw_grid(screen):
    for x in range(0, WIDTH, GridSize):
        for y in range(0, HEIGHT, GridSize):
            rect = pygame.Rect(x, y, GridSize, GridSize)
            pygame.draw.rect(screen, GRAY, rect)
            pygame.draw.rect(screen, BLACK, rect, 2)

mines_positions = jeu.grid.indice_mine()

def check_victory():
    for row in range(CellCount):
        for col in range(CellCount):
            if (row, col) in mines_positions:
                continue
            if clicked_cells[row][col] != 1:
                return False
    return True



def score():
    score_compt = 0
    for row in range(CellCount):
        for col in range(CellCount):
            if clicked_cells[row][col] == 1:
                score_compt += 1
    return score_compt






def main():
    pygame.init()
    font = pygame.font.Font(None, 30)


    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Démineur")
    clock = pygame.time.Clock()

    # Charger les images
    image_flag = pygame.image.load("drapeau-rouge.png").convert_alpha()
    image_flag = pygame.transform.scale(image_flag, (GridSize, GridSize))
    image_bomb = pygame.image.load("image/bombFR.png").convert_alpha()
    image_bomb = pygame.transform.scale(image_bomb, (GridSize, GridSize))
    game_screen = True

    grid = Grid(jeu.grid.niveau)
    running = True
    while running:
        if game_screen:
            screen.fill(WHITE)
            draw_grid(screen)

            # Dessiner les drapeaux
            for row in range(CellCount):
                for col in range(CellCount):
                    if flags[row][col] == 1:
                        screen.blit(image_flag, (col * GridSize, row * GridSize))

            for row in range(CellCount):
                for col in range(CellCount):
                    if clicked_cells[row][col] == 1:
                        pygame.draw.rect(screen, BLUE, pygame.Rect(col * GridSize, row * GridSize, GridSize, GridSize))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    row, col = y // GridSize, x // GridSize

                    if event.button == 3:  # Clic droit : poser/retirer un drapeau
                        flags[row][col] = 1 - flags[row][col]
                        print(f"Drapeau ({row}, {col})")

                    elif event.button == 1:  # Clic gauche : vérifier une case
                        if (row, col) in mines_positions:
                            print(f"Bombe ({row}, {col})")
                            print("Game Over")
                            for r, c in mines_positions:

                                screen.blit(image_bomb, (c * GridSize, r * GridSize))

                            pygame.display.flip()
                            pygame.time.delay(2000)

                            running = False
                        else:
                            clicked_cells[row][col] = 1
                    if check_victory():
                        print("Félicitations ! Vous avez gagné !")
                        pygame.display.set_caption("Victoire ! Bravo !")
                        pygame.time.wait(200)
                        game_screen = False
        else:
            screen.fill(WHITE)
            screen.blit(font.render(f"VICTOIRE score : {score()}, {grid.niveau}", 1, (255, 0, 0)), (85,100 ))
            pygame.display.flip()



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False




        pygame.display.flip()

    pygame.quit()
    sys.exit()


main()