class Car():
    def __init__(self, brand, color, speed):
        self.brand = brand
        self.color = color
        self.max_speed = speed

    def advr(self):

        print('only this black friday {} {} {}-kmh for half price!!!'.
              format(self.brand, self.color, self.max_speed))


lamborghini = Car('lambo', 'black', 600)

lamborghini.advr()