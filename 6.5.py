class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки!')


class Pen(Stationery):
    def draw(self):
        print(f'Рисуем с помощью инструмента {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Рисуем с помощью инструмента {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'Рисуем с помощью инструмента {self.title}')

st = Stationery('Рисование')
st.draw()

a = Pen('Карандаш')
a.draw()

b = Pen('Ручка')
b.draw()

c = Pen('Маркер')
c.draw()
