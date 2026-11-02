"""Простейший онлайн-магазин. Версия GREEN: все пять тестов проходят."""


class Shop:
    def __init__(self):
        self.items = []  # Список цен товаров

    def add(self, price):
        # Добавляем цену товара в корзину.
        self.items.append(price)

    def total(self):
        # Складываем цены всех товаров в корзине.
        return sum(self.items)

    def pay(self, money):
        # Если денег мало, отклоняем оплату.
        if money < self.total():
            raise ValueError("Недостаточно денег")

        # Если денег достаточно, возвращаем сдачу.
        return money - self.total()
