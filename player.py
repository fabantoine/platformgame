import pygame
from physics import Physics


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("data/caracters/player/Face-00.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 0
        self.phy = Physics()  # Instanciation de la physique

    def update_player(self, delta_time):
        x, y = self.phy.update_position(delta_time)  # récupération des déplacement en x et y
        self.rect.x += x  # Ajout du déplacement à la position en x
        self.rect.y += y  # Ajout du déplacement à la position en y
        self.collision_test()  # Test si on touche le sol
        if abs(self.phy.velocity_x) > 0.5:  # Frottement avec le sol
            self.phy.velocity_x *= 0.94
        if abs(self.phy.velocity_x) < 0.1:  # Arret pour une petite vitesse
            self.phy.velocity_x = 0

    def collision_test(self):  # si le sol est percuté on immobilise le joueur
        if self.rect.y + self.rect.height > 350:
            self.phy.vertical_mouvments_stop()

    def move_left(self):  # Déplacement à gauche
        self.phy.velocity_x -= 3

    def move_right(self):  # Déplacement à droite
        self.phy.velocity_x += 3
