class Worker():
    name = ""
    surname = ""
    position = ""
    _income = dict()
    _income["wage"] = 0
    _income["bonus"] = 0
class Position(Worker):
    def get_full_name(self,name,surname,position):
        self.name = name
        self.surname = surname
        self.position = position
        print(self.surname, self.name,"-", self.position)
    def get_total_income(self,wage,bonus):
        self._income["wage"]=wage
        self._income["bonus"] = bonus
        print("Зарплта равна ",self._income["wage"]+self._income["bonus"])
a = Position()
name1 = "Ваня"
surname1 = "Иванов"
position1 = "программист"
wage1 = 10000
bonus1 = 5000
a.get_full_name(name1,surname1,position1)
a.get_total_income(wage1,bonus1)

name1 = input("введите имя ")
surname1 = input("введите фамилию ")
position1 = input("введите должность ")
wage1 = int(input("введите оклад "))
bonus1 = int(input("введите премию "))
a.get_full_name(name1,surname1,position1)
a.get_total_income(wage1,bonus1)
