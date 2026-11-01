"""Учебная система заказов. Оплата условная: реальные деньги не списываются."""


class Order:
    """Один заказ интернет-магазина."""

    def __init__(self):
        self.items = []  # Каждый товар: (название, цена, количество)
        self.discount = 0  # Скидка в процентах
        self.payment_method = None  # Выбранный способ оплаты
        self.status = "new"  # Начальный статус заказа
        self.history = []  # История действий с заказом

    def add_item(self, name, price, quantity=1):
        # Проверяем товар перед добавлением.
        if not name or price <= 0 or quantity <= 0:
            raise ValueError("Некорректный товар")
        if self.status != "new":
            raise ValueError("Изменять оформленный заказ нельзя")
        self.items.append((name, price, quantity))

    def total(self):
        # Складываем цены товаров с учётом количества и скидки.
        amount = sum(price * quantity for _, price, quantity in self.items)
        return round(amount * (100 - self.discount) / 100, 2)

    def set_discount(self, percent):
        # Скидка не может быть меньше 0% или больше 100%.
        if not 0 <= percent <= 100:
            raise ValueError("Скидка должна быть от 0 до 100")
        self.discount = percent

    def set_payment_method(self, method):
        # Поддерживаем два простых учебных варианта.
        if method not in ("card", "cash"):
            raise ValueError("Неизвестный способ оплаты")
        self.payment_method = method

    def pay(self, balance):
        # Вместо подключения к банку используем условный баланс.
        if not self.items:
            raise ValueError("Нельзя оплатить пустой заказ")
        if self.status != "new":
            raise ValueError("Заказ уже обработан")
        if self.payment_method is None:
            raise ValueError("Сначала выберите способ оплаты")
        if balance < self.total():
            raise ValueError("Недостаточно средств")

        self.status = "paid"
        self.history.append("paid")
        return round(balance - self.total(), 2)  # Остаток баланса

    def cancel(self):
        # Отменять можно только ещё не оплаченный заказ.
        if self.status != "new":
            raise ValueError("Отменить можно только неоплаченный заказ")
        self.status = "cancelled"
        self.history.append("cancelled")

    def refund(self):
        # Возврат разрешён только после успешной оплаты.
        if self.status != "paid":
            raise ValueError("Возврат возможен только после оплаты")
        self.status = "refunded"
        self.history.append("refunded")
        return self.total()  # Условная сумма возврата
