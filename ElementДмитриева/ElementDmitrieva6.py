class ElementDmitrieva():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self):
        print("Имя:", self.name)
        print("Символ:", self.symbol)
        print("Число:", self.number)

    @property
    def name_d(self):
        return self.name
    
    @property
    def symbol_d(self):
        return self.symbol
    
    @property
    def number_d(self):
        return self.number

element=ElementDmitrieva("Азот", "N", 7)
element.dump()

print(element.name_d)
print(element.symbol_d)
print(element.number_d)