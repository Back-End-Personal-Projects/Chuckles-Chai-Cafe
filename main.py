from customer import Customer
from coffee import Coffee
from orders import Order

def main():
    # Create coffee instances
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")
    cappuccino = Coffee("Cappuccino")
    americano = Coffee("Americano")
    mocha = Coffee("Mocha")

    # Dictionary to store multiple customers
    customers = {}

    # Display menu
    print("Hey Coffee Lover🍵😋")
    print("Pick your poison:")
    for coffee_name, price in Coffee.menu.items():
        print(f"{coffee_name}: ${price}")

    # Function to create a new customer
    def create_customer():
        while True:
            customer_name = input("Enter the customer's name (or 'done' to finish): ")
            if customer_name.lower() == 'done':
                break

            if customer_name in customers:
                print("Customer already exists.")
                continue

            try:
                customer = Customer(customer_name)
                customers[customer_name] = customer
                print(f"Hello {customer.name}")
            except ValueError as e:
                print(e)

    # Function to create an order for a customer
    def create_order(customer):
        coffee_items = {}
        while True:
            try:
                coffee_name = input("Enter the coffee name you want to order (or 'done' to finish): ")
                if coffee_name.lower() == 'done':
                    break
                
                if coffee_name not in Coffee.menu:
                    print("Selected coffee is not available in the menu.")
                    continue
                
                coffee = Coffee(coffee_name)
                coffee.display_info()
                
                quantity = int(input(f"How many cups of {coffee_name} do you want to order? "))
                if quantity <= 0:
                    raise ValueError("Quantity must be a positive number.")
                
                # Add coffee and quantity to the order
                coffee_items[coffee] = quantity
            
            except ValueError as e:
                print(e)
        
        if coffee_items:
            try:
                order = customer.create_order(coffee_items)
                print("Order placed successfully!")
                order.display_info()
            except ValueError as e:
                print(e)
        else:
            print("No items added to the order.")
    
    # Create customers
    create_customer()

    # Main loop for managing orders
    while True:
        customer_name = input("Enter the customer's name to place an order (or 'done' to finish): ")
        if customer_name.lower() == 'done':
            break

        customer = customers.get(customer_name)
        if not customer:
            print("Customer not found.")
            continue

        while True:
            create_order(customer)
            more_orders = input(f"Would {customer_name} like to place another order? (yes/no): ").strip().lower()
            if more_orders == 'no':
                break
            elif more_orders != 'yes':
                print("Please enter 'yes' or 'no'.")

    # Display all orders for all customers
    print("\nAll orders for all customers:")
    for customer in customers.values():
        print(f"\nOrders for {customer.name}:")
        for order in customer.orders():
            print(order)

if __name__ == "__main__":
    main()
