
n = 1
li = []
anali1 = []
anali2 = []
anali3 = []
anali4 = []
vs = 1
while vs != 0:
    n = 1
    dict1 = dict({'название': input('Введите название товара: '),
                  'цена': input('Введите цену товара: '),
                  'количество': input('Введите количество товара: '),
                  'ед': input('Введите еденицу измерения товара: ')})

    li.append((n, dict1))
    print(li)
    anName = dict1.get('название')
    anPrice = dict1.get('цена')
    anQuantity = dict1.get('количество')
    anMeasure = dict1.get('ед')
    anali1.append(anName)
    anali2.append(anPrice)
    anali3.append(anQuantity)
    anali4.append(anMeasure)
    n += 1
    vs = int(input('Если хотите ввести еще товар - нажмите 1. Если хотите получить аналитику - нажмите 0.'))

print(f'Название: {list(set(anali1))}, Цена: {list(set(anali2))}, Количество: {list(set(anali3))}, Ед: {list(set(anali4))}')
