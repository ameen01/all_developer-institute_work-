class Vn_machine():
    def __init__(self,):
        self.iteam_list = []

    def add_iteam(self, name, price, amount):
        iteam = {'name': name, 'price': price, 'amuont': amount}
        self.iteam_list.append(iteam)
        return iteam

    def show_vn(self):
        for item in self.iteam_list:
            print(item)

    def sell_iteam(self, name, price):
        all_iteam = self.iteam_list
        for ieam in all_iteam:
            for kay, val in ieam:
                print()




candy = Vn_machine()

candy.add_iteam('milka',13,4)
candy.add_iteam('orio',3,5)
candy.show_vn()

