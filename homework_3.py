class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        wage_plus_bonus = self._income['wage'] + self._income['bonus']
        print(f'{self.position}: {wage_plus_bonus} руб.\n')

if __name__ == '__main__':

    position_instance_1 = Position('Василий', 'Пупкин', 'Утаптыватель тропинок', {'wage': 50000, 'bonus': 20000})
    position_instance_1.get_full_name()
    position_instance_1.get_total_income()

    position_instance_2 = Position('Федор', 'Преображенский', 'Космо-биолог', {'wage': 70000, 'bonus': 30000})
    position_instance_2.get_full_name()
    position_instance_2.get_total_income()
