import pygame
import random
import sys
from npc import *
from wall import *
from setting import *
from map import *
from SceneManager import *
from player import *
from stage import *

def main():
    pygame.init()
    window = pygame.display.set_mode((WindowsSettings.width, WindowsSettings.height))

    # Stage 0 - Start Screen
    stage0(window)
    player = Player(25,875)
    # Stage 1 - Teaching Section
    stage1(window,player)
    # Stage 2 - In the Tower
    stage2(window,player)
    # Stage 3 - The Final Battle
    stage3(window,player)
if __name__ == "__main__":
    main()

