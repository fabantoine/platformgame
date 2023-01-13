import pygame
import settings


class Map:
    def __init__(self):
        self.dict_type = {"tiles": [], "decor": []}
        self.map = [[0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1]]

    def load_images(self):
        for i in range(1):
            image = pygame.image.load(f"data/tiles/Bloc0{i}.png")
            self.dict_type["tiles"].append(image)

