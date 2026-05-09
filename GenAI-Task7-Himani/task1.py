class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    def get_info(self):
        return f"the product is {self.name} with price {self.price} and category {self.category}"
    

mobile = Product("iPhone", 50000, "Electronics")
macbook = Product("MacBook Pro", 150000, "Electronics")

print(mobile.get_info())
print(macbook.get_info())