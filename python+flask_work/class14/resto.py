class resto():
    def __init__(self):
        self.tables = {'table1': [],
                       'table2': [1, 2, ],
                       'table3': []}
    def emtay_table(self):
        emty = []
        for table, saet in self.tables.items():
            if len(saet) == 0:
                print(table)


my_dict = {'1': [1, 3, 5]}

for key, vale in my_dict.items():
