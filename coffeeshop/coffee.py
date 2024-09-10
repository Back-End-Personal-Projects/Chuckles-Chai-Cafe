#import
from coffeeshop.order import Order


class Coffee:
    menu = {
        "Latte": 450.0,
        "Espresso": 450.0,
        "Cappuccino": 400.0,
        "Americano": 350.0,
        "Mocha": 500.0
    }

    def __init__(self, name: str):
        if not isinstance(name, str) or name not in Coffee.menu:
            raise ValueError("Invalid coffee name.")
        
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or value not in Coffee.menu:
            raise ValueError("Invalid coffee name.")
        self._name = value

    def add_order(self, order: Order):
        if not isinstance(order, Order):
            raise ValueError("Input must be an Order instance.")
        self._orders.append(order)
    
    def orders(self):
        return self._orders
    
    def customers(self):
        return list(set(order.customer for order in self._orders))
    
    def num_orders(self):
        return len(self._orders)
    
    def average_price(self):
        if not self._orders:
            return 0
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders)

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Orders: {self.orders()}")
        print(f"Number of orders: {self.num_orders()}")
        print(f"Average price: {self.average_price()}")
