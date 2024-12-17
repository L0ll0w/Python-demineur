import pygame
from game import start_game

pygame.init()

# Dimensions par défaut
screen_width = 1920
screen_height = 1080

screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Menu Principal")
font = pygame.font.Font("font/Super Sense.ttf", 100)

# Chargement des images
boutton_play = pygame.image.load("image/play.png").convert_alpha()
boutton_score = pygame.image.load("image/score.png").convert_alpha()
boutton_exit = pygame.image.load("image/exit.png").convert_alpha()
boutton_back = pygame.image.load("image/back.png").convert_alpha()
difficulty_pad = pygame.image.load("image/difficultypad.png").convert_alpha()
titleimage = pygame.image.load("image/title.png").convert_alpha()

class Menu:
    def __init__(self):
        self.main_menu = True
        self.score_menu = False
        self.difficulties = {"Easy": (9, 9, 10), "Medium": (16, 16, 40), "Hard": (30, 16, 99)}
        self.radio_positions = [(0, 0), (0, 0), (0, 0)]
        self.selected_difficulty = 0
        self.update_positions(screen_width, screen_height)

    def update_positions(self, width, height):
        """Met à jour dynamiquement les positions des éléments."""
        self.title_position = (width // 2 - 500, height // 12)
        self.play_position = (width // 2 - 150, height // 3)
        self.score_position = (width // 2 - 150, height // 2)
        self.exit_position = (width // 2 - 150, int(height * 0.75))
        self.back_position = (25, height - 100)
        self.play_position2 = (width - 300, height - 100)

        # Boutons radio pour la sélection de difficulté
        self.radio_positions = [
            (width // 8, height // 2 - 50),
            (width // 8, height // 2 + 50),
            (width // 8, height // 2 + 150),
        ]

    def display(self, screen):
        running = True
        while running:
            mouse = pygame.mouse.get_pos()
            screen.fill((136, 162, 193))  # Fond de l'écran

            # Ajuste les éléments selon la taille actuelle
            screen_width, screen_height = screen.get_size()
            self.update_positions(screen_width, screen_height)

            # Affiche le titre
            title_resized = pygame.transform.scale(titleimage, (screen_width // 2, screen_height // 10))
            screen.blit(title_resized, self.title_position)

            if self.main_menu:
                # Affiche les boutons principaux
                screen.blit(boutton_play, self.play_position)
                screen.blit(boutton_score, self.score_position)
                screen.blit(boutton_exit, self.exit_position)

            elif self.score_menu:
                # Affiche le menu des scores
                screen.blit(boutton_back, self.back_position)
                font_small = pygame.font.Font("font/Super Sense.ttf", 50)
                for i in range(6):
                    y = 200 + i * 100
                    screen.blit(font_small.render(f"Party {i+1}", 1, (255, 255, 255)), (screen_width // 3, y))

            else:
                # Affiche le menu des difficultés
                difficulty_pad_resized = pygame.transform.scale(difficulty_pad, (screen_width // 4, screen_height // 2))
                screen.blit(difficulty_pad_resized, (50, 160))

                font = pygame.font.Font("font/Super Sense.ttf", 70)
                for i, (difficulty, pos) in enumerate(zip(self.difficulties.keys(), self.radio_positions)):
                    pygame.draw.circle(screen, (255, 255, 255), pos, 15)
                    if i == self.selected_difficulty:
                        pygame.draw.circle(screen, (0, 255, 0), pos, 10)

                    label = font.render(difficulty, True, (255, 255, 255))
                    screen.blit(label, (pos[0] + 30, pos[1] - 30))

                w, h, mines = list(self.difficulties.values())[self.selected_difficulty]
                info_font = pygame.font.Font("font/Super Sense.ttf", 50)
                screen.blit(info_font.render(f"W = {w}", 1, (255, 255, 255)), (screen_width // 2, 200))
                screen.blit(info_font.render(f"H = {h}", 1, (255, 255, 255)), (screen_width // 2, 300))
                screen.blit(info_font.render(f"Mines = {mines}", 1, (255, 255, 255)), (screen_width // 2, 400))

                screen.blit(boutton_back, self.back_position)
                screen.blit(boutton_play, self.play_position2)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.VIDEORESIZE:
                    # Redimensionne la fenêtre et les éléments
                    screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

                if event.type == pygame.MOUSEBUTTONUP:
                    if self.main_menu:
                        if self.collide(mouse, self.play_position, boutton_play):
                            self.main_menu = False
                        elif self.collide(mouse, self.score_position, boutton_score):
                            self.main_menu = False
                            self.score_menu = True
                        elif self.collide(mouse, self.exit_position, boutton_exit):
                            running = False

                    else:
                        if self.collide(mouse, self.back_position, boutton_back):
                            self.main_menu = True
                            self.score_menu = False
                        elif self.collide(mouse, self.play_position2, boutton_play):
                            difficulty = list(self.difficulties.keys())[self.selected_difficulty]
                            w, h, mines = self.difficulties[difficulty]
                            start_game(w, h, mines)

                        for i, pos in enumerate(self.radio_positions):
                            distance = ((mouse[0] - pos[0]) ** 2 + (mouse[1] - pos[1]) ** 2) ** 0.5
                            if distance <= 15:
                                self.selected_difficulty = i

            pygame.display.flip()

    @staticmethod
    def collide(mouse_pos, element_pos, image):
        """Vérifie si la souris clique sur un élément."""
        x, y = element_pos
        w, h = image.get_size()
        return x <= mouse_pos[0] <= x + w and y <= mouse_pos[1] <= y + h


menu = Menu()
menu.display(screen)