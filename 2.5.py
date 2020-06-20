a = [7, 5, 3, 3, 2]
print(f"Рейтинг - {a}")
b = float(input('Введите элемент рейтинга: '))
while b != 0:

    for el in range(len(a)):
        if a[el] == b:
                a.insert(el + 1, b)
                break

        elif a[0] < b:
                a.insert(0, b)
                break

        elif a[-1] > b:
                a.append(b)
                break

        elif a[el] > b and a[el + 1] < b:
                a.insert(el + 1, b)
                break

    print(f'Наш новый рейтинг: {a}')
    b = float(input('Если вы закночили - введите 0. Если хотите еще ввести данные, продолжаем: '))

