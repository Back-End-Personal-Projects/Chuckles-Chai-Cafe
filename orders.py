from coffee import Coffee

class Order:
    def __init__(self, customer, coffee_items):
        # Local imports to avoid circular import issues
        from customer import Customer

        if not isinstance(customer, Customer):
            raise ValueError("Invalid customer instance.")
        if not isinstance(coffee_items, dict) or not all(isinstance(v, int) and v > 0 for v in coffee_items.values()):
            raise ValueError("Coffee items should be a dictionary with positive integer quantities.")
        
        self.customer = customer
        self.coffee_items = coffee_items  # coffee_items is a dictionary of Coffee: quantity
        self.total_price = sum(coffee.price * quantity for coffee, quantity in coffee_items.items())

    def display_info(self):
        print(f"{self.customer.name}, Confirm your order")
        for coffee, quantity in self.coffee_items.items():
            print(f" {quantity} {coffee.drink}, Price: ${coffee.price * quantity}")
        print(f"Total Price: ${self.total_price}")

    def __str__(self):
        items = ', '.join(f"{coffee.drink} x {quantity}" for coffee, quantity in self.coffee_items.items())
        return f"Order by {self.customer.name}: {items} - Total: ${self.total_price}"

