# User Registration, Signup, and Login
from database import db_query
from customer import Customer
from bank import Bank
import random

def signup():
    """Handles user signup."""
    username = input("Create a username: ")
    temp = db_query("SELECT username FROM customers WHERE username = %s;", (username,), fetch=True)

    if temp:
        print("Username already exists. Please try again.")
        return

    print("Username is available")
    password = input("Enter your password: ")
    name = input("Enter your name: ")

    while True:
        age = input("Enter your age: ")
        if age.isdigit():
            age = int(age)
            break
        print("Invalid age. Please enter a number.")

    city = input("Enter your city: ")

    # Generate unique account number
    while True:
        account_number = random.randint(10000000, 99999999)
        if not db_query("SELECT account_number FROM customers WHERE account_number = %s;", (account_number,), fetch=True):
            break

    while True:
        amount = input("Enter your initial deposit: ")
        if amount.replace('.', '', 1).isdigit():  # Allow decimal input
            amount = float(amount)
            break
        print("Invalid deposit amount. Please enter a valid number.")

    cobj = Customer(username, password, name, age, city, account_number, amount)
    cobj.create_user()

    bobj = Bank(username, account_number)
    bobj.create_transaction_table()

    print("Signup successful! You can now log in.")

def login():
    """Handles user login."""
    username = input("Enter username: ")
    temp = db_query("SELECT username FROM customers WHERE username = %s;", (username,), fetch=True)

    if temp:
        for _ in range(3):  # Limit password attempts
            password = input("Enter password: ")
            stored_password = db_query("SELECT password FROM customers WHERE username = %s;", (username,), fetch=True)

            if stored_password and stored_password[0][0] == password:
                print("Login Successful")
                return username
            else:
                print("Wrong Password. Try Again.")
        print("Too many failed attempts. Try later.")
        return None
    else:
        print("User does not exist.")
        return None
