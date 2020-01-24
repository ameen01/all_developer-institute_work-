class Plane():
    def __init__(self,):
        self.sets = {'1A': False, '1B': False, '2A': False, '2B': False}

    def emty_sets(self):
        avaibale = []
        for key, value in self.sets.items():
            if not value:
                avaibale.append(key)
        return avaibale

    def tiket(self,):
        avaibale = self.emty_sets()
        print('hera all the emtay seats')





plane1 = Plane()





plane1 = Plane()

plane1.emty_sets()