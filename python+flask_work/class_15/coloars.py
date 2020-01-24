class Jug():
    jug_amont = 0

    def __init__(self, whater_in):
        self.whater_in = whater_in
        Jug.jug_amont += 1
        print(Jug.jug_amont)

class coolear():
    def __init__(self, brand):
        self.brand = brand
        self.jag = None

    def add_jag(self, jag):
        self.jag = jag


nug1 = Jug(5)
nug2 = Jug(10)

