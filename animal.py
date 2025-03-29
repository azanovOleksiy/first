class Animal:
    def __int__(self, name, special, age, sound=""):

        Args:
            name (str): Ім` я тварини
            special (str): Вид тварини
            age (int):возраст тварини
            sound (str, option): звук тварини

        self.name = name
        self.pecial = special
        self.age = age
        self.sound = sound


    def make_sound(self):
if self.sound:
            print(f"{self.name} каже: {self.sound}")
        else:
            print(f"{self.name} робить якийсь звук.")

    def __str__(self):
        return f"Ім'я: {self.name}, Вид: {self.species}, Вік: {self.age}"


class Dog(Animal):
    def __init__(self, name, age, breed="Дворняга"):
    Args:
        name(str): Ім'я собаки.
        age(int): Віксобаки.
        breed(str, optional): Породасобаки.Defaults to "Дворняга".


        super().__init__(name, "Собака", age, "Гав!")  # Викликаємо конструктор батьківського класу
        self.breed = breed


    def fetch(self, item):
        Args:
            item (str): Предмет, який собака приносить.

        print(f"{self.name} приносить {item}.")

    def __str__(self):

        return f"{super().__str__()}, Порода: {self.breed}"
    