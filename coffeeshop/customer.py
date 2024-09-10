# coffeeshop/customer.py

from coffeeshop.coffee import Coffee
from coffeeshop.order import Order

class Customer:
    all_customers = []  # Class variable to keep track of all customers
    
    def __init__(self, name: str):
        if not isinstance(name, str) or not (1 <= len(name) <= 20):
            raise ValueError("Name must be a string between 1 and 20 characters.")
        
        self._name = name
        self._orders = []  # List to store orders for this customer
        Customer.all_customers.append(self)  # Add this customer to the global list

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 20):
            raise ValueError("Name must be a string between 1 and 20 characters.")
        self._name = value

    def create_order(self, coffee: Coffee, price: float) -> Order:
        if not isinstance(coffee, Coffee):
            raise ValueError("Input must be a Coffee instance.")
        if not isinstance(price, (int, float)) or not (1.0 <= price <= 500.0):
            raise ValueError("Price must be a float between 1.0 and 500.0.")
        
        order = Order(self, coffee, 1, price)  # Assume quantity is 1 by default
        self._orders.append(order)
        return order
    
    def orders(self):
        return self._orders
    
    def coffees(self):
        return list(set(order.coffee for order in self._orders))
    
    @classmethod
    def most_aficionado(cls, coffee: Coffee):
        max_spent = 0
        top_customer = None
        for customer in cls.all_customers:
            total_spent = sum(order.price for order in customer.orders() if order.coffee == coffee)
            if total_spent > max_spent:
                max_spent = total_spent
                top_customer = customer
        return top_customer
