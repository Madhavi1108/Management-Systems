# Customer management class
from database import db_query

class Customer:
    def __init__(self, username, password, name, age, city, account_number, amount):
        self.username = username
        self.password = password
        self.name = name
        self.age = age
        self.city = city
        self.account_number = account_number
        self.amount = amount

    def create_user(self):
        """Creates a new customer record."""
        try:
            db_query('''
                INSERT INTO customers (username, password, name, age, city, account_number, balance, status)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
            ''', (self.username, self.password, self.name, self.age, self.city, self.account_number, self.amount, True))
            print("User created successfully.")
        except Exception as e:
            print(f"Error creating user: {e}")
