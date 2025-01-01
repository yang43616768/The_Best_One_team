from enum import Enum

class WindowsSettings:
    name = 'My Game'
    width = 1280
    height = 720
    OutdoorScale = 1.5

class PlayerSettings:
    playerSpeed = 5
    playerWidth = 63.5
    playerHeight = 75
    playerHealth = 20
    playerAttack = 5
    PlayerDefense = 3
    PlayerMoves = 3
class SceneSettings:
    tileXnum = 48
    tileYnum = 27
    tileWidth = tileHeight = 40


class Gamepath:
    player = r".\assets\images\player.png"

    groundTiles = [
        r".\assets\tiles\ground1.png",
        r".\assets\tiles\ground2.png",
        r".\assets\tiles\ground3.png",
        r".\assets\tiles\ground4.png",
        r".\assets\tiles\ground5.png",
        r".\assets\tiles\ground6.png",
    ]

    tree = r".\assets\tiles\tree.png"