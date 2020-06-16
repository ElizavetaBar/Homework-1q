n = (input('Введите несколько слов через пробел: '))
a = list(n.split())

for i, v in enumerate(a, 1):
    print(f'{i} - {v[0:10]}')