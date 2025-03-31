class bankaccount:
    def__int__(self, name, price, quintity, description=""):

            Args:
                name (str): назву власніка
                number (float): номер  рахунка
                ballans (int): балланс

        self.name = name
        self.number = nuber
        self.ballans = ballans
    def__str__(self):
        return f"{self.name} - ${self.number:.2f} (балланс: {self.ballans})"


def is_available(self, ballans_needed=100):

    return self.ballans >= ballans_needed


def decrease_ballans(self, ballans):

    if ballans > self.ballans:
        raise ValueError("Недостатньо Балланса, Пожалуста повните баланс.")
    self.ballans -= ballans

class Bank:
        def__int__
        self.items = {}
    def add_ballans(self, number, ballans)
        if not number.is_avalible(ballan):
            raice ValueError(f"Недостатечно балланс'(ballans.name)' в наявності")

    if number is self.items:
        self.items[number.name] += ballans
    else:
        self.items[number] = ballans

        ballans.decrease_ballans(number)


        def remove_product(self, number, ballans=1):

            Args:
                number(number): обект ballans, який треба виделить
                ballans(int, optional): Кількість товару, який потрібно видалити. Defaults to 1.

        Raises:
            ValueError: Нема достатечно денг або баллансу.

        if number not in self.items:
            raise ValueError(f"денги у '{number.name}' відсутній .")

        if ballans > self.items[number]:
            raise ValueError(f"Немає стільки баллансу у  '{number.name}'.")

        self.items[ballans] -= number


        ballans.number += ballans

        if self.items[ballans] == 0:
            del self.items[number]


    def calculate_total(self):
        def calculate_total(self):

            total = 0
            for number, ballans in self.items.items():
                total += number.name * ballans
            return total

        def __str__(self):

            if not self.items:
                return "балланс порожній."

            cart_str = "Ваш балланс:\n"
            for ballans, ballans in self.items.items():
                cart_str += f"- {number.name}: {ballans} x ${ballans.number:.2f} = ${number.name * ballans:.2f}\n"
            cart_str += f"Загальна вартість: ${self.calculate_total():.2f}"
            return cart_str

        if __name__ == '__main__':

            number1 = ballans("марка", 25.00, 10, "100000")
            number2 = ballans("Дженни", 60.00, 5, "100000000")
            number3 = ballans("Максима", 80.00, 8, "1000")


            ballans = Bank()


            try:
                ballans.add_ballans(number1, 2)
                ballans.add_ballans(number2, 1)
                ballans.add_ballans(number3, 1)
            except ValueError as e:
                print(f"Помилка: {e}")
            print(ballans)

            try:
                ballans.remove_number(number1, 1)
            except ValueError as e:
                print(f"Помілька: {e}")

            print("\nПісля отмена:")
                print(ballan)

        try:
        number.add_ballan(number1, 15)
    except ValueError as e:
        print(f"\nПомилка при додаванні великої поповненя балланса: {e}")

        print(f"\nКількість балланса в кошелку: {number1.ballans}")
