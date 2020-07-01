class Worker:
    def __init__(self, name, surname, position, _income, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


a = Position('Иван', 'Иванов', 'Менеджер', {}, 10, 20)
print(f'Полное имя: {a.get_full_name()}.\nДоход: {a.get_total_income()}.')

b = Position('Ольга', 'Иванова', 'Программист', {}, 20, 20)
print(f'Полное имя: {b.get_full_name()}.\nДоход: {b.get_total_income()}.')