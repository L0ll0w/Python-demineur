import pygame

pygame.init()

screen = pygame.display.set_mode((1920, 1080))
screen.fill((136, 162, 193))
font = pygame.font.Font("font/Super Sense.ttf", 100)
titre = font.render("Des mineurs", 1, (255, 255, 255))

# Images
boutton_play = pygame.image.load("image/play.png").convert_alpha()
boutton_score = pygame.image.load("image/score.png").convert_alpha()
boutton_exit = pygame.image.load("image/exit.png").convert_alpha()
boutton_back = pygame.image.load("image/back.png").convert_alpha()
boutton_playpressed = pygame.image.load("image/playpressed.png").convert_alpha()
boutton_scorepressed = pygame.image.load("image/scorepressed.png").convert_alpha()
boutton_exitpressed = pygame.image.load("image/exitpressed.png").convert_alpha()
boutton_backpressed = pygame.image.load("image/backpressed.png").convert_alpha()
difficulty_pad = pygame.image.load("image/difficultypad.png").convert_alpha()
titleimage = pygame.image.load("image/title.png").convert_alpha()
titleresized = pygame.transform.scale(titleimage, (1000, 150))

# Images positions
play_position = (800, 350)
score_position = (800, 550)
exit_position = (800, 750)
back_position = (25, 925)
play_position2 = (1590, 925)
# backscore_position = (25, 925)

# interactions with the images
rect_play = boutton_play.get_rect(topleft=play_position)
rect_score = boutton_score.get_rect(topleft=score_position)
rect_exit = boutton_exit.get_rect(topleft=exit_position)
rect_back = boutton_back.get_rect(topleft=back_position)
rect_play2 = boutton_play.get_rect(topleft=play_position2)

class Menu:
    def __init__(self):
        self.main_menu = True
        self.score_menu = False
        self.difficulties = {"Easy": (9, 9, 10), "Medium": (16, 16, 40), "Hard": (30, 16, 99)} # Difficulty levels (w/h/mines)
        self.radio_positions = [(115, 400), (115, 500), (115, 600)] # Difficulty buttons positions
        self.selected_difficulty = 0

    def display(self, screen, text):
        ingame = True
        while ingame:
            mouse = pygame.mouse.get_pos()
            screen.fill((136, 162, 193)) # Fill the screen with a color
            # screen.blit(text, (600, 50))
            screen.blit(titleresized, (475,20))

            if self.main_menu: # Show main menu
                screen.blit(boutton_play, play_position)
                screen.blit(boutton_score, score_position)
                screen.blit(boutton_exit, exit_position)

            elif self.score_menu: # Show score page
                screen.blit(boutton_back, back_position)
                font = pygame.font.Font("font/Super Sense.ttf", 50)
                i = 1
                y = 200
                while i <= 6:
                    i = i + 1
                    y = y + 100
                    screen.blit(font.render("Party", 1, (255, 255, 255)), (400, y))

            else: # Show start menu
                screen.blit(difficulty_pad, (50, 160))
                
                for i, (difficulty, pos) in enumerate(zip(self.difficulties.keys(), self.radio_positions)):
                    font = pygame.font.Font("font/Super Sense.ttf", 70)
                    
                    pygame.draw.circle(screen, (255, 255, 255), pos, 15)
                    if i == self.selected_difficulty:
                        pygame.draw.circle(screen, (0, 255, 0), pos, 10)

                    label = font.render(difficulty, True, (255, 255, 255))
                    screen.blit(label, (pos[0] + 30, pos[1] - 30))

                font = pygame.font.Font("font/Super Sense.ttf", 50)
                screen.blit(font.render("Difficulty :", 1, (255, 255, 255)), (115, 250))
                font = pygame.font.Font("font/Super Sense.ttf", 70)
                screen.blit(font.render("W = ", 1, (255, 255, 255)), (600, 250))
                screen.blit(font.render("H = ", 1, (255, 255, 255)), (900, 250))
                screen.blit(font.render("Mines = ", 1, (255, 255, 255)), (1200, 250))

                w, h, mines = list(self.difficulties.values())[self.selected_difficulty]
                screen.blit(font.render(str(w), 1, (255, 255, 255)), (750, 250))
                screen.blit(font.render(str(h), 1, (255, 255, 255)), (1050, 250))
                screen.blit(font.render(str(mines), 1, (255, 255, 255)), (1550, 250))

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
                            # start_game()
                            print("launch game")
                            screen.blit(font.render("LES MINEURS", 1, (255, 255, 255)), (800, 550))

                        for i, pos in enumerate(self.radio_positions):
                            distance = ((mouse[0] - pos[0]) ** 2 + (mouse[1] - pos[1]) ** 2) ** 0.5
                            if distance <= 15:
                                self.selected_difficulty = i
                                print(f"Difficulty selected: {list(self.difficulties.keys())[i]}")
                                print(i)

            pygame.display.flip()
        pygame.quit()

menu = Menu()
menu.display(screen, titre)
