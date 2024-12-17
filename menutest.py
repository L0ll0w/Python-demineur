import pygame

pygame.init()

screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
screen.fill((136, 162, 193))
font = pygame.font.Font("font/Super Sense.ttf", 100)
titre = font.render("Des mineurs", 1, (255, 255, 255))
boutton_play = pygame.image.load("image/play.png").convert_alpha()
boutton_play = pygame.transform.scale(boutton_play, (400, 200))
rect_play = boutton_play.get_rect(topleft=(760, 700))

class Menu:
    def __init__(self):
        self.difficulties = {"Easy": (9, 9, 10), "Medium": (16, 16, 40), "Hard": (30, 16, 99)}
        self.radio_positions = [(850, 300), (850, 400), (850, 500)]  # Positions des radio buttons
        self.selected_difficulty = 0  # Par défaut, première difficulté sélectionnée

    def display(self, screen, text):
        ingame = True
        clock = pygame.time.Clock()

        while ingame:
            screen.fill((136, 162, 193))  # Fond de l'écran
            mouse = pygame.mouse.get_pos()

            # Afficher le titre
            screen.blit(text, (650, 100))

            # Afficher le bouton "Play"
            screen.blit(boutton_play, rect_play.topleft)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ingame = False
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Vérifier si un bouton radio est cliqué
                    for i, pos in enumerate(self.radio_positions):
                        if (event.pos[0] - pos[0]) ** 2 + (event.pos[1] - pos[1]) ** 2 < 15 ** 2:
                            self.selected_difficulty = i
                            print(i)

                    # Vérifier si le bouton "Play" est cliqué
                    if rect_play.collidepoint(mouse):
                        
                        # Afficher les options de difficulté avec des boutons radio
                        for i, (difficulty, pos) in enumerate(zip(self.difficulties.keys(), self.radio_positions)):
                            # Dessiner les cercles des radio buttons
                            pygame.draw.circle(screen, (255, 255, 255), pos, 15)  # Cercle externe
                            if i == self.selected_difficulty:
                                pygame.draw.circle(screen, (0, 255, 0), pos, 10)  # Cercle interne si sélectionné

                            # Ajouter les labels des options
                            label = font.render(difficulty, True, (255, 255, 255))
                            screen.blit(label, (pos[0] + 30, pos[1] - 30))

                        # difficulty = list(self.difficulties.values())[self.selected_difficulty]
                        # print(f"Lancement du jeu avec difficulté : {difficulty}")
                        # return difficulty

            pygame.display.flip()
            clock.tick(30)

        pygame.quit()

menu = Menu()
difficulty = menu.display(screen, titre)
# Vous pouvez maintenant utiliser la difficulté sélectionnée pour lancer votre jeu.