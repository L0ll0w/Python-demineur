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