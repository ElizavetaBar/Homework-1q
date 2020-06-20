def int_func():
    words = input("Input words ")
    g = str(words.split())
    h = list(g)
    for i in h:
        a = ord(i)
        if a < 97 or a > 122:
            h.remove(i)
        else:
            continue
    ''.join(h)
    print(words.title())


int_func()
# s = list(input('слово из маленьких латинских букв').split())
# def int_func():
#     for i in s:
#         a = ord(i)
#         if a < 97 or a > 122:
#             s.remove(i)
#         else:
#             continue
#     ''.join(s)
#
# int_func()
#
#
# for _ in s:
#     print(f'{int_func(_)}, end = ''')

