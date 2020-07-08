class Data:

    def __init__(self, data):
        self.data = str(data) #день - месяц-год


    @classmethod
    def spl(cls, data):
        my_date = []
        for i in data.split():
            if i != '-':
                my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(d, m, y):

        if 1 <= d <= 31 and 1 <= m <= 12 and 2020 >= y > 0:
            print(f'Все верно!')
        else:
            print(f'Указаны некорректные данные!')
        # elif 2020 <= y <= 1:
        #     print(f'Год указан неправильно')
        # elif 12 <= m <= 1:
        #     print(f'Месяц указан неправильно')
        # elif 31 <= d <= 1:
        #     print(f'День указан неправильно')
        # return print()

    def __str__(self):
        return f'Сегодня: {Data.spl(self.data)}'


today = Data('5 - 7 - 2020')
print(today)
today.valid(5, 7, 2020)
today1 = Data('5 - 7 - 2022')
print(today1)
today1.valid(5, 7, 2022)
