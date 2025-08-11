import mysql.connector

# Database credentials
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = ""
DB_NAME = "restaurant_db"

# Database connection
db = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)
cursor = db.cursor()

def fetch_item_details(item_id):
    cursor.execute("SELECT item_name, price FROM menu WHERE item_id = %s", (item_id,))
    return cursor.fetchone()  # (item_name, price) or None

def get_items_from_user():
    items = []
    while True:
        try:
            item_id = int(input("Enter Item ID (0 to stop): "))
            if item_id == 0:
                break
            quantity = int(input("Enter Quantity: "))

            if quantity <= 0:
                print("❌ Quantity must be greater than zero.")
                continue

            items.append((item_id, quantity))
        except ValueError:
            print("❌ Please enter valid integers for ID and Quantity.")
    return items

def calculate_total(items):
    bill_items = []
    total = 0
    for item_id, qty in items:
        details = fetch_item_details(item_id)
        if details:
            name, price = details
            amount = float(price) * qty
            bill_items.append((item_id, name, float(price), qty, amount))
            total += amount
        else:
            print(f"❌ Item ID {item_id} not found in menu.")
    return bill_items, total

def display_bill(bill_items, total):
    print("\n===== BILL =====")
    print(f"{'ID':<5}{'Name':<20}{'Price':<10}{'Qty':<5}{'Amount':<10}")
    for item_id, name, price, qty, amount in bill_items:
        print(f"{item_id:<5}{name:<20}{price:<10}{qty:<5}{amount:<10}")
    print("-" * 50)
    print(f"{'Total':<40}{total:<10}")

# Main flow
user_items = get_items_from_user()
bill_items, total = calculate_total(user_items)
display_bill(bill_items, total)

# Close DB connection
cursor.close()
db.close()
