class Car():
    def __init__(self, brand, color, speed ,current, capacity):
        self.brand = brand
        self.color = color
        self.max_speed = speed
        self.current_fuel = current
        self.fuel_capacity = capacity

    def advr(self):

        print('only this black friday {} {} {}-kmh for half price!!!'.
              format(self.brand, self.color, self.max_speed))

    def ful_car(self):
        return self.fuel_capacity*2


lamborghini = Car('lambo', 'black', 600)

lamborghini.advr()