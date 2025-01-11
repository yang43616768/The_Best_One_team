from enum import Enum
from items import *

class WindowsSettings:
    name = 'Card battle revolution'
    width = 1500
    height = 900
    OutdoorScale = 2

class PlayerSettings:
    playerSpeed = 15
    playerWidth = 63.5
    playerHeight = 75
    playerHealth = 200
    playerAttack = 5
    PlayerDefense = 3
    PlayerMoves = 3

class NpcSettings:

    # 通用提示
    CommonSense = '''Your should response with less than 15 words.
    Here is some common sense you should know:
    1.This is a turn based card game named "card battle revolution" where players can counter their opponents by playing attack and defense cards.
    2.All resources,incluing health,attack,defense and moves,can be gained by purchasing in the NPC shop.The only way to gain resources is to defeat the NPCs for rewards.
    3.The health lost in battle will be restored after the end (regardless of success or failure).So don't worry about the health loss and try to defeat the NPCs.
    4.Each NPC has a unique dialogue system, and the player can talk with the NPC by pressing the "E" key.
    5.The player can move with the "WASD" keys.
    6.The player can fight with the NPC by pressing the "F" key.
    7.The player can purchase resources from the NPCs by pressing the "B" key.
    8.In each fight, the player can play a card to attack or defend by pressing "Q"and"E". The player can play up to 3 cards in each round initially.
    9.Some efficient tools can be purchased in the NPC shop to increase the number of cards played in each round.
    10.The player can press the "I" key to check the inventory and his current ability values.
    '''

    # Lilia 莉莉娅
    Task_Lilia = '''You are Lilia,a guiding NPC in a game world.You are sweet and kind-hearted.You like to eat sweet food.
    The player has just come to this world and needs your guidance.
    When the input involves about your identity or the setting of this game,
    you should tell him who you are and what you can do for him.
    '''+CommonSense
    dialogue1 = {"role": "system", "content":Task_Lilia}
    items1 = [("A worn-out helmet", 10), ("A worn-out armor", 20), ("A worn-out short sword", 30)]
    photopath1_1 = r".\assets\images\npc1.1.png"
    photopath1_2 = r".\assets\images\npc1.2.png"
    reward1 = 'The Legendary Sword'
    currency1 = 100
    health1 = 50
    attack1 = 20
    bubble_text1_1 = 'Press "E" to talk to me.'
    bubble_text1_2 = 'Press "B" to buy items.'
    bubble_text1_3 = 'Press "F" to fight with me.'
    Lilia = [dialogue1,items1,photopath1_1,photopath1_2,reward1,currency1,health1,attack1,"Lilia",[bubble_text1_1,bubble_text1_2,bubble_text1_3],1]

    #Berries 果酱
    Task_Berries = '''You are Berries, a merchant NPC in a game world.
    You are a little greedy and you like to tease the player.
    When the input involves about your identity or the setting of this game,
    you should tell him who you are and what you can do for him.
    '''+CommonSense
    dialogue2 = {"role": "system", "content":Task_Berries}
    items2 = [("Tears of the Dragon", 100), ("Dragon Soul", 40), ("Dragon bone", 60)]
    photopath2_1 = r".\assets\images\npc2.1.png"
    photopath2_2 = r".\assets\images\npc2.2.png"
    reward2 = "The Legendary Armor"
    currency2 = 150
    health2 = 50
    attack2 = 20
    bubble_text2_1 = "I like your dress!It's pretty."
    bubble_text2_2 = "Do you know there's a strange guy at the end of the Magic Forest?"
    bubble_text2_3 = 'Try wandering around!'
    Berries = [dialogue2,items2,photopath2_1,photopath2_2,reward2,currency2,health2,attack2,"Berries",[bubble_text2_1,bubble_text2_2,bubble_text2_3],1]

    #Irin_Evil 璃音
    Task_Irin_Evil = '''You are Irin, a hostile NPC in a game world.
    You are evil and you are trying to make a scene.
    You are determined to stop the player here at any cost.
    When the input involves about your identity or the setting of this game,
    you should express your contemptuous attitude.
    '''+CommonSense 
    dialogue3 = {"role": "system", "content":Task_Irin_Evil}
    items3 = [("Undifined1", 9999), ("Undifined2", 9999), ("Undifined3", 9999)]
    photopath3_1 = r".\assets\images\npc3.1.png"
    photopath3_2 = r".\assets\images\npc3.2.png"
    reward3 = "The Evil Black Mandala"
    currency3 = 100
    health3 = 250
    attack3 = 40
    bubble_text3_1 = 'I will stop you.'
    bubble_text3_2 = 'I am no longer her.'
    bubble_text3_3 = 'I am the embodiment of evil'
    Irin_Evil = [dialogue3,items3,photopath3_1,photopath3_2,reward3,currency3,health3,attack3,"Evil Irin",[bubble_text3_1,bubble_text3_2,bubble_text3_3],2]
    
    #Sakura 樱
    Task_Sakura = '''You are Sakura,a NPC with senior status in a game world.
    You are wise and have a high level of combat power.
    You are afraid of the player's strength and want to test the player's strength.
    You want to see if the player is qualified to defeat the final boss.
    When the input involves about your identity or the setting of this game,
    you should persuade the player not to move forward anymore.
    '''+CommonSense
    dialogue4 = {"role": "system", "content":Task_Sakura}
    items4 = [("The Principal's Pcepter", 150), ("Undifined2", 9999), ("Undifined3", 9999)]
    photopath4_1 = r".\assets\images\npc4.1.png"
    photopath4_2 = r".\assets\images\npc4.2.png"
    reward4 = "The philosopher's stone"
    currency4 = 100
    health4 = 700
    attack4 = 30
    bubble_text4_1 = 'I have seen too many young people like you before.'
    bubble_text4_2 = 'They accidentally entered the forest and got lost in the darkness.'
    bubble_text4_3 = 'You need to be aware of the cost of delving deeper into it.'
    Sakura = [dialogue4,items4,photopath4_1,photopath4_2,reward4,currency4,health4,attack4,"Sakura",[bubble_text4_1,bubble_text4_2,bubble_text4_3],1]

    #Nyakori 喵可莉
    Task_Nyakori = '''You are Nyakori,a NPC.
    You are a foodie who likes to eat snacks. 
    You were once a friend of the player, but now the player has lost his memory and doesn't know you.
    When the input involves about your identity or the setting of this game,
    You should encourage players to move forward bravely.
    '''+CommonSense
    dialogue5 = {"role": "system", "content":Task_Nyakori}
    items5 = [("A bag of crisps", 15), ("Friendship necklace", 75), ("Kitties Cookies", 20)]
    photopath5_1 = r".\assets\images\npc5.1.png"
    photopath5_2 = r".\assets\images\npc5.2.png"
    reward5 = "The Legendary Armor"
    currency5 = 150
    health5 = 500
    attack5 = 20
    bubble_text5_1 = 'Have you seen my potato chips?'
    bubble_text5_2 = "Don't you remember me?"
    bubble_text5_3 = "We were best friends before you lost your memory..."
    Nyakori = [dialogue5,items5,photopath5_1,photopath5_2,reward5,currency5,health5,attack5,"Nyakori",[bubble_text5_1,bubble_text5_2,bubble_text5_3],1]

    #Eliza 心渊
    Task_Eliza = '''You are Eliza,a NPC.
    You are timid and socially anxious, and don't like to socialize,
    but you and Berries are good friends. 
    You guard the magical forest and prevent outsiders from entering danger.
    When the input involves about your identity or the setting of this game,
    you should persuade the player not to move forward anymore.
    '''+CommonSense
    dialogue6 = {"role": "system", "content":Task_Eliza}
    items6 = [("The Hat of the Forest Guardian", 40), ("The Coat of the Forest Guardian", 30), ("The Boots of the Forest Guardian", 20)]
    photopath6_1 = r".\assets\images\npc6.1.png"
    photopath6_2 = r".\assets\images\npc6.2.png"
    reward6 = 'The Legendary Shield'
    currency6 = 150
    health6 = 400
    attack6 = 20
    bubble_text6_1 = 'I like wondering around with Berries...Have you seen her?'
    bubble_text6_2 = 'You shall not...enter the magical forest.'
    bubble_text6_3 = 'I will take everyone seriously and protect them.'
    Eliza = [dialogue6,items6,photopath6_1,photopath6_2,reward6,currency6,health6,attack6,"Eliza",[bubble_text6_1,bubble_text6_2,bubble_text6_3],1]

    #Irin 璃音
    Task_Irin = '''You are Irin,a friendly NPC in a game world.
    You were deceived and used as a container to seal evil.
    You hope that players can break the sealed evil replica of yourself, go deep into the altar, and find the truth.
    '''+CommonSense
    dialogue7 = {"role": "system", "content":Task_Irin}
    items7 = [("A Pure Heart", 100), ("Undifined2", 9999), ("Undifined3", 9999)]
    photopath7_1 = r".\assets\images\npc7.1.png"
    photopath7_2 = r".\assets\images\npc7.2.png"
    reward7 = "The Container"
    currency7 = 200
    health7 = 700
    attack7 = 30
    bubble_text7_1 = 'I bear the mission of becoming The Container.'
    bubble_text7_2 = 'Evil will be forever sealed ... until your arrival.'
    bubble_text7_3 = 'Break the seal,find the Truth.'
    Irin = [dialogue7,items7,photopath7_1,photopath7_2,reward7,currency7,health7,attack7,"Irin",[bubble_text7_1,bubble_text7_2,bubble_text7_3],2]

    #Lianne 莲
    Task_Lianne = '''You are Lianne,a NPC.
    You are the mysterious librarian in the tower, and you have a deep affection for the ancient knowledge in books. 
    To protect this tower, you hope to prevent players from breaking the seal.
    You should persuade the player not to move forward anymore.
    '''+CommonSense
    dialogue8 = {"role": "system", "content":Task_Lianne}
    items8 = [("The Gloves of the Librarian", 50), ("The Magnifying Glass of the Librarian", 50), ("Undefined3", 9999)]
    photopath8_1 = r".\assets\images\npc8.1.png"
    photopath8_2 = r".\assets\images\npc8.2.png"
    reward8 = "The Book of All Things"
    currency8 = 200
    health8 = 700
    attack8 = 30
    bubble_text8_1 = 'I like to smell the pages of the book.'
    bubble_text8_2 = 'I manage everything in the library.'
    bubble_text8_3 = 'Sealing is necessary to protect the tower...'
    Lianne = [dialogue8,items8,photopath8_1,photopath8_2,reward8,currency8,health8,attack8,"Lianne",[bubble_text8_1,bubble_text8_2,bubble_text8_3],2]

    #Theia 缇娅
    Task_Theia = '''You enjoy conducting experiments and using your own developed robots to make decisions. 
    You have a lot of knowledge.
    You don't care about the essence of the world, 
    but you are curious about the sincere player and willing to provide help.
    '''+CommonSense
    dialogue9 = {"role": "system", "content":Task_Theia}
    items9 = [("A Hard Wrench", 30), ("The Star Ring", 50), ("The Robot Fortifier", 20)]
    photopath9_1 = r".\assets\images\npc9.1.png"
    photopath9_2 = r".\assets\images\npc9.2.png"
    reward9 = "A Faulty Robot"
    currency9 = 200
    health9 = 700
    attack9 = 30
    bubble_text9_1 = "Hello, let's say hello to the little robot"
    bubble_text9_2 = "The Truth? It's nothing to do with me."
    bubble_text9_3 = "I am still busy repairing my experiment."
    Theia = [dialogue9,items9,photopath9_1,photopath9_2,reward9,currency9,health9,attack9,"Theia",[bubble_text9_1,bubble_text9_2,bubble_text9_3],2]

    #Drakura 德古拉
    Task_Drakura = '''You are a vampire duke with powerful bloodline power. 
    You want to compete with powerful players out of curiosity.
    '''+CommonSense
    dialogue10 = {"role": "system", "content":Task_Drakura}
    items10 = [("Undifined1", 9999), ("Undifined2", 9999), ("Undifined3", 9999)]
    photopath10_1 = r".\assets\images\npc10.1.png"
    photopath10_2 = r".\assets\images\npc10.2.png"
    reward10 = "The Vessel of Blood"
    currency10 = 100
    health10 = 700
    attack10 = 30
    bubble_text10_1 = "I have been endowed with the power of blood."
    bubble_text10_2 = "Disputes, struggles and pains ... What a sweet taste."
    bubble_text10_3 = "Interesting guy. I am longing to fight with you."
    Drakura = [dialogue10,items10,photopath10_1,photopath10_2,reward10,currency10,health10,attack10,"Drakura",[bubble_text10_1,bubble_text10_2,bubble_text10_3],3]

    #Nyarutoru 喵露朵露薇
    Task_Nyarutoru = '''You are a remnant of the player's past.
    Unlike players, you still hold onto your past memories.
    You are an existence created by the influence of evil fissures,
    and your mission is to defeat players and turn the entire world into the master of darkness.
    '''+CommonSense
    dialogue11 = {"role": "system", "content":Task_Nyarutoru}
    items11 = [("Undifined1", 9999), ("Undifined2", 9999), ("Undifined3", 9999)]
    photopath11_1 = r".\assets\images\npc11.1.png"
    photopath11_2 = r".\assets\images\npc11.2.png"
    reward11 = "The Bow Tie of Nyarutoru"
    currency11 = 100
    health11 = 700
    attack11 = 30
    bubble_text11_1 = "I am the Past of you."
    bubble_text11_2 = "I was born from evil."
    bubble_text11_3 = "Darkness will eventually annihilate the world."
    Nyarutoru = [dialogue11,items11,photopath11_1,photopath11_2,reward11,currency11,health11,attack11,"Nyarutoru",[bubble_text11_1,bubble_text11_2,bubble_text11_3],3]
    
