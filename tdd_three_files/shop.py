"""Простейший магазин: финальная версия после 15 тестов (GREEN)."""


class Shop:
    def __init__(self):
        self.items = []  # Товары: (цена, количество)
        self.discount = 0  # Скидка в процентах
        self.status = "new"  # Новый заказ
        self.history = []  # История операций

    def add(self, price, quantity=1):
        # Разрешаем добавлять товары только в новый заказ.
        if self.status != "new":
            raise ValueError("Заказ уже закрыт")
        if price <= 0 or quantity <= 0:
            raise ValueError("Цена и количество должны быть больше нуля")
        self.items.append((price, quantity))

    def total(self):
        # Сумма всех товаров с учётом количества и скидки.
        amount = sum(price * quantity for price, quantity in self.items)
        return round(amount * (100 - self.discount) / 100, 2)

    def set_discount(self, percent):
        # Допускаем только скидки от 0 до 100%.
        if not 0 <= percent <= 100:
            raise ValueError("Неверная скидка")
        self.discount = percent

    def pay(self, money):
        # Оплата условная, никакой связи с банком нет.
        if self.status != "new":
            raise ValueError("Заказ уже обработан")
        if not self.items:
            raise ValueError("Корзина пуста")
        if money < self.total():
            raise ValueError("Недостаточно денег")
        self.status = "paid"
        self.history.append("paid")
        return round(money - self.total(), 2)  # Сдача

    def cancel(self):
        # Отменить можно лишь неоплаченный заказ.
        if self.status != "new":
            raise ValueError("Отменить нельзя")
        self.status = "cancelled"
        self.history.append("cancelled")

    def refund(self):
        # Возврат разрешён только после оплаты.
        if self.status != "paid":
            raise ValueError("Оплаты ещё не было")
        self.status = "refunded"
        self.history.append("refunded")
        return self.total()
