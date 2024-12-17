import pygame
import sys

# Settings
WIDTH, HEIGHT = 600, 600
GridSize = 60  # Taille d'une cellule
CellCount = WIDTH // GridSize  # Nombre de cellules par ligne/colonne

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)

# Grille pour mémoriser les drapeaux (0 = pas de drapeau, 1 = drapeau)
flags = [[0 for _ in range(CellCount)] for _ in range(CellCount)]


# Fonction pour dessiner la grille vide
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

    # Charger l'image du drapeau
    image = pygame.image.load("drapeau-rouge.png")
    image = pygame.transform.scale(image, (GridSize, GridSize)) 

    running = True
    while running:
        # Remplir l'écran de blanc
        screen.fill(WHITE)

        # Dessiner la grille
        drawGrid(screen)

        # Dessiner les drapeaux mémorisés
        for row in range(CellCount):
            for col in range(CellCount):
                if flags[row][col] == 1:  
                    screen.blit(image, (col * GridSize, row * GridSize))

        # Gérer les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Gérer les clics de souris
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                x, y = event.pos  

                row = y // GridSize
                col = x // GridSize

                print(f"Clic sur la case ({row}, {col})")

                # Alterner entre poser et retirer un drapeau
                if flags[row][col] == 0:  
                    flags[row][col] = 1
                else: 
                    flags[row][col] = 0

        # Mettre à jour l'écran
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
    sys.exit()


# Lancer le jeu
main()
