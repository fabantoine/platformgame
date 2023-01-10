import pygame
from ground import Ground
from player import Player
from physics import Physics

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.ground = Ground(screen)
        self.background = pygame.image.load("data/background/fond.jpg")      # Chargement de l'image dans la variable
        self.player = Player()
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.input = {}


    def update_game(self):
        self.delta_time = self.clock.tick()                     # temps entre deux boucle du jeux
        self.screen.fill((0, 0, 0))                             # Remplissage en noir pour graphisme
        self.screen.blit(self.background, (0, 0))               # Affichage de background
        self.screen.blit(self.ground.surface, self.ground.rect)
        self.screen.blit(self.player.image, self.player.rect)
        self.player.update_player(self.delta_time)              # Mise à jour du joueur
        if self.input.get(pygame.K_LEFT):                       # Récuperer la flèche de gauche
            self.player.move_left()
        elif self.input.get(pygame.K_RIGHT):                    # Récupérer la flèche de droite
            self.player.move_right()
