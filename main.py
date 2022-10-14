import pygame
from ground import Ground

pygame.init()                                   # Initialisation de pygame
pygame.display.set_caption("Titre")             # Titre de la fenetre
icon = pygame.image.load("my_icon.png")         # Charger une image
pygame.display.set_icon(icon)                   # Chanher l'icone de la fenêtre
screen = pygame.display.set_mode((400, 400))    # Taile de la fenetre
ground = Ground(screen)

background = pygame.image.load("fond.jpg")      # Chargement de l'image dans la variable


running = True

while running:
    screen.fill((0, 0, 0))                      # Remplissage en noir pour graphisme
    screen.blit(background, (0, 0))             # Affichage de background
    screen.blit(ground.surface, ground.rect)
    pygame.display.flip()                       # Mise à jour de l'affichage
    for event in pygame.event.get():            # on recupère les évenements
        if event.type == pygame.QUIT:           # si le type d'evenement est quit
            running = False
            pygame.quit()                       # Quiter Pygame
