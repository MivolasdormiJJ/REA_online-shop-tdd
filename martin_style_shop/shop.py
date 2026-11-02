"""Учебный интернет-магазин в стиле TDD: минимальная логика без банковского API.

Порядок появления возможностей описан в TDD_STEPS.md.
"""


class Shop:
    """Корзина и простейшая условная оплата заказа."""

    def __init__(self):
        self.items = []  # Товары как пары (цена, количество)
        self.discount = 0  # Процент скидки
        self.status = "new"
        self.payment_method = None
        self.events = []  # Для наглядной истории операций

    def add(self, price, quantity=1):
        """Положить товар в корзину."""
        if self.status != "new":
            raise ValueError("Заказ уже закрыт")
        if price <= 0 or quantity <= 0:
            raise ValueError("Цена и количество должны быть положительными")
        self.items.append((price, quantity))

    def total(self):
        """Стоимость корзины с учётом скидки."""
        subtotal = sum(price * quantity for price, quantity in self.items)
        return round(subtotal * (100 - self.discount) / 100, 2)

    def set_discount(self, percent):
        """Установить скидку от 0 до 100 процентов."""
        if not 0 <= percent <= 100:
            raise ValueError("Скидка должна быть от 0 до 100")
        if self.status != "new":
            raise ValueError("Заказ уже закрыт")
        self.discount = percent

    def set_payment_method(self, method):
        """Выбрать условный способ оплаты."""
        if self.status != "new":
            raise ValueError("Заказ уже закрыт")
        if method not in ("card", "cash"):
            raise ValueError("Выберите card или cash")
        self.payment_method = method

    def pay(self, balance):
        """Имитировать оплату и вернуть оставшиеся средства.

        Это учебная модель: реальные деньги не переводятся.
        """
        if self.status != "new":
            raise ValueError("Заказ нельзя оплатить повторно")
        if not self.items:
            raise ValueError("Корзина пуста")
        if self.payment_method is None:
            raise ValueError("Способ оплаты не выбран")
        if balance < self.total():
            raise ValueError("Недостаточно средств")
        self.status = "paid"
        self.events.append("paid")
        return round(balance - self.total(), 2)

    def cancel(self):
        """Отменить ещё не оплаченный заказ."""
        if self.status != "new":
            raise ValueError("Можно отменить только новый заказ")
        self.status = "cancelled"
        self.events.append("cancelled")

    def refund(self):
        """Имитировать возврат денег после оплаты."""
        if self.status != "paid":
            raise ValueError("Возврат возможен только после оплаты")
        self.status = "refunded"
        self.events.append("refunded")
        return self.total()
