import pygame
import sys

class Portal:
    def __init__(self, image_path,item_needed,x,y):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (180, 180))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.item_needed = item_needed
        self.tp_succeed = False

    def check_telepotation(self,player,event,npcs):
        if not any (npc.dialogue_active for npc in npcs) and not any (npc.buy_active for npc in npcs) and not any (npc.fight_active for npc in npcs):
            if event.type == pygame.KEYDOWN:
                if self.rect.colliderect(player.rect) and event.key == pygame.K_e:
                    if self.check_item(player):
                        self.tp_succeed = True
                    else:
                        self.tp_failed(player)
                    return True

    def check_item(self,player):
        for item in self.item_needed:
            if item not in player.inventory:
                return False
        return True


    def tp_failed(self, player):
        window = pygame.display.get_surface()
        font = pygame.font.Font(None, 36)
        missing_items = ', '.join([f"'{item}'" for item in self.item_needed if item not in player.inventory])
        message = f"Teleportation failed, you need {missing_items}"
        message0 = "Press 'ESC' to continue your adventure!"

        # 创建一个半透明白色背景
        background_surface = pygame.Surface(window.get_size(), pygame.SRCALPHA)
        background_surface.fill((255, 255, 255, 40))  # 半透明白色

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return

            window.blit(background_surface, (0, 0))  # 渲染半透明白色背景
            text_surface = font.render(message, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(window.get_width() // 2, window.get_height() // 2))
            window.blit(text_surface, text_rect)
            text_surface = font.render(message0, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(window.get_width() // 2, window.get_height() // 2 + 40))
            window.blit(text_surface, text_rect)
            pygame.display.flip()

