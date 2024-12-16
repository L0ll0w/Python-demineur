import pygame

pygame.init()

screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
screen.fill((136, 162, 193))
font = pygame.font.Font("font/Super Sense.ttf", 100)
titre = font.render("Des mineurs", 1, (255, 255, 255))
boutton_play = pygame.image.load("image/play.png").convert_alpha()
boutton_play = pygame.transform.scale(boutton_play, (1200, 1200))
rect = boutton_play.get_rect()


class Menu:

    def display(self, screen , text):
        ingame = True
        while ingame:
            mouse = pygame.mouse.get_pos()
            screen.blit(text, (650,100))
            screen.blit(boutton_play, (400,50))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and rect.collidepoint(mouse):
                    screen.blit(font.render("JADORE LES MINEURS", 1, (255,255,255)), (100,1000))
                    pygame.display.flip()
                if event.type == pygame.MOUSEBUTTONDOWN and not rect.collidepoint(mouse):
                    pygame.quit()

            pygame.display.flip()
        pygame.quit()


menu = Menu()
menu.display(screen, titre)