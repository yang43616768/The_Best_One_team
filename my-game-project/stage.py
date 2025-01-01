import pygame
import sys
from setting import *
from player import *
from wall import *
from SceneManager import *
from npc import *

def draw_screen(window, background_path):
    background = pygame.image.load(background_path)
    window.blit(background, (0, 0))
    font = pygame.font.Font(None, 36)
    text = font.render("Press any key to start", True, (255, 255, 255))
    text_rect = text.get_rect(center=(WindowsSettings.width / 2, WindowsSettings.height / 2))
    window.blit(text, text_rect)
    pygame.display.flip()

def stage0(window):
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

def stage1(window):
    player = Player(150,150)
    walls = pygame.sprite.Group()
    walls.add(Wall(100,100,2,2))
    npc1 = NPC(200,200,r".\assets\images\player.png",'Alice')
    
    pygame.display.set_caption("Learn To Start")

    scene_manager = SceneManager(window)
    scene_manager.tick(30)
    scene_manager.render()
    pygame.display.flip()


    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    npc1.close_dialogue()
                else:
                    npc1.handle_input(event)

            player.update(walls)

            window.fill((0, 0, 0))

            scene_manager.render()
            scene_manager.update_camera(player)
            scene_manager.update_camera(npc1)
            scene_manager.update_camera(walls)


            pygame.display.flip()
            player.check_interaction(npc1)
