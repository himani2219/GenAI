def apply_discount(price, percentage):
    discount_amount = price * (percentage / 100)
    return price - discount_amount

def flat_discount(price):
    return price - 50

