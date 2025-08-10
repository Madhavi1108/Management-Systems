import mysql.connector
from mysql.connector import errorcode

def get_connection():
    try:
        # Connect to MySQL without specifying a database
        root_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mara1406#"  # your actual password
        )

        root_cursor = root_connection.cursor()

        # Check if the database exists
        root_cursor.execute("SHOW DATABASES LIKE 'restaurant_db'")
        result = root_cursor.fetchone()

        if not result:
            # Create the database
            root_cursor.execute("CREATE DATABASE restaurant_db")
            print("Database 'restaurant_db' created ✅")

        root_cursor.close()
        root_connection.close()

        # Now connect to the restaurant_db
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mara1406#",
            database="restaurant_db"
        )

        return connection

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
