class Currency:
    def __init__(self, value, label):
        self.value = float(value)
        self.label = label

    def __str__(self):

        return '{}{}'.format(self.value, self.label)

    def __add__(self, other):
        if self.label != self.label:
            return 'not the same the Currency'
        elif self.label == self.label:
            self.value += other
            return self.value, self.label

    def __reduce_ex__(self, protocol):

c1 = Currency(4, "$")
c2 = Currency(2, "$")
print(c1)
print(c1 + c2)
