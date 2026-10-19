
def record_sale(products, sales):
    print("\n--- Record a Sale ---")

    if not products:
        print("No products available.")
        return

    product_id = input("Enter product ID: ").strip()

    selected_product = None

    for product in products:
        if product.id == product_id:
            selected_product = product
            break

    if selected_product is None:
        print("Product not found.")
        return

    selected_product.display()

    try:
        quantity = int(input("Enter quantity to sell: "))
    except ValueError:
        print("Enter a valid whole number.")
        return

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return

    if quantity > selected_product.quantity:
        print(f"Available stock: {selected_product.quantity}")
        print("Not enough stock.")
        return

    unit_price = selected_product.price
    total = unit_price * quantity
    sale_id = f"S{len(sales) + 1:03d}"

    sale = {
        "sale_id": sale_id,
        "product_id": selected_product.id,
        "product_name": selected_product.name,
        "quantity": quantity,
        "unit_price": unit_price,
        "total": total
    }

    selected_product.quantity -= quantity
    sales.append(sale)

    print("\n========== RECEIPT ==========")
    print(f"Sale ID: {sale_id}")
    print(f"Product: {selected_product.name}")
    print(f"Quantity: {quantity}")
    print(f"Unit price: {unit_price:.2f}")
    print(f"Total: {total:.2f}")
    print("=============================")
    print("Sale completed successfully!")


def display(sales):
    print("\n--- Sales History ---")

    if not sales:
        print("No sales recorded.")
        return

    for sale in sales:
        print("-" * 30)
        print(f"Sale ID: {sale['sale_id']}")
        print(f"Product: {sale['product_name']}")
        print(f"Quantity: {sale['quantity']}")
        print(f"Unit price: {sale['unit_price']:.2f}")
        print(f"Total: {sale['total']:.2f}")
        print("-" * 30)


def search(sales):
    if not sales:
        print("No sales recorded.")
        return

    sale_id = input("Enter sale ID: ").strip().upper()

    for sale in sales:
        if sale_id == sale["sale_id"].upper():
            print("\n========== RECEIPT ==========")
            print(f"Sale ID: {sale['sale_id']}")
            print(f"Product: {sale['product_name']}")
            print(f"Quantity: {sale['quantity']}")
            print(f"Unit price: {sale['unit_price']:.2f}")
            print(f"Total: {sale['total']:.2f}")
            print("=============================")
            return

    print("Sale not found.")
