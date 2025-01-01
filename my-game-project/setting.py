from enum import Enum

class WindowsSettings:
    name = 'My Game'
    width = 1500
    height = 900
    OutdoorScale = 2

class PlayerSettings:
    playerSpeed = 5
    playerWidth = 63.5
    playerHeight = 75
    playerHealth = 20
    playerAttack = 5
    PlayerDefense = 3
    PlayerMoves = 3
class SceneSettings:
    tileXnum = 60
    tileYnum = 36
    tileWidth = tileHeight = 25


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