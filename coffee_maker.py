class CoffeeMaker:
    """Virtual Coffee Maker"""
    def __init__(self) -> None:
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee":100
        }
    
    def report(self):
        """Prints status of the resources"""
        print(f"Water: {self.resources["water"]}ml")
        print(f"Milk: {self.resources["milk"]}ml")
        print(f"Coffee: {self.resources["coffee"]}ml")

    def is_resources_sufficient(self, drink):
        """Returns true if the order can be made using current 
        ingredient. False if insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}")
                can_make = False    
        return can_make
    
    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] = self.resources[item] - order.resources[item]
        print(f"Here is your {order.name} . Enjoy!")