# database.py
from dotenv import load_dotenv
import mysql.connector
import os
from tkinter import messagebox
from dotenv import load_dotenv
load_dotenv(dotenv_path="file.env")

product_list = [
    'Bath Soap', 'Face Cream', 'Face Wash', 'Hair Spray', 'Hair Gel', 'Baby Lotion',
    'Rice', 'Oil', 'Daal', 'Wheat', 'Sugar', 'Tea',
    'Maaza', 'Pepsi', 'Sprite', 'Dew', 'Frooti', 'Coca Cola'
]

def connect_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME")
    )

def search_bill(bill_no):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bills WHERE bill_no = %s", (bill_no,))
        result = cursor.fetchone()
        conn.close()
        return result
    except Exception as e:
        messagebox.showerror("Database Error", str(e))
        return None

def save_bill(bill_data):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        columns = ['bill_no', 'customer_name', 'phone'] + [item.lower().replace(" ", "_") for item in product_list] + ['total_price', 'bill_text']
        placeholders = ', '.join(['%s'] * len(columns))
        column_names = ', '.join(columns)

        query = f"INSERT INTO bills ({column_names}) VALUES ({placeholders})"
        values = [bill_data['bill_no'], bill_data['name'], bill_data['phone']] + [bill_data[item] for item in product_list] + [bill_data['total'], bill_data['bill_text']]

        cursor.execute(query, values)
        conn.commit()
        conn.close()
    except Exception as e:
        messagebox.showerror("Database Error", str(e))
