class Zero(Exception):

    def __init__(self, txt):
        self.txt = txt



    def zer(self):
        a = int(input('Введите делимое: '))
        b = int(input('Введите делитель: '))

        try:
            res = a/b
        except ZeroDivisionError:
            print('На ноль делить нельзя!')
        else:
            print(res)
        finally:
            print('Хорошего дня!')

Zero.zer('Zero')

