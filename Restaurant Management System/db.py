import mysql.connector

# Database credentials
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "Mara1406#"
DB_NAME = "restaurant_db"

def get_connection():
    """Connect to MySQL and create the database if it doesn't exist"""
    root_connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD
    )
    root_cursor = root_connection.cursor()

    # Create database if not exists
    root_cursor.execute(f"SHOW DATABASES LIKE '{DB_NAME}'")
    if not root_cursor.fetchone():
        root_cursor.execute(f"CREATE DATABASE {DB_NAME}")
        print(f"Database '{DB_NAME}' created ✅")
    else:
        print(f"Database '{DB_NAME}' already exists ✅")

    root_cursor.close()
    root_connection.close()

    # Now connect to the specific DB
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

def create_menu_table(conn):
    """Create the menu table if it doesn't exist"""
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS menu (
            item_id INT PRIMARY KEY,
            item_name VARCHAR(100) NOT NULL,
            price DECIMAL(10,2) NOT NULL,
            category VARCHAR(50) NOT NULL
        )
    """)
    conn.commit()
    print("Menu table ready ✅")
    cursor.close()

def insert_menu_items(conn):
    """Insert all menu items into the table"""
    cursor = conn.cursor()

    # Check if already inserted
    cursor.execute("SELECT COUNT(*) FROM menu")
    count = cursor.fetchone()[0]
    if count > 0:
        print("Menu items already exist, skipping insertion ✅")
        cursor.close()
        return

    menu_items = [
        # Breakfast (10 items)
        (101, 'Masala Dosa', 60.00, 'Breakfast'),
        (102, 'Idli Sambar', 40.00, 'Breakfast'),
        (103, 'Plain Dosa', 50.00, 'Breakfast'),
        (104, 'Upma', 45.00, 'Breakfast'),
        (105, 'Poori Bhaji', 55.00, 'Breakfast'),
        (106, 'Onion Uttapam', 65.00, 'Breakfast'),
        (107, 'Medu Vada', 45.00, 'Breakfast'),
        (108, 'Pongal', 50.00, 'Breakfast'),
        (109, 'Veg Sandwich', 40.00, 'Breakfast'),
        (110, 'Bread Omelette', 35.00, 'Breakfast'),

        # Veg Main Course (25 items)
        (201, 'Veg Biryani', 120.00, 'Veg'),
        (202, 'Paneer Butter Masala', 150.00, 'Veg'),
        (203, 'Butter Naan', 25.00, 'Veg'),
        (204, 'Roti', 15.00, 'Veg'),
        (205, 'Veg Pulao', 110.00, 'Veg'),
        (206, 'Veg Fried Rice', 90.00, 'Veg'),
        (207, 'Gobi Manchurian', 100.00, 'Veg'),
        (208, 'Veg Korma', 130.00, 'Veg'),
        (209, 'Dal Tadka', 80.00, 'Veg'),
        (210, 'Chana Masala', 90.00, 'Veg'),
        (211, 'Bhindi Masala', 85.00, 'Veg'),
        (212, 'Aloo Gobi', 80.00, 'Veg'),
        (213, 'Jeera Rice', 70.00, 'Veg'),
        (214, 'Palak Paneer', 140.00, 'Veg'),
        (215, 'Veg Hakka Noodles', 95.00, 'Veg'),
        (216, 'Mix Veg Curry', 120.00, 'Veg'),
        (217, 'Mushroom Masala', 135.00, 'Veg'),
        (218, 'Rajma Masala', 95.00, 'Veg'),
        (219, 'Kadai Paneer', 150.00, 'Veg'),
        (220, 'Malai Kofta', 145.00, 'Veg'),
        (221, 'Veg Spring Roll', 100.00, 'Veg'),
        (222, 'Sweet Corn Soup', 70.00, 'Veg'),
        (223, 'Tomato Soup', 65.00, 'Veg'),
        (224, 'Paneer Tikka', 160.00, 'Veg'),
        (225, 'Veg Seekh Kebab', 120.00, 'Veg'),

        # Non-Veg Main Course (25 items)
        (301, 'Chicken Biryani', 160.00, 'Non-Veg'),
        (302, 'Mutton Biryani', 220.00, 'Non-Veg'),
        (303, 'Egg Fried Rice', 100.00, 'Non-Veg'),
        (304, 'Chicken Fried Rice', 130.00, 'Non-Veg'),
        (305, 'Fish Curry', 200.00, 'Non-Veg'),
        (306, 'Chicken Curry', 150.00, 'Non-Veg'),
        (307, 'Mutton Curry', 240.00, 'Non-Veg'),
        (308, 'Prawns Masala', 250.00, 'Non-Veg'),
        (309, 'Chicken Korma', 170.00, 'Non-Veg'),
        (310, 'Butter Chicken', 200.00, 'Non-Veg'),
        (311, 'Egg Curry', 120.00, 'Non-Veg'),
        (312, 'Chicken Tikka', 180.00, 'Non-Veg'),
        (313, 'Tandoori Chicken (Half)', 200.00, 'Non-Veg'),
        (314, 'Tandoori Chicken (Full)', 380.00, 'Non-Veg'),
        (315, 'Fish Fry', 190.00, 'Non-Veg'),
        (316, 'Crab Curry', 260.00, 'Non-Veg'),
        (317, 'Chicken 65', 160.00, 'Non-Veg'),
        (318, 'Chicken Lollipop', 150.00, 'Non-Veg'),
        (319, 'Mutton Rogan Josh', 250.00, 'Non-Veg'),
        (320, 'Keema Masala', 210.00, 'Non-Veg'),
        (321, 'Egg Bhurji', 90.00, 'Non-Veg'),
        (322, 'Grilled Fish', 230.00, 'Non-Veg'),
        (323, 'Chicken Shawarma Roll', 120.00, 'Non-Veg'),
        (324, 'Chicken Hakka Noodles', 140.00, 'Non-Veg'),
        (325, 'Mutton Keema Pulao', 200.00, 'Non-Veg'),

        # Beverages (10 items)
        (401, 'Chocolate Milkshake', 80.00, 'Beverage'),
        (402, 'Vanilla Milkshake', 75.00, 'Beverage'),
        (403, 'Strawberry Milkshake', 85.00, 'Beverage'),
        (404, 'Banana Milkshake', 70.00, 'Beverage'),
        (405, 'Mango Milkshake', 90.00, 'Beverage'),
        (406, 'Oreo Shake', 95.00, 'Beverage'),
        (407, 'Cold Coffee', 70.00, 'Beverage'),
        (408, 'Lemon Soda', 30.00, 'Beverage'),
        (409, 'Pepsi (500ml)', 35.00, 'Beverage'),
        (410, 'Sprite (500ml)', 35.00, 'Beverage'),

        # Desserts (10 items)
        (501, 'Vanilla Scoop', 30.00, 'Dessert'),
        (502, 'Chocolate Scoop', 35.00, 'Dessert'),
        (503, 'Strawberry Scoop', 35.00, 'Dessert'),
        (504, 'Butterscotch Scoop', 40.00, 'Dessert'),
        (505, 'Black Currant Scoop', 45.00, 'Dessert'),
        (506, 'Kulfi Stick', 25.00, 'Dessert'),
        (507, 'Ice Cream Sundae', 70.00, 'Dessert'),
        (508, 'Brownie with Ice Cream', 90.00, 'Dessert'),
        (509, 'Choco Lava with Ice Cream', 100.00, 'Dessert'),
        (510, 'Cassata Slice', 50.00, 'Dessert')
    ]

    cursor.executemany("INSERT INTO menu (item_id, item_name, price, category) VALUES (%s, %s, %s, %s)", menu_items)
    conn.commit()
    print("Menu items inserted successfully ✅")
    cursor.close()

if __name__ == "__main__":
    connection = get_connection()
    create_menu_table(connection)
    insert_menu_items(connection)
    connection.close()
    print("Setup complete 🚀")
