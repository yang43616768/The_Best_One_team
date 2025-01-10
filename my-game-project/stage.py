import pygame
import sys
from setting import *
from player import *
from wall import *
from SceneManager import *
from npc import *
from portal import *
from transparent import *


def draw_screen(window, background_path):
    background = pygame.image.load(background_path)
    window.blit(background, (0, 0))
    font = pygame.font.Font(None, 36)
    text = font.render("Press any key to start", True, (255, 255, 255))
    text_rect = text.get_rect(center=(WindowsSettings.width / 2, WindowsSettings.height / 2))
    window.blit(text, text_rect)
    pygame.display.flip()

def stage_common(npcs,player,walls,transparents,portal,scene_manager,window):
    waiting = True
    while waiting:
        for npc in npcs:
            npc.switch_bubble()
            scene_manager.location(npc.bubble,npcs)
            pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    for npc in npcs:
                        npc.close_dialogue()
                        npc.buy_active = False
                    player.bag_active = False
                elif event.key == pygame.K_i and not any(npc.dialogue_active for npc in npcs):  # 按下i键打开背包
                    player.bag_active = not player.bag_active

                else:
                    for npc in npcs:
                        npc.handle_input(event,player)
            player.update(walls, any(npc.dialogue_active for npc in npcs),any(npc.buy_active for npc in npcs),scene_manager)
            for transparent in transparents:
                transparent.check_transparent(player)

            window.fill((0, 0, 0))

            scene_manager.update_camera(player)  # 更新摄像机位置
            scene_manager.render2(npcs)
            scene_manager.location(player,npcs)
            scene_manager.location(walls,npcs)
            for npc in npcs:
                scene_manager.location(npc,npcs)
            scene_manager.location(portal,npcs)
            for transparent in transparents:
                scene_manager.location(transparent,npcs)
            player.show_inventory(scene_manager.window)
            portal.check_telepotation(player,event)
            pygame.display.flip()
            if portal.tp_succeed:
                waiting = False

def stage0(window):
    pygame.display.set_caption("Game Start")
    draw_screen(window,r".\assets\images\grass.jpg")
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                waiting = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def stage1(window,player):

    walls = pygame.sprite.Group()


    npc1 = NPC(350,880,NpcSettings.Lilia)
    npc2 = NPC(350,300,NpcSettings.Berries)
    npc3 = NPC(350,1460,NpcSettings.Nyakori)
    npc4 = NPC(800,880,NpcSettings.Eliza)
    npc5 = NPC(1200,880,NpcSettings.Sakura)
    npcs = [npc1,npc2,npc3,npc4,npc5]
    portal = Portal(r".\assets\images\portal.png",["The Legendary Sword","The Legendary Shield","The Lengendary Armor","The philosopher's stone"], 1250, 880)

    walls.add(Wall(1390,0,20,700))
    walls.add(Wall(1390,1100,20,700))
    walls.add(Wall(2090,0,20,700))
    walls.add(Wall(2090,1100,20,700))
    walls.add(Wall(1410,680,680,20))
    walls.add(Wall(1410,1100,680,20))

    walls.add(Wall(2110,390,890,20))
    walls.add(Wall(2110,1390,890,20))


    npcs = [npc1,npc2,npc3,npc4,npc5]
    
    transparent_roof1 = Transparent(r".\assets\images\roof.png",0,500,800,800)
    transparent_roof2 = Transparent(r".\assets\images\roof.png",0,0,600,500)
    transparent_roof3 = Transparent(r".\assets\images\roof.png",0,1300,600,500)
    transparent_roof4 = Transparent(r".\assets\images\roof.png",1400,0,700,700)
    transparent_roof5 = Transparent(r".\assets\images\roof.png",1400,1110,700,700)
    transparent_roof6 = Transparent(r".\assets\images\roof.png",2100,0,900,400)
    transparent_roof7 = Transparent(r".\assets\images\roof.png",2100,1400,900,400)
    transparents = [transparent_roof1,transparent_roof2,transparent_roof3,transparent_roof4,transparent_roof5,transparent_roof6,transparent_roof7]

    pygame.display.set_caption("Learn To Start")

    scene_manager = SceneManager(window)
    scene_manager.tick(30)

    #全物品指令
    # for item in Item_List.keys:   
    #     player.inventory.append(item)
    scene_manager.render2(npcs)

    stage_common(npcs,player,walls,transparents,portal,scene_manager,window)


def stage2(window,player):
    player.rect.x = 1600
    player.rect.y = 900
    walls = pygame.sprite.Group()
    walls.add(Wall(0,200,50,50))


    npc1 = NPC(350,880,NpcSettings.Theia)
    npc2 = NPC(350,300,NpcSettings.Lianne)
    npc3 = NPC(800,880,NpcSettings.Irin)
    npc4 = NPC(1200,880,NpcSettings.Irin_Evil)
    npcs = [npc1,npc2,npc3,npc4]
    portal = Portal(r".\assets\images\portal.png",["The Evil Black Mandala","The Container"], 1250, 880)
    transparent_roof1 = Transparent(r".\assets\images\roof.png",50,550,1000,600)
    transparents = [transparent_roof1]

    pygame.display.set_caption("We are getting deeper...into the Truth")

    scene_manager = SceneManager(window)
    scene_manager.tick(30)
    scene_manager.render1(npcs)

    stage_common(npcs,player,walls,transparents,portal,scene_manager,window)

def stage3(window,player):
    player.rect.x = 1600
    player.rect.y = 900
    walls = pygame.sprite.Group()
    walls.add(Wall(0,200,50,50))


    npc1 = NPC(350,880,NpcSettings.Drakura)
    npc2 = NPC(350,300,NpcSettings.Nyarutoru)

    npcs = [npc1,npc2]
    portal = Portal(r".\assets\images\portal.png",["The Vessel of Blood","The Bow Tie of Nyarutoru"], 1250, 880)
    transparent_roof1 = Transparent(r".\assets\images\roof.png",50,550,1000,600)
    transparents = [transparent_roof1]

    pygame.display.set_caption("The Final Chapter.")

    scene_manager = SceneManager(window)
    scene_manager.tick(30)
    scene_manager.render1(npcs)

    stage_common(npcs,player,walls,transparents,portal,scene_manager,window)
