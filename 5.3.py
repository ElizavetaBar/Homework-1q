with open('text_3.txt', 'r', encoding='utf-8') as loly:
    malo = []
    ave = []

    d = loly.read().split('\n')
    for i in d:
        i = i.split()
        if float(i[1]) < 20000.0:
            malo.append(i[0])
        ave.append(i[1])
    print(f'Оклад меньше 20.000 {malo}, средний оклад {sum(map(float, ave)) / len(ave)}')
