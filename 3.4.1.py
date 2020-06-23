
# def my_func(x, y):
#     a = 2
#     b = 0
#     while a <= y:
#         def my_f():
#             nonlocal b
#             b = x*x
#             nonlocal a
#             a += 1
#             return b
# v = 1 / my_f()
# return v


# def my_func(x, y):
#     a = 0
#     b = 0
#     while a <= y:
#         b = x * x
#         a = a + 1
#         c = x * b
#     print(1/c)
#
#
# print(my_func(int(input('Введите число, которое возведем в степень: ')),
#               abs(int(input('Введите отрицательное число, в которое бцдем возводить')))))
c = 1

def my_func(x, y):

    for i in range(1, y):
        global c
        c = x * x
        return 1/c



print(my_func(int(input('Введите число, которое возведем в степень: ')),
              abs(int(input('Введите отрицательное число, в которое бцдем возводить')))))
