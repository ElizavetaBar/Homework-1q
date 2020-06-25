from itertools import count

a = int(input('Введите число, с которого начнем генерировать числа: '))
b = int(input('Введите число, на котором закончим генерировать список: '))

for el in count(a):
    if el > b:
        break
    else:
        print(el)
