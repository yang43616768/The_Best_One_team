from enum import Enum

class WindowsSettings:
    name = 'default game name'
    width = 1280
    height = 720
    OutdoorScale = 1.5

class PlayerSettings:
    playerSpeed = 5
    playerWidth = 60
    playerHeight = 55

class SceneSettings:
    tileXnum = 48
    tileYnum = 27
    tileWidth = tileHeight = 40


class Gamepath:
    player = r".\assets\player\1.png"

    groundTiles = [
        r".\assets\tiles\tiles\ground1.png",
        r".\assets\tiles\tiles\ground2.png",
        r".\assets\tiles\tiles\ground3.png",
        r".\assets\tiles\tiles\ground4.png",
        r".\assets\tiles\tiles\ground5.png",
        r".\assets\tiles\tiles\ground6.png",
    ]

    tree = r".\assets\tiles\tiles\tree.png"

class GameState(Enum):
    MainMenu = 0
    Game = 1
    Settings = 2
    Exit = 3