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
        k = ''.join(h)
        k.title()
    print(g)
int_func()
