
def total_revenue(sales):
    revenue = 0

    for sale in sales:
        revenue += sale["total"]

    print(f"\nTotal revenue: {revenue:.2f}")


def total_unit_sold(sales):
    units = 0

    for sale in sales:
        units += sale["quantity"]

    print(f"\nTotal units sold: {units}")


def best_selling_product(sales):
    if not sales:
        print("No sales available.")
        return

    product_quantities = {}

    for sale in sales:
        product_id = sale["product_id"]
        product_name = sale["product_name"]
        quantity = sale["quantity"]

        if product_id in product_quantities:
            product_quantities[product_id]["quantity"] += quantity
        else:
            product_quantities[product_id] = {
                "name": product_name,
                "quantity": quantity
            }

    best_product = max(
        product_quantities,
        key=lambda key: product_quantities[key]["quantity"]
    )

    print("\n--- Best-Selling Product ---")
    print(f"Product: {product_quantities[best_product]['name']}")
    print(f"Units sold: {product_quantities[best_product]['quantity']}")


def invantory_value(products):
    total = 0

    for product in products:
        total += product.price * product.quantity

    print(f"\nCurrent inventory value: {total:.2f}")


def recent_sales(sales):
    print("\n--- Five Most Recent Sales ---")

    if not sales:
        print("No sales available.")
        return

    for sale in sales[-5:][::-1]:
        print("-" * 30)
        print(f"Sale ID: {sale['sale_id']}")
        print(f"Product: {sale['product_name']}")
        print(f"Quantity: {sale['quantity']}")
        print(f"Total: {sale['total']:.2f}")
