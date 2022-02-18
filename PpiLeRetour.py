import pygame


LARGEUR = 800
HAUTEUR = 800


pygame.init()
ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))

fini = False

while not fini:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        fini = True
        
        pygame.display.flip() 
