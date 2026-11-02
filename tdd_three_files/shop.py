"""Учебный магазин. Версия RED: тесты уже есть, но логика пока не написана."""


class Shop:
    def __init__(self):
        self.items = []  # Здесь будут храниться цены товаров

    def add(self, price):
        # TODO: добавить цену товара в список
        pass

    def total(self):
        # TODO: посчитать общую сумму
        return 0

    def pay(self, money):
        # TODO: проверить сумму оплаты и вернуть сдачу
        raise NotImplementedError("Оплата пока не реализована")
