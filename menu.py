import pygame
pygame.init()
ecran = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
ecran.fill((136, 162, 193))
pygame.display.flip()
continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False
pygame.quit()

def mai(Widht = 560, Height=700, Title="Démineur"):
    screen = pygame.display.set_mode((Widht, Height))
    pygame.display.set_caption(Title)
    Mine