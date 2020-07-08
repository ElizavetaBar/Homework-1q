class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        off = 1
        while off != 0:

            try:
                a = int(input('Введите значения  - '))
                self.my_list.append(a)
                print(f'Текущий список - {self.my_list} \n ')
            except ValueError:
                print(f'Некорректное значение!')

            else:
                off = int(input(f'Попробовать еще раз? Если да - нажмите 1. Если хотите выйти - нажмите 0.'))


ex = Error(1)
print(ex.my_input())
