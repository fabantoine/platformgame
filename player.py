import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Face-00.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 200
