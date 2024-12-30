import pygame
import random
import sys
from npc import *
from wall import *
from setting import *
from map import *
from SceneManager import *
from player import *

def draw_screen(window, background_path):
    background = pygame.image.load(background_path)
    window.blit(background, (0, 0))
    font = pygame.font.Font(None, 36)
    text = font.render("Press any key to start", True, (255, 255, 255))
    text_rect = text.get_rect(center=(WindowsSettings.width / 2, WindowsSettings.height / 2))
    window.blit(text, text_rect)
    pygame.display.flip()


def main():
    pygame.init()
    window = pygame.display.set_mode((WindowsSettings.width, WindowsSettings.height))

    # Stage 0 - Start Screen
    pygame.display.set_caption("Game Start")
    draw_screen(window,r".\assets\images\grass.png")
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                waiting = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    pygame.display.set_caption("Learn To Start")
    player = Player(150,150)
    walls = pygame.sprite.Group()
    walls.add(Wall(100,100,2,2))
    walls.add(Wall(200,200,2,2))
    # Stage 1 - Teaching Section
    pygame.display.set_caption("Learn To Start")
    scene_manager = SceneManager(window)
    scene_manager.tick(30)
    scene_manager.render()
    pygame.display.flip()

    npc1 = NPC(200,200,r".\assets\images\player.png",'Alice')
    player = Player(100, 100)




    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            player.update(walls)

            scene_manager.update_camera(player)
            scene_manager.update_camera(npc1)
            scene_manager.update_camera(walls)

            pygame.display.flip()
            player.check_interaction(npc1)

if __name__ == "__main__":
    main()