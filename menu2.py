import pygame

pygame.init()

screen = pygame.display.set_mode((1920, 1080))
screen.fill((136, 162, 193))
font = pygame.font.Font("font/Super Sense.ttf", 100)
titre = font.render("Des mineurs", 1, (255, 255, 255))
boutton_play = pygame.image.load("image/play.png").convert_alpha()
boutton_score = pygame.image.load("image/score.png").convert_alpha()
boutton_exit = pygame.image.load("image/exit.png").convert_alpha()


# Position de l'image
play_position = (800, 350)
score_position = (800, 550)
exit_position = (800, 750)


# Ajuster la position du rect pour qu'il suive l'image
rect_play = boutton_play.get_rect(topleft=play_position)
rect_score = boutton_score.get_rect(topleft=score_position)
rect_exit = boutton_exit.get_rect(topleft=exit_position)


class Menu:
    def display(self, screen, text):
        ingame = True
        while ingame:
            mouse = pygame.mouse.get_pos()
            screen.blit(text, (680, 100))
            screen.blit(boutton_play, play_position)
            screen.blit(boutton_score, score_position)
            screen.blit(boutton_exit, exit_position)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONUP and rect_play.collidepoint(mouse):
                    screen.blit(font.render("J'ADORE", 1, (255, 255, 255)), (100, 1000))
                    pygame.display.flip()
                if event.type == pygame.MOUSEBUTTONUP and rect_score.collidepoint(mouse):
                    screen.blit(font.render("LES MiNEURS", 1, (255, 255, 255)), (600, 1000))
                    pygame.display.flip()
                if event.type == pygame.MOUSEBUTTONUP and rect_exit.collidepoint(mouse):
                    ingame=False


            pygame.display.flip()
        pygame.quit()


menu = Menu()
menu.display(screen, titre)
