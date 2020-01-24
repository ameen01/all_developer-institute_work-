class Character:
    """character in mini game take  main attributes and 3 main functions"""

    def __init__(self, name, hair_color):
        self.name = name
        self.hair_color = hair_color
        self.life_point = []
        print(self.__class__.init_scream)

    def interodce(self):
        """the character well about himself"""
        print('haloo my name is {}'.format(self.name))

    def change_hair_color(self, nhair_color):
        """1 arg to change the hair color of the character"""
        self.hair_color = nhair_color
        print('my hair color is {}'.format(nhair_color))

    def rest(self):
        """what happen when the character rest"""
        self.life_point = ['♥', '♥', '♥']
        print("{} life_point --{}--".format(self.name, self.life_point))


class Warrior(Character):
    """" all the warrior are in this class"""
    init_scream = "RRRRR"

    def ror(self):
        """what the warrior say"""
        print('{} atRRRR!!!!!'.format(self.name))


class Sorcerer(Character):
    """all the sorcerer function """
    s_scram = "let the killing begin~~"

    def curse(self, name):
        """ Tybe of the sorcerer curse 1 agr """
        print('sweat {}'.format(name))


class Drood(Character):
    """all the do"""
    d_scram = "oh here we go again~~"
    def healer(self):
        """ heal the character"""
        nlife = ['♥', '♥', '♥']


# give name and hair color to your character!!
wor = Warrior('ameen', 'black')
wor2 = Warrior('ad', 'red')






#
#droo = Drood()
## the character life point will back to ♥♥♥
#wor.rest()
#
## change the hair color of the character take 1 arg
#wor.hair_color()
#
## warrior calls needs 2 args name hair color
#warrior = Warrior()
#
## what the character scream
#warrior.ror()
#
#

