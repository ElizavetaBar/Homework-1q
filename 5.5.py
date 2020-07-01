with open('numbers.txt', 'a+', encoding='utf-8') as loly:
    li = input('Введите числа через пробел: ')
    loly.writelines(li)
    numb = li.split()
    print(sum(map(int, numb)))
