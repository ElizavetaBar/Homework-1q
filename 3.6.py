# my_word = input('слово из маленьких латинских букв')
# ord(my_word[el])

# def int_func():
#     for el in range(0, len(my_word)):
#         global a
#         a = ord(my_word[el])
#         print(a)
#     print(a)


# print(int_func)


# def int_func():
#     s = set(input('слово из маленьких латинских букв'))
#     for i in s:
#         a = ord(i)
#         if a < 97 or a > 122:
#             s.remove(i)
#         else:
#             continue
#     s = list(s)
#     print(s)
# int_func()
# for i in s:
s = []


def int_func():
    s = list(input('слово из маленьких латинских букв'))
    for i in s:
        a = ord(i)
        if a < 97 or a > 122:
            s.remove(i)
        else:
            continue
    print(''.join(s))


int_func()
