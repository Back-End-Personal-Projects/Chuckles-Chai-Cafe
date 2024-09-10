# app.py

from coffeeshop.customer import Customer
from coffeeshop.coffee import Coffee
from coffeeshop.order import Order

def main():
    # Create Coffee objects
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")
    
    # Create Customer objects
    alice = Customer("Alice")
    bob = Customer("Bob")
    
    # Create Orders
    order1 = Order(alice, latte, 1, 450.0)
    order2 = Order(bob, latte, 2, 900.0)
    order3 = Order(bob, espresso, 1, 450.0)
    
    # Display information about Coffee and Customers
    print("Latte Information:")
    latte.display_info()
    
    print("\nEspresso Information:")
    espresso.display_info()
    
    print("\nMost Aficionado for Latte:")
    top_customer = Customer.most_aficionado(latte)
    print(f"{top_customer.name} has spent the most on Latte.")

if __name__ == "__main__":
    main()
