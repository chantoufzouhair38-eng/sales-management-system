
class Product:
    def __init__(self, ID, name, price, quantity):
        self.ID = ID
        self.name = name
        self.price = price
        self.quantity = quantity

    # Display one product
    def display(self):
        print("-" * 30)
        print(f"ID: {self.ID}")
        print(f"Name: {self.name}")
        print(f"Price: {self.price:.2f}")
        print(f"Quantity: {self.quantity}")
        print("-" * 30)


# A.1 - Add a product
def add_product(products):
    print("\n--- Add Product ---")

    ID = input("Enter product ID: ").strip()

    if not ID:
        print("ID cannot be empty.")
        return

    for product in products:
        if product.ID == ID:
            print(f"{ID} already exists.")
            return

    name = input("Enter product name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    try:
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
    except ValueError:
        print("Invalid data. Enter a number for price and "
              "a whole number for quantity.")
        return

    if price < 0:
        print("Price cannot be negative.")
        return

    if quantity < 0:
        print("Quantity cannot be negative.")
        return

    new_product = Product(ID, name, price, quantity)
    products.append(new_product)

    print("Product added successfully!")


# A.2 - Display all products
def display_all_products(products):
    print("\n--- All Products ---")

    if not products:
        print("No products available.")
        return

    for product in products:
        product.display()


# A.3 - Search for a product
def search_product(products):
    print("\n--- Search Product ---")

    if not products:
        print("No products available.")
        return

    search_value = input(
        "Enter product ID or name: "
    ).strip().lower()

    found = False

    for product in products:
        if (search_value == product.ID.lower()
                or search_value == product.name.lower()):
            product.display()
            found = True

    if not found:
        print(f"Product not found: {search_value}")


# A.4 - Update a product
def update_product(products):
    print("\n--- Update Product ---")

    ID = input("Enter product ID to update: ").strip()

    for product in products:
        if product.ID == ID:
            print("Current product information:")
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
                except ValueError:
                    print("Invalid price.")
                    return

                if price < 0:
                    print("Price cannot be negative.")
                    return

                product.price = price

            new_quantity = input(
                "New quantity (Enter to keep current): "
            ).strip()

            if new_quantity:
                try:
                    quantity = int(new_quantity)
                except ValueError:
                    print("Invalid quantity.")
                    return

                if quantity < 0:
                    print("Quantity cannot be negative.")
                    return

                product.quantity = quantity

            print("Product updated successfully!")
            return

    print("Product ID not found.")


# A.5 - Delete a product
def delete_product(products):
    print("\n--- Delete Product ---")

    ID = input("Enter product ID to delete: ").strip()

    for product in products:
        if product.ID == ID:
            confirmation = input(
                f"Delete {product.name}? (yes/no): "
            ).strip().lower()

            if confirmation == "yes":
                products.remove(product)
                print("Product deleted successfully.")
            else:
                print("Deletion cancelled.")

            return

    print("Product ID not found.")
