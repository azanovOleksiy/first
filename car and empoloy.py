#class Car:
#        self.make = make
#        self.model = model
#        self.year = year
#
#    def get_info(self):
#        return f"{self.year} {self.make} {self.model}"
#
#my_car = Car("БМВ", "6", 2003)
#
#print("Інформація про автомобіль:", my_car.get_info())




class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_info(self):
        return f"{self.name} {self.position} {self.salary}"

employee = Employee("Марк", "менеджер", "150k$")

print("Інформація про працівника:", employee.get_info())

