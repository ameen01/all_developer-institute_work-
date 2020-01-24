class Smartponhe:
    def __init__(self, passw, number, brand):
        self.password = passw
        self.number  = number
        self.brand = brand

    def unlock_phne(self,):
        user_pass = input('tybe the password >')
        if user_pass == self.password:
            print(' phone unlooked')
        else:
            print('worng password')

    def face_unlock(self):
        print('face unlocked')


class Lg(Smartponhe):

    def unloc_lg(self):
        print('its open')


class Iphone():

    def __init__(self, passw, number):
        super().__init__(self, passw, number, 'apple')


smart1 = Smartponhe('05688', '0586877','apple')

lg = Lg('0544', '555555', 'lg')
