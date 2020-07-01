subject = {}
with open('text_6.txt', 'r+', encoding='utf-8') as loly:
    for line in loly:
        name, s = line.split(':')
        name_s = sum(map(int, ''.join([i for i in s if i == '' or (i >= '0' and i <= '9')]).split()))
        subject[name] = name_s
print(f'{subject}')
