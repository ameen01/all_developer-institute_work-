class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            return print('we have {} in the ZOO'.format(new_animal))

    def prnt_animal(self):
        print("list fo all the animals in the zoo", self.animals)

    def by_animal(self, sell):
        if sell in self.animals:
            self.animals.remove(sell)

    def in_order(self):
        for number, name in enumerate(sorted(self.animals)):
            print('the list of our animals', number+1, name)


zoo = Zoo("b_zoo")
zoo.add_animal('mokey')
zoo.add_animal('gowal')
zoo.add_animal('kingkog')
zoo.add_animal('donkey')
zoo.add_animal('zebra')


zoo.prnt_animal()

zoo.in_order()