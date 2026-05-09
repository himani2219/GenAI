class NegativeNumberError(Exception):
    def __init__(self, message="Negative numbers are not allowed."):
        self.message = message
        super().__init__(self.message)

def check_number(num):
    if num < 0:
        raise NegativeNumberError()
    else:
        return num
cart=[]
total=0
while True:
    item=input("Enter the item to add to the cart (q to quit):")
    if item.lower() == 'q':
        break
    try:
        it = float(item)
        float_item = check_number(it)
        total += float_item
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
    except NegativeNumberError as e:
        print(e)
        continue
    cart.append(item)
print("Total items: ", len(cart))
print("Items in cart: ", cart)
print("Total bill: ", total)