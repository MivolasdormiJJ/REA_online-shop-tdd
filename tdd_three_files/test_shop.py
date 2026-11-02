"""Тесты пишем ПЕРЕД кодом: сначала они должны падать (RED)."""
import unittest
from shop import Shop


class TestShop(unittest.TestCase):
    def test_01_empty_cart(self):
        # Пустая корзина стоит 0 рублей.
        shop = Shop()
        self.assertEqual(shop.total(), 0)

    def test_02_one_item(self):
        # Один товар за 100 рублей.
        shop = Shop()
        shop.add(100)
        self.assertEqual(shop.total(), 100)

    def test_03_two_items(self):
        # Два товара: 100 + 50 = 150.
        shop = Shop()
        shop.add(100)
        shop.add(50)
        self.assertEqual(shop.total(), 150)

    def test_04_not_enough_money(self):
        # Если денег меньше стоимости, оплата запрещена.
        shop = Shop()
        shop.add(100)
        with self.assertRaises(ValueError):
            shop.pay(50)

    def test_05_successful_payment(self):
        # Оплата 150 рублей за товар ценой 100: сдача 50.
        shop = Shop()
        shop.add(100)
        self.assertEqual(shop.pay(150), 50)


if __name__ == "__main__":
    unittest.main()
