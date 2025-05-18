# 🧾 Retail Billing System

A GUI-based retail billing system built using **Python** and **Tkinter**, backed by a **MySQL** database. This application is designed for managing customer bills, calculating totals and taxes, and storing bill data for later retrieval.

## 🛠 Features

- Customer detail input (Name, Phone, Bill Number)
- Product input for:
  - Cosmetics
  - Groceries
  - Cold Drinks
- Automatic price and tax calculation per category
- Bill generation with a unique bill number
- Bill display and printing area
- Save bill data to MySQL database
- Search and retrieve past bills by bill number
- Placeholder buttons for email and print functionality (ready to be implemented)

## 📦 Project Structure

```plaintext
.
├── calculations.py            # Handles pricing logic and bill generation
├── database.py                # Connects to MySQL and manages bill data storage/retrieval
├── retail_bill_management.py  # Main GUI logic using Tkinter
````

## 🧰 Requirements

* Python 3.x
* Tkinter (usually bundled with Python)
* MySQL server
* Python packages:

  * `mysql-connector-python`

Install dependencies:

```bash
pip install mysql-connector-python
```

## 🗄️ MySQL Setup

Ensure your MySQL database is running and create a database and table as follows:

```sql
CREATE DATABASE billing_system;

USE billing_system;

CREATE TABLE bills (
    bill_no VARCHAR(10) PRIMARY KEY,
    customer_name VARCHAR(100),
    phone VARCHAR(20),
    bath_soap INT,
    face_cream INT,
    face_wash INT,
    hair_spray INT,
    hair_gel INT,
    baby_lotion INT,
    rice INT,
    oil INT,
    daal INT,
    wheat INT,
    sugar INT,
    tea INT,
    maaza INT,
    pepsi INT,
    sprite INT,
    dew INT,
    frooti INT,
    coca_cola INT,
    total_price INT,
    bill_text TEXT
);
```

> Make sure your database credentials in `database.py` match your MySQL setup:

```python
host="localhost",
user="root",
password="YOUR_PASSWORD",
database="billing_system"
```

## 🚀 Running the App

```bash
python retail_bill_management.py
```

The application window will launch, allowing entry of customer and product details. Click `Total` to calculate prices, `Bill` to generate and save the bill, and `Search` to retrieve a previous bill using its number.

## ✅ To-Do

* Implement email functionality (`send_email`)
* Add support for printing bills (`print_bill`)
* Enhance UI and error handling

---

## 🧑‍💻 Author

* Developed by Madhavi as part of a retail management automation project.
