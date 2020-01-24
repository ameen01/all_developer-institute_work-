import
class Human():


    def __init__(self, name, age):
        self.name = name
        self.age = age

class family:
        def __init__(self, **kwargs):
            self.famliy_tree = {}

            for kay, val in kwargs.items():
                if isinstance(val,Human):
                    self.famliy_tree[kay] = val
                else:
                    raise Exception('all shlod be human')