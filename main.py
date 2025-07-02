from product_manager import ProductManager
from product import Product
from cart import Cart
import random

def main():
    manager = ProductManager()

    manager.add_product(Product("Laptop", 1200.99, 5))
    manager.add_product(Product("Mouse", 25.50, 15))
    manager.add_product(Product("Keyboard", 45.00, 10))
    manager.add_product(Product("Monitor", 250.75, 7))

    #print("Available Products:")
    #manager.display_all_products()

    #total_value = manager.total_inventory_value()
    #print(f"\nTotal Inventory Value: ${total_value:.2f}")
    
    cart = Cart()

    products = manager.products  
    for _ in range(3):
        product = random.choice(products)  #
        max_quantity = min(product.quantity, 3)  
        if max_quantity > 0:  
            quantity = random.randint(1, max_quantity)  #
            cart.add_to_cart(product, quantity)


    print("\nCart Contents:")
    cart.display_cart()

    cart_total = cart.calculate_total()
    print(f"\nTotal Cart Value: ${cart_total:.2f}")

if __name__ == "__main__":
    main()