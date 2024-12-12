class ElementDmitrieva:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

element = ElementDmitrieva("Азот", "N", 7)

print("Имя элемента:", element.name)
print("Символ элемента:", element.symbol)
print("Номер элемента:", element.number)