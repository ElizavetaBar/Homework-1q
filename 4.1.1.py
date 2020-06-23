from sys import argv

script_name, work, s, p = argv


def my_func():
    try:
        global work
        global s
        global p
        work = int(work)
        s = int(s)
        p = int(p)
        return int(work * s + p)

    except ValueError:
        print('Введены некорректные данные!')


print('script_name: ', script_name)
print('Выработка в часах: ', work)
print('Ставка в час: ', s)
print('Премия ', p)
print('Зарплата: ', my_func())
