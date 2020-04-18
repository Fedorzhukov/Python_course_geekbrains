class Cell:
    def __init__(self, nucleus):
        self.nucleus = nucleus

    def __add__(self, other):
        result = self.nucleus + other.nucleus
        return result

    def __sub__(self, other):
        result = self.nucleus - other.nucleus
        if result < 0:
            result = 'Ошибка!'
        return result

    def __mul__(self, other):
        return self.nucleus * other.nucleus

    def __truediv__(self, other):
        return (self.nucleus // other.nucleus)

    def make_order(self, num):
        out = ''
        r = self.nucleus // num
        for i in range(r):
            out += '*' * num + '\n'
        out += '*' * (self.nucleus - num * r)
        print(out)


cell1 = Cell(10)
cell2 = Cell(12)
cell3 = Cell(30)

print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 / cell2)

cell3.make_order(11)
