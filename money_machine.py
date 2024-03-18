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
    
