from task2 import Product

class ElectronicProduct(Product):
    def __init__(self, name, price, category, warranty):
        super().__init__(name, price, category)
        self.warranty = warranty
    
    def get_info(self):
        return f"{super().get_info()} with a warranty of {self.warranty} years"
    
if __name__ == "__main__":
    laptop = ElectronicProduct("Dell XPS 13", 120000, "Electronics", 2)
    print(laptop.get_info())