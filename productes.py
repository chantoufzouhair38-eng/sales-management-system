
class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self):
        print("-" * 30)
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Price: {self.price:.2f}")
        print(f"Quantity: {self.quantity}")
        print("-" * 30)


def add_product(products):
    print("\n--- Add Product ---")
    product_id = input("Enter product ID: ").strip()

    if not product_id:
        print("ID cannot be empty.")
        return

    for product in products:
        if product.id == product_id:
            print("This ID already exists.")
            return

    name = input("Enter product name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    try:
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Please enter a valid price and whole-number quantity.")
        return

    if price < 0 or quantity < 0:
        print("Price and quantity cannot be negative.")
        return

    new_product = Product(product_id, name, price, quantity)
    products.append(new_product)
    print("Product added successfully!")


def display_all_products(products):
    print("\n--- All Products ---")

    if not products:
        print("No products available.")
        return

    for product in products:
        product.display()


def search(products):
    search_value = input("Enter product ID or name: ").strip().lower()

    if not search_value:
        print("Search value cannot be empty.")
        return

    found = False

    for product in products:
        if (search_value == product.id.lower()
                or search_value == product.name.lower()):
            product.display()
            found = True

    if not found:
        print("Product not found.")


def update(products):
    product_id = input("Enter product ID to update: ").strip()

    for product in products:
        if product.id == product_id:
            product.display()

            new_name = input(
                "New name (Enter to keep current): "
            ).strip()

            if new_name:
                product.name = new_name

            new_price = input(
                "New price (Enter to keep current): "
            ).strip()

            if new_price:
                try:
                    price = float(new_price)
                    if price < 0:
                        print("Price cannot be negative.")
                        return
                    product.price = price
                except ValueError:
                    print("Invalid price.")
                    return

            new_quantity = input(
                "New quantity (Enter to keep current): "
            ).strip()

            if new_quantity:
                try:
                    quantity = int(new_quantity)
                    if quantity < 0:
                        print("Quantity cannot be negative.")
                        return
                    product.quantity = quantity
                except ValueError:
                    print("Invalid quantity.")
                    return

            print("Product updated successfully!")
            return

    print("Product not found.")


def delete(products):
    product_id = input("Enter product ID to delete: ").strip()

    for product in products:
        if product.id == product_id:
            confirmation = input(
                f"Delete {product.name}? (yes/no): "
            ).strip().lower()

            if confirmation == "yes":
                products.remove(product)
                print("Product deleted successfully.")
            else:
                print("Deletion cancelled.")
            return

    print("Product not found.")
