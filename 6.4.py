import random as rn


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Поехали!')

    def stop(self):
        print('Стоп')

    def turn(self):
        dir_list = ['Лево', 'Право', 'Вперед', 'Назад']
        print(rn.choice(dir_list))

    def show_speed(self):
        print(f'Скорость: {self.speed} км/час')

    def check(self):
        if self.is_police == True:
            print('Это полицейская машина')
        else:
            print('Это не полицейская машина')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Скорость превышена!')
        else:
            print(f'Скорость: {self.speed} км/час')

class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Скорость превышена!')
        else:
            print(f'Скорость: {self.speed} км/час')


class PoliceCar(Car):
    pass


a = TownCar(40, 'Красный', 'Mercedes', False)
a.go()
a.turn()
a.show_speed()
a.check()
a.stop()