import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",        # change if needed
    user="root",             # your MySQL username
    password="yourpassword"  # your MySQL password
)

cursor = connection.cursor()

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS restaurant_db")
cursor.execute("USE restaurant_db")

# ------------------------
# USERS TABLE
# ------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    role ENUM('owner','manager','staff') NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB
""")

# ------------------------
# MENU TABLE
# ------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS menu (
    item_id INT NOT NULL AUTO_INCREMENT,
    item_name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    category VARCHAR(50) NOT NULL,
    PRIMARY KEY (item_id)
) ENGINE=InnoDB
""")

# ------------------------
# CUSTOMERS TABLE
# ------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(100),
    PRIMARY KEY (customer_id)
) ENGINE=InnoDB
""")

# ------------------------
# ORDERS TABLE
# ------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INT NOT NULL AUTO_INCREMENT,
    customer_id INT,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10,2),
    PRIMARY KEY (order_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
) ENGINE=InnoDB
""")

# ------------------------
# ORDER ITEMS TABLE
# ------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS order_items (
    id INT NOT NULL AUTO_INCREMENT,
    order_id INT,
    item_id INT,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (item_id) REFERENCES menu(item_id)
) ENGINE=InnoDB
""")

print("✅ All tables created successfully in restaurant_db!")

# Close connection
cursor.close()
connection.close()
