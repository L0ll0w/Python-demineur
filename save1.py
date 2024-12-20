import csv

def save_score(name, score, difficulty):
    with open('stats.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, score, difficulty])






# Dans le fichier Menu
def display(self, screen):
    ingame = True
    while ingame:
        mouse = pygame.mouse.get_pos()
        screen.fill(colorfill)
        screen.blit(titleresized, (475, 20))

        if self.main_menu:  # Show main menu
            screen.blit(boutton_play, play_position)
            screen.blit(boutton_load, load_position)
            screen.blit(boutton_score, score_position)
            screen.blit(boutton_exit, exit_position)

        elif self.score_menu:  # Show score page
            screen.blit(boutton_back, back_position)
            font = pygame.font.Font("font/Super Sense.ttf", 50)
            i = 1
            y = 200
            with open('stats.csv', 'r') as file:
                reader = csv.reader(file, delimiter=',')
                for row in reader:
                    y = y + 100
                    screen.blit(font.render(f"{row[0]}", 1, (255, 255, 255)), (400, y))
                    screen.blit(font.render(f"{row[1]}", 1, (255, 255, 255)), (650, y))
                    screen.blit(font.render(f"{row[2]}", 1, (255, 255, 255)), (900, y))

        else:  # Show start menu after victory
            screen.blit(difficulty_pad, (50, 160))

            for i, (difficulty, pos) in enumerate(zip(self.difficulties.keys(), self.radio_positions)):
                font = pygame.font.Font("font/Super Sense.ttf", 70)
                pygame.draw.circle(screen, (255, 255, 255), pos, 15)
                if i == self.selected_difficulty:
                    pygame.draw.circle(screen, (0, 255, 0), pos, 10)

                label = font.render(difficulty, True, (255, 255, 255))
                screen.blit(label, (pos[0] + 30, pos[1] - 30))

            font = pygame.font.Font("font/Super Sense.ttf", 50)
            screen.blit(font.render("Difficulty :", True, (255, 255, 255)), (115, 250))
            w, h, mines = list(self.difficulties.values())[self.selected_difficulty]
            font = pygame.font.Font("font/Super Sense.ttf", 70)
            screen.blit(font.render(f"W = {w}", True, (255, 255, 255)), (600, 250))
            screen.blit(font.render(f"H = {h}", True, (255, 255, 255)), (900, 250))
            screen.blit(font.render(f"Mines = {mines}", True, (255, 255, 255)), (1200, 250))

            screen.blit(boutton_back, back_position)
            screen.blit(boutton_play, play_position2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONUP:
                if self.main_menu:
                    if rect_play.collidepoint(mouse):
                        self.main_menu = False
                    elif rect_score.collidepoint(mouse):
                        self.main_menu = False
                        self.score_menu = True
                    elif rect_exit.collidepoint(mouse):
                        ingame = False

                else:
                    if rect_back.collidepoint(mouse):
                        self.main_menu = True
                        self.score_menu = False
                    elif rect_play2.collidepoint(mouse):
                        self.difficulty_name = list(self.difficulties.keys())[self.selected_difficulty]
                        w, h, mines = self.difficulties[self.difficulty_name]
                        start_game(w, h, mines, self.difficulty_name)  # Démarrer une nouvelle partie

                    for i, pos in enumerate(self.radio_positions):
                        distance = ((mouse[0] - pos[0]) ** 2 + (mouse[1] - pos[1]) ** 2) ** 0.5
                        if distance <= 15:
                            self.selected_difficulty = i
                            print(f"Difficulty selected: {list(self.difficulties.keys())[i]}")



if check_victory():
    print("Victory!")
    game_screen = False
    # Affichage du bouton "Rejouer"
    screen.blit(boutton_play, play_position2)
    pygame.display.flip()

# Ajouter une logique pour que le joueur clique sur "Rejouer"
for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONUP:
        if rect_play2.collidepoint(mouse):  # Si le joueur clique sur "Rejouer"
            # Réinitialiser la partie
            start_game(w, h, mines, difficulty_name)  # Redémarre le jeu avec les mêmes paramètres
