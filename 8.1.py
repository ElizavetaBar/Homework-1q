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

        if 1 <= d <= 31:
            if 1 <= m <= 12:
                if 2020 >= y > 0:
                    return f'Все верно!'
                else:
                    return f'Год указан неправильно'
            else:
                return f'Месяц указан неправильно'
        else:
            return f'День указан неправильно'

    def __str__(self):
        return f'Сегодня: {Data.spl(self.data)}'


today = Data('5 - 7 - 2020')
print(today)
print(Data.valid(5, 7, 2020))
print(today.valid(5, 12, 20234))
