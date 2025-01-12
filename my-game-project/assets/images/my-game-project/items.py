
class Items:
    def __init__(self,statistics,discription):
        self.attack = statistics[0]
        self.defense = statistics[1]
        self.health = statistics[2]
        self.moves = statistics[3]
        self.equipped = False
        self.discription = discription

    def statistics_adding(self,player):
        if not self.equipped:
            player.attack += self.attack
            player.defense += self.defense
            player.health += self.health
            player.moves += self.moves
            self.equipped = True