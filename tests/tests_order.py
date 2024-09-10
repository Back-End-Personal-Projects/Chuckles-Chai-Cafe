# tests/test_order.py
import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_order_creation():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0
    assert coffee.orders() == [order]

def test_invalid_order_price():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    with pytest.raises(ValueError):
        Order(customer, coffee, 11.0)

