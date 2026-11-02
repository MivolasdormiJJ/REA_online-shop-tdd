"""15 небольших тестов в порядке «от простого к сложному».

Все тесты использует pytest. Каждый проверяет одно новое правило.
"""
import pytest

from martin_style_shop.shop import Shop


def shop_with_item(price=100, quantity=1):
    """Общий подготовительный код, чтобы тесты было легко читать."""
    shop = Shop()
    shop.add(price, quantity)
    return shop


def test_01_new_shop_is_empty():
    shop = Shop()
    assert shop.total() == 0


def test_02_one_item():
    shop = shop_with_item(100)
    assert shop.total() == 100


def test_03_two_items():
    shop = Shop()
    shop.add(100)
    shop.add(40)
    assert shop.total() == 140


def test_04_item_quantity():
    shop = shop_with_item(80, 3)
    assert shop.total() == 240


def test_05_invalid_quantity():
    shop = Shop()
    with pytest.raises(ValueError):
        shop.add(100, 0)


def test_06_invalid_price():
    shop = Shop()
    with pytest.raises(ValueError):
        shop.add(-10)


def test_07_discount():
    shop = shop_with_item(200)
    shop.set_discount(25)
    assert shop.total() == 150


def test_08_invalid_discount():
    shop = Shop()
    with pytest.raises(ValueError):
        shop.set_discount(150)


def test_09_choose_payment_method():
    shop = Shop()
    shop.set_payment_method("card")
    assert shop.payment_method == "card"


def test_10_successful_payment():
    shop = shop_with_item(100)
    shop.set_payment_method("card")
    assert shop.pay(150) == 50
    assert shop.status == "paid"


def test_11_empty_order_cannot_be_paid():
    shop = Shop()
    shop.set_payment_method("card")
    with pytest.raises(ValueError):
        shop.pay(150)


def test_12_insufficient_balance():
    shop = shop_with_item(100)
    shop.set_payment_method("card")
    with pytest.raises(ValueError):
        shop.pay(50)
    assert shop.status == "new"


def test_13_no_double_payment():
    shop = shop_with_item(100)
    shop.set_payment_method("card")
    shop.pay(150)
    with pytest.raises(ValueError):
        shop.pay(150)


def test_14_cancel_unpaid_order():
    shop = shop_with_item()
    shop.cancel()
    assert shop.status == "cancelled"
    with pytest.raises(ValueError):
        shop.pay(150)


def test_15_refund_and_history():
    shop = shop_with_item(100)
    shop.set_payment_method("card")
    shop.pay(150)
    assert shop.refund() == 100
    assert shop.status == "refunded"
    assert shop.events == ["paid", "refunded"]
