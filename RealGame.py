import pygame
import sys
from random import sample
import time

class Grid:
    def __init__(self, niveau):
        self.niv = 0
        self.niveau = niveau
        self.rows, self.cols, self.mines = self.get_dimensions_and_mines()
        self.tableau = []
        self.creer_tableau()

    def get_dimensions_and_mines(self):
        niveaux = {
            "Easy": (10, 10, 10, 1),
            "Medium": (20, 20, 40, 2),
            "Hard": (45, 45, 99, 3),
        }
        if self.niveau not in niveaux:
            raise ValueError("Veuillez choisir un niveau entre Easy, Medium ou Hard.")
        self.niv = niveaux[self.niveau][3]
        return niveaux[self.niveau][:3]

    def creer_tableau(self):
        self.tableau = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        all_positions = [(i, j) for i in range(self.rows) for j in range(self.cols)]
        for i, j in sample(all_positions, self.mines):
            self.tableau[i][j] = 'B'

    def afficher_tableau(self):
        for ligne in self.tableau:
            print(' '.join(str(cell) for cell in ligne))

    def indice_mine(self):
        tab_mine_indice = [(i, j) for i in range(self.rows) for j in range(self.cols) if self.tableau[i][j] == 'B']
        return tab_mine_indice


class Game:
    def __init__(self):
        self.niveau = None
        self.grid = None

    def demander_niveau(self):
        self.niveau = input("Saisissez votre difficulté parmi Easy, Medium, Hard : ")
    def indice(self):
        return self.grid.indice_mine()

    def demarrer(self):
        try:
            self.demander_niveau()
            self.grid = Grid(self.niveau)
            self.grid.afficher_tableau()
            self.grid.indice_mine()
            return self.grid.niv
        except ValueError as e:
            print(e)
            print("Veuillez recommencer.")


jeu = Game()
niv2 = jeu.demarrer()

# Settings
config = {
    1: (600, 600, 60),
    2: (800, 800, 40),
    3: (900, 900, 20),
}
if niv2 in config:
    WIDTH, HEIGHT, GridSize = config[niv2]
else:
    print("Erreur : Niveau non valide.")
    sys.exit()

CellCount = WIDTH // GridSize

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)

# Grille pour mémoriser les drapeaux (0 = pas de drapeau, 1 = drapeau)
flags = [[0 for _ in range(CellCount)] for _ in range(CellCount)]


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

    # Charger les images
    image_flag = pygame.image.load("drapeau-rouge.png")
    image_flag = pygame.transform.scale(image_flag, (GridSize, GridSize))
    image_bomb = pygame.image.load("image/bombFR.png")
    image_bomb = pygame.transform.scale(image_bomb, (GridSize, GridSize))

    running = True
    while running:
        screen.fill(WHITE)
        drawGrid(screen)

        # Dessiner les drapeaux
        for row in range(CellCount):
            for col in range(CellCount):
                if flags[row][col] == 1:
                    screen.blit(image_flag, (col * GridSize, row * GridSize))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                x, y = event.pos
                row, col = y // GridSize, x // GridSize
                flags[row][col] = 1 - flags[row][col]  # Alterner entre poser/retirer un drapeau
                print(f"Drapeau ({row}, {col})")
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                tab = jeu.indice()
                for coord in tab:
                    x, y = event.pos
                    row, col = y // GridSize, x // GridSize
                    if coord == (row,col):
                        print(f"Bombe ({row}, {col})")
                        print("Game Over")
                        game_over = True
                        for coord2 in tab:
                            screen.blit(image_bomb, (coord2[1] * GridSize, coord2[0] * GridSize))

                            pygame.display.update()
                            pygame.time.delay(500)
                            running = False








        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
    sys.exit()


main()
