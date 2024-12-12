class ElementDmitrieva:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print("Имя элемента:", self.name)
        print("Символ элемента:", self.symbol)
        print("Номер элемента:", self.number)

element = ElementDmitrieva("Азот", "N", 7)

element.dump()