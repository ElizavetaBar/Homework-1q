class Ceil:
    def __init__(self, qua):
        self.qua = qua

    def __str__(self):
        return f'{self.qua}'

    def __add__(self, other):
        return Ceil(self.qua + other.qua)

    def __sub__(self, other):
        return self.qua - other.qua if (self.qua - other.qua) > 0 else print('Некорректно!')

    def __mul__(self, other):
        return Ceil(self.qua * other.qua)

    def __truediv__(self, other):
        if other.qua == 0:
            print('На ноль делить нельзя!')
        else:
            return Ceil(self.qua // other.qua)

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.qua / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.qua % cells_in_row)}'
        return row


ceil1 = Ceil(56)
ceil2 = Ceil(11)
print(f'Сумма: {ceil1 + ceil2}')
print(f' Разность: {ceil1 - ceil2}')
print(f' Умножение: {ceil1 * ceil2}')
print(f' Деление: {ceil1 / ceil2}')
print(f'Клетка 1: {ceil1.make_order(6)}\n')
print(f'Клетка 2: {ceil2.make_order(8)}\n')
