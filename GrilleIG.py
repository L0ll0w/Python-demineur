import pygame
import sys
from random import sample

class Grid:
    def __init__(self, niveau):
        self.niveau = niveau
        self.rows, self.cols, self.mines, self.niv = self.get_dimensions_and_mines()
        self.tableau = self.creer_tableau()

    def get_dimensions_and_mines(self):
        niveaux = {
            "Easy": (10, 10, 10, 1),
            "Medium": (20, 20, 40, 2),
            "Hard": (45, 45, 99, 3),
        }
        if self.niveau not in niveaux:
            raise ValueError("Veuillez choisir un niveau entre Easy, Medium ou Hard.")
        return niveaux[self.niveau]

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
        return [(i, j) for i in range(self.rows) for j in range(self.cols) if self.tableau[i][j] == 'B']


class Game:
    def __init__(self):
        self.grid = None

    def demander_niveau(self):
        while True:
            niveau = input("Saisissez votre difficulté parmi Easy, Medium, Hard : ")
            if niveau in ["Easy", "Medium", "Hard"]:
                return niveau
            print("Niveau invalide. Réessayez.")

    def demarrer(self):
        try:
            niveau = self.demander_niveau()
            self.grid = Grid(niveau)
            self.grid.afficher_tableau()
            return self.grid.niv
        except ValueError as e:
            print(e)
            print("Veuillez recommencer.")


# Initialisation du jeu
jeu = Game()
niv2 = jeu.demarrer()

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

# Grille pour les drapeaux
flags = [[0] * CellCount for _ in range(CellCount)]


def draw_grid(screen):
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
    image_flag = pygame.image.load("drapeau-rouge.png").convert_alpha()
    image_flag = pygame.transform.scale(image_flag, (GridSize, GridSize))
    image_bomb = pygame.image.load("image/bombFR.png").convert_alpha()
    image_bomb = pygame.transform.scale(image_bomb, (GridSize, GridSize))

    mines_positions = jeu.grid.indice_mine()
    running = True
    while running:
        screen.fill(WHITE)
        draw_grid(screen)

        # Dessiner les drapeaux
        for row in range(CellCount):
            for col in range(CellCount):
                if flags[row][col] == 1:
                    screen.blit(image_flag, (col * GridSize, row * GridSize))

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
                        pygame.time.wait(2000)

                        running = False

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
    sys.exit()


main()
