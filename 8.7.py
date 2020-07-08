class CompN:

    def __init__(self, p_1, p_2):
        self.p_1 = p_1
        self.p_2 = p_2

    def __add__(self, other):
        return CompN(self.p_1 + other.p_1, self.p_2 + other.p_2)

    def __mul__(self, other):
        print(f'Результат (3 +2i) * (2 - 3i) = ')
        return f'{self.p_1 * other.p_1 - (self.p_2 * other.p_2)} + {self.p_2 * other.p_1} * i'

    def __str__(self):
        return f'Результат (3 +2i) + (2 - 3i) = {self.p_1} + {self.p_2}i'


n = CompN(3, 2)
b = CompN(2, -3)
print(n + b)
print(n * b)
