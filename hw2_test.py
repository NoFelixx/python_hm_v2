from hw2 import Order, morning_discount, elder_discount
def test_morning_discount():
    order = Order(100, morning_discount)
    assert order.final_price() == 75

def test_elder_discount():
    order = Order(100, elder_discount)
    assert order.final_price() == 90
