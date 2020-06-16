mnl = [input('Введите любое значение: ')]
n = 1

while n < 6:
    a = input('Введите любое значение: ')
    n = n + 1
    mnl.append(a)
    print(mnl)

l = int(input('Список есть! Хоите ввести еще значение? Если да - введите 1. '))


while l == 1:
    b = input('Введите любое значение: ')
    mnl.append(b)
    v = input('Введите любое значение: ')
    mnl.append(v)
    print(mnl)
    l = int(input('Список есть! Хоите ввести еще значение? Если да - введите 1. '))

print(mnl)

for i in range(0, len(mnl), 2):
    mnl[i], mnl[i + 1] = mnl[i + 1], mnl[i]
    i += 1
print(mnl)
