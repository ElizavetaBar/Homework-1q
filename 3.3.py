def my_func(a, b, c):
    if a < b and a < c:
        return b + c
    elif b < a and b < c:
        return a + c
    elif c < b and c < a:
        return b + a
    else:
        print('Нет минимального значения :(')


print(my_func(int(input('Введите первое значение: ')),
              int(input('Введите второе значение: ')),
              int(input('Введите третье значение: '))))
