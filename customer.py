from coffee import Coffee

class Customer:
    def __init__(self, name: str):
        if not isinstance(name, str) or not (1 <= len(name) <= 20):
            raise ValueError("Name must be a string between 1 and 20 characters.")
        self.name = name
        self._orders = []

    def display_info(self):
        print(f"Name: {self.name}")

    def create_order(self, coffee_items: dict):
        # Local imports to avoid circular import issues
        from orders import Order
        
        if not isinstance(coffee_items, dict):
            raise ValueError("Coffee items should be provided as a dictionary.")
        
        # Ensure all coffee items are valid Coffee instances and quantities are positive
        for coffee, quantity in coffee_items.items():
            if not isinstance(coffee, Coffee) or quantity <= 0:
                raise ValueError("Invalid coffee instance or non-positive quantity.")
        
        # Create the order
        order = Order(self, coffee_items)
        self._orders.append(order)
        for coffee in coffee_items.keys():
            coffee.add_order(order)
        return order

    def orders(self):
        return self._orders
