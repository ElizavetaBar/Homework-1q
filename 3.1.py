"""Функция принимает позиционные параметры и производит деление."""

a = int(input('Введите делимое число: '))
b = int(input('Введите делитель: '))


def my_func(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('На ноль делить нельзя!')


print(my_func(a, b))
