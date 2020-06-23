from itertools import cycle

a = input('Введите элемент, который будем повторять: ')

b = 0

try:
    for el in cycle(a):
        if b > 15:
            break
        else:
            print(el)
            b += 1
except TypeError:
    print('Введены некорректные данные!')

