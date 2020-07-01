translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_loly = []

with open('text_4.txt', 'r', encoding='utf-8') as loly:
    line = loly.read().split('\n')
    for i in line:
        i = i.split(' - ', 1)
        new_loly.append(translate[i[0]] + ' - ' + i[1])
    print(new_loly)

with open('text_4_new.txt', 'a', encoding='utf-8') as loly_new:
    loly_new.writelines(new_loly)
