w = [12, 1, 2]
sp = [3, 4, 5]
su = [6, 7, 8]
au = [9, 10, 11]
# md = {'Это зима!': w, 'Это весна': sp, 'Это лето!': su, 'Это осень!': au}
md = {1: 'Это зима!', 2: 'Это весна', 3: 'Это лето!', 4: 'Это осень!'}
n = int(input('Введите значение месяца в формате 1 -12: '))
if n in w:
    print(md.pop(1))
if n in sp:
    print(md.pop(2))
if n in su:
    print(md.pop(3))
if n in au:
    print(md.pop(4))
