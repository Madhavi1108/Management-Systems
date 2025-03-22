# Database Management for Banking System
import mysql.connector as sql

# Establish connection to MySQL database
mydb = sql.connect(
    host="localhost",
    user="root",
    password="",#Enter your password
    database="bank"
)

cursor = mydb.cursor()

def db_query(query, values=None, fetch=False):
    """Executes a database query with optional fetching."""
    try:
        cursor.execute(query, values or ())
        if fetch:
            return cursor.fetchall()
        else:
            mydb.commit()
    except sql.Error as e:
        print(f"Database error: {e}")

def create_customer_table():
    """Creates the customers table if it does not exist."""
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                username VARCHAR(20) PRIMARY KEY,
                password VARCHAR(20),
                name VARCHAR(20),
                age INTEGER,
                city VARCHAR(20),
                account_number INTEGER UNIQUE,
                balance DECIMAL(10,2) DEFAULT 0.00,
                status BOOLEAN
            )
        ''')
        mydb.commit()
    except sql.Error as e:
        print(f"Error creating table: {e}")

if __name__ == "__main__":
    create_customer_table()
