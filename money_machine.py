class MoneyMachine:

    CURRENCY = "₹"

    COIN_VALUES = {
        "chawanni" : 0.25,
        "atthanni" : 0.5,
        "One" : 1,
        "Two" : 2,
        "Five": 5,
        "Ten" : 10,
        "Twenty":20
    }

    def __init__(self):
        self.profit = 0
        self.money_recieved = 0
    
    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")
    
    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: "))*self.COIN_VALUES[coin]
        return self.money_received
    
    def make_payment(self, cost):
        """Returns true when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_recieved >= cost:
            change = round(self.money_recieved-cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            return True
        else:
            print("sorry that's not enough money. Money refunded.")
            self.money_recieved = 0
            return False