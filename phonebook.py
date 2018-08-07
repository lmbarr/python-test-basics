class Phonebook:
    def __init__(self):
        self.entries = {}

    def add(self, name, number):
        self.entries[name] = number

    def lookup(self, name):
        return self.entries[name]

    def is_consistent(self):
        cont = 0
        for value in self.entries.values():
            for number in self.entries.values():
                if number[0:3] == value[0:3]:
                    cont = cont + 1
                if cont == 2:
                    return False
            cont = 0
        return True