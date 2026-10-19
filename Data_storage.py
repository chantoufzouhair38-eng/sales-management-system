
import json
import os
from products import Product


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

PRODUCTS_FILE = os.path.join(DATA_DIR, "products.json")
SALES_FILE = os.path.join(DATA_DIR, "sales.json")


def save_data(products, sales):
    try:
        os.makedirs(DATA_DIR, exist_ok=True)

        products_data = []

        for product in products:
            product_data = {
                "id": product.id,
                "name": product.name,
                "price": product.price,
                "quantity": product.quantity
            }
            products_data.append(product_data)

        with open(PRODUCTS_FILE, "w", encoding="utf-8") as file:
            json.dump(products_data, file, indent=4)

        with open(SALES_FILE, "w", encoding="utf-8") as file:
            json.dump(sales, file, indent=4)

        print("Data saved successfully!")

    except (OSError, TypeError, ValueError) as error:
        print(f"Error saving data: {error}")


def load_data():
    products = []
    sales = []

    # Load products
    try:
        with open(PRODUCTS_FILE, "r", encoding="utf-8") as file:
            products_data = json.load(file)

        if not isinstance(products_data, list):
            raise ValueError("Products data must be a list.")

        for item in products_data:
            product = Product(
                item["id"],
                item["name"],
                item["price"],
                item["quantity"]
            )
            products.append(product)

    except FileNotFoundError:
        print("No saved products found.")

    except (json.JSONDecodeError, OSError, TypeError,
            KeyError, ValueError) as error:
        print(f"Could not load products: {error}")
        products = []

    # Load sales
    try:
        with open(SALES_FILE, "r", encoding="utf-8") as file:
            sales_data = json.load(file)

        if not isinstance(sales_data, list):
            raise ValueError("Sales data must be a list.")

        sales = sales_data

    except FileNotFoundError:
        print("No saved sales found.")

    except (json.JSONDecodeError, OSError, TypeError,
            ValueError) as error:
        print(f"Could not load sales: {error}")
        sales = []

    return products, sales
