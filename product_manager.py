from product import Product 

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_all_products(self):
        if not self.products:
            print("No products available.")
        else:
            for product in self.products:
                print(product.display_info())

    def total_inventory_value(self):
        total_value = sum(product.price * product.quantity for product in self.products)
        return total_value
    
    def remove_product_by_name(self, name):
        initial_count = len(self.products)
        self.products = [p for p in self.products if p.name != name]
        if len(self.products) < initial_count:
            print(f"Product(s) named '{name}' removed.")
        else:
            print(f"No product named '{name}' found.")