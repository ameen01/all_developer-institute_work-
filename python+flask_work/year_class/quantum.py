import random

class quantum():
    def __init__(self, x, p):
        self.postion = x
        self.spin = p

    def rando(self):
        self.postion = random(range(10))
        self.spin = random(float(range(10)))