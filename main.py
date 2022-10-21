import time
import pygame
from game import Game

pygame.init()
# Initialisation de pygame
pygame.display.set_caption("Titre")             # Titre de la fenetre
icon = pygame.image.load("my_icon.png")         # Charger une image
pygame.display.set_icon(icon)                   # Chanher l'icone de la fenêtre
screen = pygame.display.set_mode((400, 400))    # Taile de la fenetre
game = Game(screen)

running = True

while running:
    game.update_game()
    pygame.display.flip()                       # Mise à jour de l'affichage
    for event in pygame.event.get():            # on recupère les évenements
        if event.type == pygame.QUIT:           # si le type d'evenement est quit
            running = False
            pygame.quit()                       # Quiter Pygame
