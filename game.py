import pygame
from ground import Ground
from player import Player

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.ground = Ground(screen)
        self.background = pygame.image.load("data/background/fond.jpg")      # Chargement de l'image dans la variable
        self.player = Player()

    def update_game(self):
        self.screen.fill((0, 0, 0))                             # Remplissage en noir pour graphisme
        self.screen.blit(self.background, (0, 0))               # Affichage de background
        self.screen.blit(self.ground.surface, self.ground.rect)
        self.screen.blit(self.player.image, self.player.rect)