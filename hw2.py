class Order:
    def __init__(self, price, discount_strategy):
        self.price = price
        self.discount_strategy = discount_strategy

    def final_price(self):
        return self.discount_strategy(self.price)

def morning_discount(price):
    return price * 0.25

def elder_discount(price):
    return price * 0.9

order_1 = Order(100, morning_discount)
assert order_1.final_price() == 75

order_2 = Order(100, elder_discount)
assert order_2.final_price() == 90
