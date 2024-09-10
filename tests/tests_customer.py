# tests/test_customer.py
import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_create_customer():
    customer = Customer("Alice")
    assert customer.name == "Alice"
    with pytest.raises(ValueError):
        Customer("This name is way too long")

def test_create_order():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = customer.create_order(coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0

def test_coffees():
    customer = Customer("Alice")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Espresso")
    customer.create_order(coffee1, 5.0)
    customer.create_order(coffee2, 3.0)
    assert set(customer.coffees()) == {coffee1, coffee2}

def test_most_aficionado():
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    coffee = Coffee("Latte")
    customer1.create_order(coffee, 5.0)
    customer1.create_order(coffee, 2.0)
    customer2.create_order(coffee, 3.0)
    assert Customer.most_aficionado(coffee) == "Alice"

