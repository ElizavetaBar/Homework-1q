from itertools import count
from math import factorial


def fact(n):
    for el in count(1):
        yield factorial(el)


c = int(input('Факториал какого числа вы хотите получить: '))
a = fact(c)

x = 0

for i in a:
    if x < c:
        print(i)
        x += 1
    else:
        break

