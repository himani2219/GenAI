class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.__price = price
        self.category = category
    
    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Price must be positive.")
    
    def get_info(self):
        return f"the product is {self.name} with price {self.get_price()} and category {self.category}"
    
if __name__ == "__main__":
    mobile = Product("iPhone", 50000, "Electronics")
    macbook = Product("MacBook Pro", 150000, "Electronics")

    print(mobile.get_info())
    mobile.set_price(-20000)
    mobile.set_price(55000)
    print(mobile.get_info()) 
    print(macbook.get_info())