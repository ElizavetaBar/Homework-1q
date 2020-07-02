with open('my_file_new.txt', 'r+', encoding='utf-8') as loly:
    content = loly.readlines()
    print(f'Количество строк: {len(content)}')

    for i in range(len(content)):
        print(f'Количество слов {i + 1} - ой строки {len(content[i])}')
