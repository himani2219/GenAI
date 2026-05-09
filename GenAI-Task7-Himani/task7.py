class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        return f"Name: {self.name}, Price: {self.price}"

    def __add__(self, other):
        return self.price + other.price


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                break

    def get_total_value(self):
        return sum(product.price for product in self.products)

    def show_all_products(self):
        for product in self.products:
            print(product.get_info())


class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = Inventory()

    def add_new_product(self, name, price):
        product = Product(name, price)
        self.inventory.add_product(product)

    def show_summary(self):
        print(f"Store: {self.store_name}")
        print(f"Total items: {len(self.inventory.products)}")
        print(f"Total inventory value: {self.inventory.get_total_value()}")
        print("Products in inventory:")
        self.inventory.show_all_products()


if __name__ == "__main__":
    # 1) Creating a Store object
    my_store = Store("New Age Store")

    # 2) Adding 3 products
    my_store.add_new_product("Pen", 10.0)
    my_store.add_new_product("Notebook", 50.0)
    my_store.add_new_product("Bag", 700.0)

    product_1 = my_store.inventory.products[0]
    product_2 = my_store.inventory.products[1]

    my_store.show_summary()

    combined_price = product_1 + product_2
    print(f"Combined price of {product_1.name} and {product_2.name}: {combined_price}")