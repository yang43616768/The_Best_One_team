import pygame
class Transparent:
    def __init__(self,image_path,x,y,length,width):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (length, width))
        self.surface = pygame.Surface((length, width), pygame.SRCALPHA)
        self.alpha = 255
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def check_transparent(self,player):
        if self.rect.colliderect(player.rect):
                self.alpha = 30
        else:
            self.alpha = 255

