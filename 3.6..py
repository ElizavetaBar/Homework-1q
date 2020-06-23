def my_sum():
    result = 0
    off = 'A'
    while off != 'V':
        my_list = input('Введите числа. Если хотите прекратить - введите V: ').split()
        b = 0

        for el in range(len(my_list)):
            if my_list[el] == 'V':
                off = 'V'
                break
            else:
                b = b + int(my_list[el])
        result = result + b
        print(f'Сумма равна: {result}')


my_sum()
