
class Orgtechnics:
    def __init__(self, a):
        self.a = 'Приветствуем на складе оргтехники! Ваш пароь: 123'
        print(self.a)


    def hi(self, correctpassword = '123'):
        self.correctpassword = correctpassword
        password = int(input('Введите пароль: '))
        while password != 123:
            print('Пароль неверный!')
            password = int(input('Введите пароль: '))
        print('Добро пожаловать!')




class Tech:
    def __init__(self, name, price, qua, *args):
        self.name = name
        self.price = price
        self.qua = qua
        self.org = []
        self.all = {'Марка': self.name, 'Цена': self.price, 'Количество': self.qua}
        self.ext = {}
        # print(f'Есть в наличии: {self.all}')

    def ad(self):
        self.org.append(self.all)

    def st(self):
        print('Здесь можно поработать с техникой. У нас есть: принтер, сканер, ксерокс.')

        try:
            it = input(f'Введите марку ')
            it_o = int(input(f'Введите цену за ед. '))
            it_q = int(input(f'Введите количество '))
            ex = {'Марка': it, 'Цена за ед.': it_o, 'Количество': it_q}
            self.ext.update(ex)
            self.org.append(self.ext)
            print(f'Текущий список -\n {self.org}')
        except:
            return f'Некорректное значение'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f' ')
        if q == 'Q' or q == 'q':
            print(f'Весь склад -\n {self.org}')
        return self.org



class Printer(Tech):
    def to_print(self):
        # print(f'Есть в наличии: {self.org}')
        n = int()
        try:
            n = input('Сколько принтеров отправляем на склад? ')
        except ValueError:
            print('Введено некорректное значение?')
        else:
            return f'передано {n} экземп.'
        return n


class Scanner(Tech):
    def to_scan(self):
        # print(f'Есть в наличии: {self.org}')
        n = int()
        try:
            n = input('Сколько сканеров отправляем на склад? ')
        except ValueError:
            print('Введено некорректное значение?')
        else:
            return f'передано {n} экземп.'
        return n


class Copier(Tech):
    def to_copy(self):
        # print(f'Есть в наличии: {self.org}')
        n = int()
        try:
            n = input('Сколько ксерокосов отправляем на склад? ')
        except ValueError:
            print('Введено некорректное значение?')
        else:
            return f'передано {n} экземп.'
        return n

# потомки принтер ксерокс сканер

a = Orgtechnics(1)
a.hi()

it_1 = Tech('HP', 2300, 10)
it_1.ad()
it_1.st()
it_p = Printer('HP', 2300, 10)
it_p.to_print()
it_c = Copier('Samsung', 2500, 10)
it_c.to_copy()
it_s = Scanner('Dell', 2600, 10)
it_s.to_scan()






