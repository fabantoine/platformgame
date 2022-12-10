import pygame
from physics import Physics


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("data/caracters/player/Face-00.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 0
        self.phy = Physics()

    def update_player(self, delta_time):
        x, y = self.phy.update_position(delta_time)
        self.rect.x += x
        self.rect.y += y
        self.collision_test()
        if abs(self.phy.velocity_x) > 0.5:
            self.phy.velocity_x *= 0.98
        if abs(self.phy.velocity_x) < 0.1:
            self.phy.velocity_x = 0

    def collision_test(self):
        if self.rect.y + self.rect.height > 350:
            self.phy.vertical_mouvments_stop()

    def move_left(self):
        self.phy.velocity_x -= 3
    def move_right(self):
        self.phy.velocity_x += 3