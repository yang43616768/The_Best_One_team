from setting import *
import pygame
import map

class SceneManager:
    def __init__(self, window):
        self.map = map.gen_map()
        self.window = window
        self.clock = pygame.time.Clock()
        self.cameraX = 0
        self.cameraY = 0
        self.camera = pygame.Rect(self.cameraX, self.cameraY, WindowsSettings.width * WindowsSettings.OutdoorScale, WindowsSettings.height * WindowsSettings.OutdoorScale)

    def tick(self, fps):
        self.clock.tick(fps)
    
    def get_width(self):
        return WindowsSettings.width * WindowsSettings.OutdoorScale
    
    def get_height(self):
        return WindowsSettings.height * WindowsSettings.OutdoorScale
    
    def update_camera(self, object):
        object.draw(self.window)
        pass

    def render(self):
        for i in range(SceneSettings.tileXnum):
            for j in range(SceneSettings.tileYnum):
                self.window.blit(self.map[i][j], (SceneSettings.tileWidth * i, SceneSettings.tileHeight * j))

    def npc_where(self,npc):
        pass