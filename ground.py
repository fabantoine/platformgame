import pygame


class Ground:
    def __init__(self, screen):
        self.surface = pygame.Surface((screen.get_width(), 50))
        self.col = self.surface.fill((0, 255, 0))
        self.rect = self.surface.get_rect()
        self.rect.y = screen.get_height() - 50
