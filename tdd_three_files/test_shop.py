"""15 учебных тестов интернет-магазина. Сначала RED, затем GREEN."""
import unittest
from shop import Shop


class TestShop(unittest.TestCase):
    def test_01_empty_cart(self):
        # Пустая корзина стоит 0.
        self.assertEqual(Shop().total(), 0)

    def test_02_one_item(self):
        shop = Shop()
        shop.add(100)
        self.assertEqual(shop.total(), 100)

    def test_03_two_items(self):
        shop = Shop()
        shop.add(100)
        shop.add(50)
        self.assertEqual(shop.total(), 150)

    def test_04_not_enough_money(self):
        shop = Shop()
        shop.add(100)
        with self.assertRaises(ValueError):
            shop.pay(50)

    def test_05_successful_payment(self):
        shop = Shop()
        shop.add(100)
        self.assertEqual(shop.pay(150), 50)

    def test_06_quantity(self):
        # Три товара по 100 стоят 300.
        shop = Shop()
        shop.add(100, 3)
        self.assertEqual(shop.total(), 300)

    def test_07_invalid_price(self):
        # Отрицательная цена запрещена.
        with self.assertRaises(ValueError):
            Shop().add(-10)

    def test_08_invalid_quantity(self):
        # Количество 0 запрещено.
        with self.assertRaises(ValueError):
            Shop().add(100, 0)

    def test_09_discount(self):
        # Скидка 10% от 200 даёт 180.
        shop = Shop()
        shop.add(200)
        shop.set_discount(10)
        self.assertEqual(shop.total(), 180)

    def test_10_invalid_discount(self):
        # Нельзя задать скидку больше 100%.
        with self.assertRaises(ValueError):
            Shop().set_discount(120)

    def test_11_empty_payment(self):
        # Пустую корзину нельзя оплатить.
        with self.assertRaises(ValueError):
            Shop().pay(100)

    def test_12_no_double_payment(self):
        # За один заказ нельзя заплатить дважды.
        shop = Shop()
        shop.add(100)
        shop.pay(100)
        with self.assertRaises(ValueError):
            shop.pay(100)

    def test_13_cancel_order(self):
        # Неоплаченный заказ можно отменить.
        shop = Shop()
        shop.add(100)
        shop.cancel()
        self.assertEqual(shop.status, "cancelled")
        with self.assertRaises(ValueError):
            shop.pay(100)

    def test_14_refund(self):
        # После оплаты можно вернуть стоимость заказа.
        shop = Shop()
        shop.add(100)
        shop.pay(100)
        self.assertEqual(shop.refund(), 100)
        self.assertEqual(shop.status, "refunded")

    def test_15_history(self):
        # История фиксирует оплату и возврат.
        shop = Shop()
        shop.add(100)
        shop.pay(100)
        shop.refund()
        self.assertEqual(shop.history, ["paid", "refunded"])


if __name__ == "__main__":
    unittest.main()
