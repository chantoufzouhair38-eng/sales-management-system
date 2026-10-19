# sales-management-system


A simple, terminal-based Sales Management System built with **Python**. This project helps manage products, track sales, monitor inventory, and generate basic sales reports.

I built this project to practice Python fundamentals and learn how to organize a multi-file application.

## Features

### Product Management
- Add new products with unique IDs.
- Display all available products.
- Search for products by ID or name.
- Update product information.
- Delete products.

### Sales Management
- Record sales by product ID and quantity.
- Calculate the total price of each sale.
- Automatically update inventory after a successful sale.
- Generate a receipt with a unique sale ID.
- View sales history.
- Search for a sale by ID.

### Sales Reports
- Calculate total revenue.
- Calculate total units sold.
- Identify the best-selling product.
- Calculate the current inventory value.
- Display the five most recent sales.

### Data Storage
- Save product and sales data in JSON files.
- Load saved data when the program starts.
- Keep sales history between program sessions.

## Technologies Used

- **Python** — application logic and object-oriented programming.
- **JSON** — data storage.
- **Git and GitHub** — version control and project hosting.

## Project Structure

```text
sales-management-system/
├── main.py
├── products.py
├── sales.py
├── reports.py
├── Data_storage.py
├── .gitignore
└── data/
    ├── products.json
    └── sales.json
```

## How to Run

### 1. Install Python

Download Python from [python.org](https://www.python.org/downloads/) if it is not already installed.

### 2. Clone the repository

```bash
git clone https://github.com/chantoufzouhair38-eng/sales-management-system.git
```

### 3. Open the project folder

```bash
cd sales-management-system
```

### 4. Run the program

```bash
python main.py
```

Follow the menu displayed in the terminal to manage products, record sales, and view reports.

## What I Learned

Through this project, I practiced:

- Python classes and objects.
- Functions and modules.
- Lists and dictionaries.
- Loops and conditional statements.
- Input validation and exception handling.
- Reading and writing JSON files.
- Organizing a project across multiple Python files.
- Using Git and GitHub for version control.

## Future Improvements

- Add automated tests.
- Improve error handling and input validation.
- Use `Decimal` for more reliable monetary calculations.
- Improve the reporting system.
- Add a database for persistent storage.

## Author

**Chantouf Zouhair**

GitHub: [@chantoufzouhair38-eng](https://github.com/chantoufzouhair38-eng)

---

*This is a beginner Python project created for learning and practice.*
