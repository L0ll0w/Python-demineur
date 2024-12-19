import pygame
import sys
import csv
from grid import Grid



def start_game(w, h, mines, difficulty_name):
    grid = Grid((w,h,mines))

    WIDTH = w * 60
    HEIGHT = h * 60
    GridSize = 60
    CellCount = w
    mines_positions = Grid((w, h, mines)).indice_mine()

    WHITE = (255, 255, 255)
    GRAY = (192, 192, 192)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)

    flags = [[0] * CellCount for _ in range(CellCount)]
    clicked_cells = [[0] * CellCount for _ in range(CellCount)]

    input_rect = pygame.Rect(190,600,500,32)
    color = pygame.Color('lightskyblue3')
    titleimage = pygame.image.load("image/title.png").convert_alpha()
    titleresized = pygame.transform.scale(titleimage, (1000, 150))
    colorfill = (136, 162, 193)

    def draw_grid(screen):
        for x in range(0, WIDTH, GridSize):
            for y in range(0, HEIGHT, GridSize):
                rect = pygame.Rect(x, y, GridSize, GridSize)
                pygame.draw.rect(screen, GRAY, rect)
                pygame.draw.rect(screen, BLACK, rect, 2)

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

    def reveal_cells(row, col):
        # Vérifie les limites de la grille
        if row < 0 or row >= CellCount or col < 0 or col >= CellCount:
            return

        # Arrête la récursion si la case est déjà cliquée ou contient une bombe
        if clicked_cells[row][col] == 1 or (row, col) in mines_positions:
            return

        # Colorie la case actuelle
        clicked_cells[row][col] = 1

        # Liste des directions pour explorer les cases adjacentes
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        # Révélation récursive des cases adjacentes
        for dx, dy in directions:
            reveal_cells(row + dx, col + dy)

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Démineur")
    clock = pygame.time.Clock()

    image_flag = pygame.image.load("image/redflag.png").convert_alpha()
    image_flag = pygame.transform.scale(image_flag, (GridSize, GridSize))
    image_bomb = pygame.image.load("image/bombFR.png").convert_alpha()
    image_bomb = pygame.transform.scale(image_bomb, (GridSize, GridSize))
    font = pygame.font.Font(None, 30)
    user_text = ""

    game_screen = True
    running = True

    while running:
        if game_screen:
            screen.fill(WHITE)
            draw_grid(screen)

            font = pygame.font.Font("font/Super Sense.ttf", 20)
            # difficulty_label = font.render(f"Difficulty: {difficulty_name}", True, (0, 0, 0))
            # screen.blit(difficulty_label, (10, 10))

            # Dessiner les drapeaux
            for row in range(CellCount):
                for col in range(CellCount):
                    if flags[row][col] == 1:
                        screen.blit(image_flag, (col * GridSize, row * GridSize))
                    elif clicked_cells[row][col] == 1:
                        pygame.draw.rect(screen, BLUE, pygame.Rect(col * GridSize, row * GridSize, GridSize, GridSize))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    row, col = y // GridSize, x // GridSize

                    if event.button == 3:
                        flags[row][col] = 1 - flags[row][col]
                        print(f"Drapeau ({row}, {col})")
                    elif event.button == 1:
                        if (row, col) in mines_positions:

                            print(f"Bombe ({row}, {col})")

                            print("Game Over")

                            for r, c in mines_positions:
                                screen.blit(image_bomb, (c * GridSize, r * GridSize))

                            pygame.display.flip()

                            running = False

                        else:

                            # Démarre la révélation des cases à partir de la case cliquée

                            reveal_cells(row, col)

            if check_victory():
                print("Victory!")
                game_screen = False

                screen = pygame.display.set_mode((1920, 1080))

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        user_text += user_text[:-1]
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    if event.key == pygame.K_RETURN:
                        with open('stats.csv', mode='a', encoding='utf-8') as fichier_csv:
                            writer = csv.writer(fichier_csv)
                            writer.writerow([user_text, score(), difficulty_name ])
                    else:
                        user_text += event.unicode

            screen.fill(colorfill)
            screen.blit(titleresized, (475,20))
            screen.blit(font.render(f"VICTOIRE score : {score()}, {difficulty_name}, {user_text}", 1, (255, 0, 0)), (185,500 ))
            pygame.draw.rect(screen,color,input_rect, 2)
            text_surface = font.render(user_text, 1, (0, 0, 0))
            screen.blit(text_surface, input_rect)
            pygame.display.flip()

        pygame.display.flip()

    pygame.quit()
    sys.exit()
