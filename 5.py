n = int(input('Введите вашу выручку за год: '))
while n < 0:
    n = int(input('Выручка не может быть отрицательной. Введите положительное число: '))
    if n > 0:
        continue

m = int(input('Введите ваши издержки за год: '))
while m < 0:
    m = int(input('Ихдержки не могут быть отрицательными. Вы же потратили деньги... Введите положительное число: '))
    if m > 0:
        continue
if m == n == 0:
    print('0 - тоже неплохо :)')
else:
    v = n - m
    R = v / n

    if m > n:
        print(f'Вы работаете с убытком! Ваш убыток = {m - n}.')
    elif m == n:
        print('0 - тоже неплохо :)')
    else:
        print(f'Вы работаете с прибылью! Ваша прибыль = {n - m}! Рентабельность {R:.2f}.')
        q = int(input('Введите количество сотрудников: '))
        print(f'Прибыль на 1 сотрудника составляет: {v / q}')
