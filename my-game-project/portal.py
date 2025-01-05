import pygame

class Portal:
    def __init__(self, image_path,item_needed,x,y):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.item_needed = item_needed
        self.tp_succeed = False

    def check_telepotation(self,player,event):
        if event.type == pygame.KEYDOWN:
            if self.rect.colliderect(player.rect) and event.key == pygame.K_e:
                if self.check_item(player):
                    self.tp_succeed = True
                else:
                    self.tp_failed()
                return True

    def check_item(self,player):
        for item in self.item_needed:
            if item not in player.inventory:
                return False
        return True


    def tp_failed(self):

        pass    
