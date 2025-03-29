class product:
    def__int__(self, name, price, quintity, description=""):

            Args:
                name (str): назву товару
                price (float): Ціна товару
                quintity (int): качетсво товару
                description (str, optional): опис товару. Defults to ""

        self.name = name
        self.price = price
        self.quintity = quintity
        self.description = description
    def__str__(self):
        return f"{self.name} - ${self.price:.2f} (В нявности: {self.quintity})"


def is_available(self, quantity_needed=1):

    return self.quantity >= quantity_needed


def decrease_quantity(self, quantity):

    if quantity > self.quantity:
        raise ValueError("Недостатньо товару в наявності.")
    self.quantity -= quantity

class cart:
        def__int__
        self.items = {}
    def add_product(self, quantity, description)
        if not product.is_avalible(quantity):
            raice ValueError(f"Недостатечно товару'(product.name)' в наявності")

    if product is self.items:
        self.items[product.name] += quantity
    else:
        self.items[product] = quantity

        product.decrease_quantity(quantity)


        def remove_product(self, product, quantity=1):

            Args:
                product(product): обект Product, який треба виделить
                quantity(int, optional): Кількість товару, який потрібно видалити. Defaults to 1.

        Raises:
            ValueError: Якщо товару немає в кошику, або намагаються видалити більше, ніж є в кошику.

        if product not in self.items:
            raise ValueError(f"Товар '{product.name}' відсутній у кошику.")

        if quantity > self.items[product]:
            raise ValueError(f"В кошику немає стільки товару '{product.name}'.")

        self.items[product] -= quantity


        product.quantity += quantity

        if self.items[product] == 0:
            del self.items[product]


    def calculate_total(self):
        def calculate_total(self):

            total = 0
            for product, quantity in self.items.items():
                total += product.price * quantity
            return total

        def __str__(self):

            if not self.items:
                return "Кошик порожній."

            cart_str = "Ваш кошик:\n"
            for product, quantity in self.items.items():
                cart_str += f"- {product.name}: {quantity} x ${product.price:.2f} = ${product.price * quantity:.2f}\n"
            cart_str += f"Загальна вартість: ${self.calculate_total():.2f}"
            return cart_str

        if __name__ == '__main__':

            product1 = Product("Футболка", 25.00, 10, "Бавовняна футболка")
            product2 = Product("Джинси", 60.00, 5, "Класичні джинси")
            product3 = Product("Кросівки", 80.00, 8, "Спортивні кросівки")


            cart = Cart()


            try:
                cart.add_product(product1, 2)
                cart.add_product(product2, 1)
                cart.add_product(product3, 1)
            except ValueError as e:
                print(f"Помилка: {e}")
            print(cart)

            try:
                cart.remove_product(product1, 1)
            except ValueError as e:
                print(f"Помілька: {e}")

            print("\nПісля видалення:")
                print(cart)

        try:
        cart.add_product(product1, 15)
    except ValueError as e:
        print(f"\nПомилка при додаванні великої кількості: {e}")

        print(f"\nКількість футболок в магазині: {product1.quantity}")
