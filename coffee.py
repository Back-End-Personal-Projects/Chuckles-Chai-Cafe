class Coffee:
    menu = {
        "Latte": 450.0,
        "Espresso": 450.0,
        "Cappuccino": 400.0,
        "Americano": 350.0,
        "Mocha": 500.0
    }

    def __init__(self, drink: str):
        # Input validation
        if drink not in Coffee.menu:
            raise ValueError("Invalid coffee name. Please choose from the menu.")
       
        self.drink = drink
        self.price = Coffee.menu[drink]
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

       # Print coffee info
    def display_info(self):
        print(f"Coffee Name: {self.drink}")
        print(f"Price: {self.price}")

    def __str__(self):
        return f"{self.drink} - ${self.price}"
     

# For testing purposes
#if __name__ == "__main__":
   # try:
        #my_coffee = Coffee("Latte", 450.0)
        #my_coffee.display_info()
   # except ValueError as e:
        #print(e)