class SceneSettings:
    tileXnum = 120
    tileYnum = 72
    tileWidth = tileHeight = 25


class Gamepath:
    player = r".\assets\images\player.png"

    groundTiles1 = [
        r".\assets\tiles\grass12.png",
        r".\assets\tiles\grass13.png",
        r".\assets\tiles\grass14.png",
        r".\assets\tiles\grass15.png",
        r".\assets\tiles\grass16.png",
        r".\assets\tiles\grass17.png",
        r".\assets\tiles\grass18.png",
        r".\assets\tiles\grass19.png",
        r".\assets\tiles\grass20.png",
        r".\assets\tiles\grass21.png",
        r".\assets\tiles\grass22.png",
    ]
    groundTiles2 = [
        r".\assets\tiles\stage2-1.png",
        r".\assets\tiles\stage2-2.png",
        r".\assets\tiles\stage2-3.png",
        r".\assets\tiles\stage2-4.png",
        r".\assets\tiles\stage2-5.png",
        r".\assets\tiles\stage2-6.png",
    ]

    tree = r".\assets\tiles\tree.png"

class Item_List:
#   物品名 = Items([攻击力,防御力,生命值,步数])
    The_Legendary_Sword = Items([10,0,0,0],'A peerless sword in the world')
    The_Legendary_Shield = Items([0,10,0,0],'A peerless shield in the world')
    The_Evil_Black_Mandala = Items([-5,0,40,0],'A black mandala that brings evil')
    The_Legendary_Armor = Items([-5,0,100,0],'An ancient armor')
    A_worn_out_helmet = Items([0,1,0,0],"It's a bit worn out...But it can still be used")
    A_worn_out_armor = Items([0,0,2,0],"It's a bit worn out...But it can still be used")
    A_worn_out_short_sword = Items([3,0,0,0],"It's a bit worn out...But it can still be used")
    Tears_of_the_Dragon = Items([0,5,0,1],'Do you hear the dragon crying?')
    Dragon_Soul = Items([0,0,20,0],'The soul of the dragon')
    Dragon_bone = Items([4,0,10,0],'A bit horrible...Do you want to hear the story behind it?')
    The_philosophers_stone = Items([4,2,10,1],'Pure Legend——Only the highest hero can become the holder')
    The_Container = Items([5,5,10,0],"What do you want to fill it with, justice, evil, desire, or just love?")
    The_Book_of_All_Things = Items([0,0,20,1],"What lies behind endless knowledge?")
    A_Faulty_Robot = Items([0,6,20,0],"An intelligent robot...It may be able to protect you")
    The_Vessel_of_Blood = Items([10,0,15,0],"The blood inside is still steaming hot...")
    The_Bow_Tie_of_Nyarutoru = Items([5,5,15,1],"I am the PAST of you")
    The_Principals_Pcepter = Items([5,0,20,0],"The symbol of the principal's supreme power")
    A_bag_of_crisps = Items([0,0,10,0],"Yummy!")
    Friendship_necklace = Items([0,4,0,0],"The symbol of our friendship")
    Kitty_Cookies = Items([0,0,15,0],"Yummy!")
    The_Hat_of_the_Forest_Guardian = Items([0,2,0,0],"Old styles never go out of style")
    The_Coat_of_the_Forest_Guardian = Items([0,2,0,0],"Old styles never go out of style")
    The_Boots_of_the_Forest_Guardian = Items([0,2,0,0],"Old styles never go out of style")
    A_Pure_Heart = Items([0,3,20,0],"It's still beating")
    The_Gloves_of_the_Librarian = Items([0,2,5,0],"You will need this...Perhaps")
    The_Magnifying_Glass_of_the_Librarian = Items([0,2,5,0],"You will need this...Perhaps")
    A_Hard_Wrench = Items([5,0,0,0],"It hurts!")
    The_Star_Ring = Items([0,0,0,1],"It's shining")
    The_Robot_Fortifier = Items([2,2,0,0],"It improve the performance of robots")

    items = {
        "The Legendary Sword": The_Legendary_Sword,
        "The Legendary Shield": The_Legendary_Shield,
        "The Evil Black Mandala": The_Evil_Black_Mandala,
        "The Legendary Armor": The_Legendary_Armor,
        "A worn-out helmet": A_worn_out_helmet,
        "A worn-out armor": A_worn_out_armor,
        "A worn-out short sword": A_worn_out_short_sword,
        "Tears of the Dragon": Tears_of_the_Dragon,
        "Dragon Soul": Dragon_Soul,
        "Dragon bone": Dragon_bone,
        "The philosopher's stone":The_philosophers_stone,
        "The Container":The_Container,
        "The Book of All Things":The_Book_of_All_Things,
        "A Faulty Robot":A_Faulty_Robot,
        "The Vessel of Blood":The_Vessel_of_Blood,
        "The Bow Tie of Nyarutoru":The_Bow_Tie_of_Nyarutoru,
        "The Principal's Pcepter":The_Principals_Pcepter,
        "A bag of crisps":A_bag_of_crisps,
        "Friendship necklace":Friendship_necklace,
        "Kitties Cookies":Kitty_Cookies,
        "The Hat of the Forest Guardian":The_Hat_of_the_Forest_Guardian,
        "The Coat of the Forest Guardian":The_Coat_of_the_Forest_Guardian,
        "The Boots of the Forest Guardian":The_Boots_of_the_Forest_Guardian,
        "A Pure Heart":A_Pure_Heart,
        "The Gloves of the Librarian":The_Gloves_of_the_Librarian,
        "The Magnifying Glass of the Librarian":The_Magnifying_Glass_of_the_Librarian,
        "A Hard Wrench":A_Hard_Wrench,
        "The Star Ring":The_Star_Ring,
        "The Robot Fortifier":The_Robot_Fortifier,
    }
    keys = items.keys()