import random


class Dicegame():
    def play(self, players,):
        # bet 10$

        for player in players:
            player.money -= 10

        # rolldice function
        best = 0
        winner = None
        for player in players:
            roll = player.rolldice()
            if 


        # winner take all


class Player:

    def __init__(self, name):
        self.name = list(name)
        self.money = 100

    def rolldice(self,):
        dice_rsualt = random.randint(1, 6)
        return dice_rsualt

plaer1 = Dicegame()
