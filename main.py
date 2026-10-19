
from productes import (
    add_product,
    display_all_products,
    search as search_product,
    update,
    delete
)

from sales import (
    record_sale,
    display as display_sales,
    search as search_sale
)

import reports
from Data_storage import save_data, load_data


# Load saved information when the program starts
products, sales = load_data()


while True:
    print("\n" + "=" * 35)
    print("       SALES MANAGEMENT SYSTEM")
    print("=" * 35)

    print("\n--- Product Management ---")
    print("1. Add product")
    print("2. Display all products")
    print("3. Search product")
    print("4. Update product")
    print("5. Delete product")

    print("\n--- Sales Management ---")
    print("6. Record a sale")
    print("7. View sales history")
    print("8. Search sale by ID")

    print("\n--- Reports ---")
    print("9. Sales reports")

    print("\n--- Data Storage ---")
    print("10. Save data")
    print("0. Save and exit")

    choice = input("\nChoose an option: ").strip()

    if choice == "1":
        add_product(products)

    elif choice == "2":
        display_all_products(products)

    elif choice == "3":
        search_product(products)

    elif choice == "4":
        update(products)

    elif choice == "5":
        delete(products)

    elif choice == "6":
        record_sale(products, sales)

    elif choice == "7":
        display_sales(sales)

    elif choice == "8":
        search_sale(sales)

    elif choice == "9":
        reports.total_revenue(sales)
        reports.total_unit_sold(sales)
        reports.best_selling_product(sales)
        reports.recent_sales(sales)
        reports.invantory_value(products)

    elif choice == "10":
        save_data(products, sales)

    elif choice == "0":
        save_data(products, sales)
        print("Thank you for using the Sales Management System!")
        break

    else:
        print("Invalid choice. Please enter a number from the menu.")
