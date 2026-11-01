"""15 простых автоматических тестов: по одному на каждую итерацию TDD."""
import pytest
from payment import Order


def test_01_create_order():
    # Новый заказ должен иметь статус new.
    order = Order()
    assert order.status == "new"


def test_02_add_item():
    # Добавленный товар появляется в списке.
    order = Order()
    order.add_item("Книга", 500)
    assert len(order.items) == 1


def test_03_total_one_item():
    # Цена одного товара равна сумме заказа.
    order = Order()
    order.add_item("Книга", 500)
    assert order.total() == 500


def test_04_total_multiple_items():
    # Учитываются разные товары и их количество.
    order = Order()
    order.add_item("Книга", 500, 2)
    order.add_item("Ручка", 50, 3)
    assert order.total() == 1150


def test_05_invalid_quantity():
    # Нельзя добавить товар с отрицательным количеством.
    order = Order()
    with pytest.raises(ValueError):
        order.add_item("Книга", 500, -1)


def test_06_empty_order_cannot_be_paid():
    # Пустой заказ оплачивать нельзя.
    order = Order()
    order.set_payment_method("card")
    with pytest.raises(ValueError):
        order.pay(1000)


def test_07_discount():
    # Скидка 10% уменьшает 1000 рублей до 900.
    order = Order()
    order.add_item("Книга", 1000)
    order.set_discount(10)
    assert order.total() == 900


def test_08_invalid_discount():
    # Скидка больше 100% недопустима.
    order = Order()
    with pytest.raises(ValueError):
        order.set_discount(120)


def test_09_payment_method():
    # Можно выбрать оплату картой.
    order = Order()
    order.set_payment_method("card")
    assert order.payment_method == "card"


def test_10_successful_payment():
    # После оплаты получаем остаток и статус paid.
    order = Order()
    order.add_item("Книга", 500)
    order.set_payment_method("card")
    assert order.pay(1000) == 500
    assert order.status == "paid"


def test_11_not_enough_money():
    # При нехватке денег заказ остаётся новым.
    order = Order()
    order.add_item("Книга", 500)
    order.set_payment_method("card")
    with pytest.raises(ValueError):
        order.pay(100)
    assert order.status == "new"


def test_12_no_double_payment():
    # Дважды оплатить один заказ нельзя.
    order = Order()
    order.add_item("Книга", 500)
    order.set_payment_method("card")
    order.pay(1000)
    with pytest.raises(ValueError):
        order.pay(1000)


def test_13_cancel_order():
    # Новый заказ можно отменить.
    order = Order()
    order.cancel()
    assert order.status == "cancelled"


def test_14_refund():
    # После оплаты можно вернуть условную сумму.
    order = Order()
    order.add_item("Книга", 500)
    order.set_payment_method("card")
    order.pay(1000)
    assert order.refund() == 500
    assert order.status == "refunded"


def test_15_history():
    # История запоминает оплату и возврат по порядку.
    order = Order()
    order.add_item("Книга", 500)
    order.set_payment_method("card")
    order.pay(1000)
    order.refund()
    assert order.history == ["paid", "refunded"]
