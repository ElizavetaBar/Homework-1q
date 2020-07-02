class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        asph = int(input('введите массу асфальта: '))
        th = int(input('введите толщину полотна: '))
        print(f'{(self._length * self._width * asph * th)/1000} тонн')


g = Road(20, 5000)
g.mass()

