# imports
from coffeeshop.coffee import Coffee
from coffeeshop.customer import Customer


class Order:
    def __init__(self, customer: Customer, coffee: Coffee, quantity: int, price: float):
        if not isinstance(customer, Customer):
            raise ValueError("Customer must be an instance of Customer.")
        if not isinstance(coffee, Coffee):
            raise ValueError("Coffee must be an instance of Coffee.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number.")
        
        self._customer = customer
        self._coffee = coffee
        self._quantity = quantity
        self._price = price
        
        coffee.add_order(self)  # Add this order to the coffee's list of orders
        customer.create_order(coffee, price)  # Add this order to the customer's list of orders

    @property
    def customer(self):
        return self._customer
    
    @property
    def coffee(self):
        return self._coffee
    
    @property
    def quantity(self):
        return self._quantity
    
    @property
    def price(self):
        return self._price
    
    def __repr__(self):
        return (f"Order(customer={self.customer.name}, coffee_name={self.coffee.name}, "
                f"quantity={self.quantity}, price={self.price})")
