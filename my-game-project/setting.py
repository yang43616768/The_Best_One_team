from enum import Enum

class WindowsSettings:
    name = 'Card battle revolution'
    width = 1500
    height = 900
    OutdoorScale = 2

class PlayerSettings:
    playerSpeed = 6
    playerWidth = 63.5
    playerHeight = 75
    playerHealth = 200
    playerAttack = 5
    PlayerDefense = 3
    PlayerMoves = 3

class NpcSettings:
    Task_Alice = '''You are Alice,a guiding NPC in a game world.
    The player has just come to this world and needs your guidance.
    When the input involves about your identity or the setting of this game,
    you should tell him who you are and what you can do for him.
    Your should response with less than 15 words.
    Here is some common sense you should know:
    1.This is a turn based card game named "card battle revolution" where players can counter their opponents by playing attack and defense cards.
    2.All resources,incluing health,attack,defense and moves,can be gained by purchasing in the NPC shop.The only way to gain resources is to defeat the NPCs for rewards.
    3.The health lost in battle will be restored after the end (regardless of success or failure).So don't worry about the health loss and try to defeat the NPCs.
    4.Each NPC has a unique dialogue system, and the player can interact with the NPC by pressing the "E" key.
    5.The player can move with the "WASD" keys.
    6.The player can fight with the NPC by pressing the "F" key.
    7.The player can purchase resources from the NPCs by pressing the "P" key.'''
    dialogue1 = {"role": "system", "content":Task_Alice}
    items1 = [("Item 1", 10), ("Item 2", 20), ("Item 3", 30)]
    photopath1_1 = r".\assets\images\npc1.1.png"
    photopath1_2 = r".\assets\images\npc1.2.png"
    reward1 = 'The lengendary Sword'
    currency1 = 100
    health1 = 50
    attack1 = 20
    Alice = [dialogue1,items1,photopath1_1,photopath1_2,reward1,currency1,health1,attack1]
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
