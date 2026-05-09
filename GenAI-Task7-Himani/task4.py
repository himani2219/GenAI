from task2 import Product

class Mobile(Product):
    def __init__(self, name, price, category):
        super().__init__(name, price, category)
    
    def get_info(self):
        return f"this product is of mobile class with name {self.name}, price: {self.get_price()} and category: {self.category}"

class Laptop(Product):
    def __init__(self, name, price, category):
        super().__init__(name, price, category)
    
    def get_info(self):
        return f"this product is of laptop class with name {self.name}, price: {self.get_price()} and category: {self.category}"

if __name__ == "__main__":
    mobile = Mobile("iPhone", 50000, "Electronics")
    laptop = Laptop("MacBook Pro", 150000, "Electronics")

    print(mobile.get_info())
    print(laptop.get_info())