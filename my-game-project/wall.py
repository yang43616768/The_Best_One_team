import pygame
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.width = x
        self.height = y
        self.image = pygame.Surface((x, y))
        self.image.fill((255, 0, 0))
        