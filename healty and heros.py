class character:
    def __init__(self, age, healthy):
        self.age = age
        self.healthy = healthy

    def get_name(self):
        return self._name

    def get_health(self):
        return self._healthy

    def set_health(self, healthy):
        if healthy >= 0:
        else:
            print("ошибка хп не можеть бить менше нула")

    def attack(self):
        print(f'{self.name}атакує!')

    def take_damage(self, amount):
        if amount > 0:
            self.set_healthy(self.healthy - amount)
            print(f"{self._name}здох")

    def is_alive(self):
        return self.healthy > 0

class tank(character):
    def __int__(self, name):
        super().__init__(name, healthy=250)
        self.__weapon = "мозний меч"

    def attack(self):
        print(f"{self.get_name()}атакує мечом!!!")

class speedy(Character):
    def __init__(self, name):
        super().__init__(name, health=35)  # Менше здоров'я
        self.__spell = "маленкий нож"

    def attack(self):
        print(f"{self.get_name()} атакує ножом!")

tank = tank("Артур")
speedy = speedy("Мерлін")

print(f"Ім'я танка: {tank.get_name()}, Здоров'я: {tank.get_health()}")
print(f"Ім'я скоростник: {speedy.get_name()}, Здоров'я: {speedy.get_health()}")

tank.attack()
speedy.attack()

tank.take_damage(125)
print(f"Здоров'я танка: {tank.get_health()}")

speedy.take_damage(125)
print(f"скоростник живий? {speedy.is_alive()}")
