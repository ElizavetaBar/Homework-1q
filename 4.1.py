from sys import argv

script_name, work, s, p = argv

work = int(work)
s = int(s)
p = int(p)
salary = int(work * s + p)


print('script_name: ', script_name)
print('Выработка в часах: ', work)
print('Ставка в час: ', s)
print('Премия ', p)
print('Зарплата: ', salary)
