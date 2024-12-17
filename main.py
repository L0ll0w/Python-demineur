import pygame

pygame.init()

screen = pygame.display.set_mode((1920, 1080))
screen.fill((136, 162, 193))
font = pygame.font.Font("font/Super Sense.ttf", 100)
titre = font.render("Des mineurs", 1, (255, 255, 255))
boutton_play = pygame.image.load("image/play.png").convert_alpha()
boutton_score = pygame.image.load("image/score.png").convert_alpha()
boutton_exit = pygame.image.load("image/exit.png").convert_alpha()
boutton_back = pygame.image.load("image/back.png").convert_alpha()

play_position = (800, 350)
score_position = (800, 550)
exit_position = (800, 750)
back_position = (550, 750)
play_position2 = (1050, 750)

rect_play = boutton_play.get_rect(topleft=play_position)
rect_score = boutton_score.get_rect(topleft=score_position)
rect_exit = boutton_exit.get_rect(topleft=exit_position)
rect_back = boutton_back.get_rect(topleft=back_position)
rect_play2 = boutton_play.get_rect(topleft=play_position2)


class Menu:
    def __init__(self):
        self.main_menu = True
        self.difficulties = {"Easy": (9, 9, 10), "Medium": (16, 16, 40), "Hard": (30, 16, 99)}
        self.radio_positions = [(350, 400), (800, 400), (1250, 400)]
        self.selected_difficulty = 0

    def display(self, screen, text):
        ingame = True
        while ingame:
            mouse = pygame.mouse.get_pos()
            screen.fill((136, 162, 193))
            screen.blit(text, (680, 100))

            if self.main_menu:
                screen.blit(boutton_play, play_position)
                screen.blit(boutton_score, score_position)
                screen.blit(boutton_exit, exit_position)
            else:
                for i, (difficulty, pos) in enumerate(zip(self.difficulties.keys(), self.radio_positions)):
                    font = pygame.font.Font("font/Super Sense.ttf", 75)
                    
                    pygame.draw.circle(screen, (255, 255, 255), pos, 15)
                    if i == self.selected_difficulty:
                        pygame.draw.circle(screen, (0, 255, 0), pos, 10)

                    label = font.render(difficulty, True, (255, 255, 255))
                    screen.blit(label, (pos[0] + 30, pos[1] - 30))
                
                screen.blit(font.render("W = ", 1, (255, 255, 255)), (450, 550))
                screen.blit(font.render("H = ", 1, (255, 255, 255)), (750, 550))
                screen.blit(font.render("Mines = ", 1, (255, 255, 255)), (1050, 550))

                w, h, mines = list(self.difficulties.values())[self.selected_difficulty]
                screen.blit(font.render(str(w), 1, (255, 255, 255)), (600, 550))
                screen.blit(font.render(str(h), 1, (255, 255, 255)), (900, 550))
                screen.blit(font.render(str(mines), 1, (255, 255, 255)), (1400, 550))

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
                            screen.blit(font.render("LES MINEURS", 1, (255, 255, 255)), (600, 1000))
                            pygame.display.flip()
                        elif rect_exit.collidepoint(mouse):
                            ingame = False
                    else:
                        if rect_back.collidepoint(mouse):
                            self.main_menu = True

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
