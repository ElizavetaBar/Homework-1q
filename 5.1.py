text = input('Введите слова: ')
with open('my_file_new.txt', 'a+', encoding='utf-8') as loly:
    while text:
        loly.write('\n' + text)
        text = input('Введите слова: ')
        if not text:
            break
    print(loly.read())
