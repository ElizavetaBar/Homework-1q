def simple(**kwargs):
    return kwargs


print(simple(имя=input('Введите имя: '),
             фамилия=input('Введите фамилию: '),
             год=input('Введите год рождения: '),
             город=input('Введите город проживания'),
             почта=input('Введите e-mail: '),
             телефон=input('Введите телефон: ')))
