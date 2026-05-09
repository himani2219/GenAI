class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    def get_info(self):
        return f"the product is {self.name} with price {self.price} and category {self.category}"
    
    def __str__(self):
        return f"this is {self.name}, use get_info() method to get more details about this product"
    
    def __add__(self, other):
        return Product(self.name + " & " + other.name, self.price + other.price, self.category)
    

mobile = Product("iPhone", 50000, "Electronics")
macbook = Product("MacBook Pro", 150000, "Electronics")

print(mobile)
print(macbook)
combined = mobile + macbook
print(combined)
print(combined.get_info())