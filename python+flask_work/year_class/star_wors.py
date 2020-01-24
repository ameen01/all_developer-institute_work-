import random
class Forcewi():
    def __init__(self, name):
        self.name = name
        self.power = random.randrange(1, 15)
        self.wisdom = random.randrange(1, 15)

    def trina(self):
        raise NotImplementedError

    @staticmethod
    def harmmoni(x, y):
        return 2 * x * y / (x + y)

    def fhgit(self, obj):
        if isinstance(obj,self.__class__):
            raise Exception('he shlod be in forcewilder')
        if self.harmmoni(self.power, self.wisdom) > self.harmmoni(self.power ,self.wisdom):
            return self
        elif self.harmmoni(self.power, self.wisdom) < self.harmmoni(self.power ,self.wisdom):
            return obj
        else:
            return None
