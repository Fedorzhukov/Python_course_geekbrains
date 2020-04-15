class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.my_dict = {"wage": wage, "bonus": bonus}
        self._income = wage + bonus

class Position(Worker):

    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(self._income)

employee1 = Position('Ivan', 'Ivanov', 'Manager', 100, 300)
employee1.get_full_name()
employee1.get_total_income()


employee2 = Position('Petr', 'Petrov', 'Boss', 10000, 3000000)
employee2.get_total_income()
employee2.get_full_name()
