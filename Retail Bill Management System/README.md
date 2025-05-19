# 🧾 Retail Billing System

A desktop-based Retail Billing System built using **Python**, **Tkinter**, and **MySQL**. It allows store owners to generate customer bills with tax calculation, print them as PDFs, send them via email, and maintain a searchable billing history.

---

## ✨ Features

* 📋 **Product Entry & Pricing**: Supports Cosmetics, Groceries, and Cold Drinks with customizable quantities.
* 🧮 **Automated Billing**: Calculates product totals, applies category-specific taxes, and computes the final amount.
* 🧾 **Bill Generation**: Generates itemized bills with formatting.
* 📬 **Email Bill**: Sends generated bills directly to the customer via email.
* 🖨️ **Print as PDF**: Saves bill content as a PDF file using `reportlab`.
* 🔍 **Search Past Bills**: Lookup and reload previous bills from the database.
* 🧼 **Clear Interface**: Reset all fields for a new customer.

---

## 🏗️ Tech Stack

* **Frontend/UI**: Tkinter
* **Backend/Logic**: Python (OOP based)
* **Database**: MySQL (via `mysql-connector-python`)
* **PDF Generation**: ReportLab
* **Email Support**: `smtplib` with Gmail SMTP

---

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/retail-billing-system.git
cd retail-billing-system
```

### 2. Install dependencies

```bash
pip install mysql-connector-python reportlab
```

### 3. Setup MySQL Database

Run the following SQL in your MySQL client to create the database:

```sql
CREATE DATABASE billing_system;

USE billing_system;

CREATE TABLE bills (
    bill_no VARCHAR(10) PRIMARY KEY,
    customer_name VARCHAR(100),
    phone VARCHAR(15),
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
    total_price FLOAT,
    bill_text TEXT
);
```

> ✅ **Note**: Ensure your MySQL user/password is correctly set in `database.py`.

---

## 🔐 Configuration

### 1. Email Credentials

Update the sender email and app password in `calculations.py`:

```python
msg['From'] = 'your_email@gmail.com'
server.login('your_email@gmail.com', 'your_app_password')
```

Use [Gmail App Passwords](https://support.google.com/accounts/answer/185833) for better security.

### 2. MySQL Connection

Modify the credentials in `database.py`:

```python
connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="your_user",
        password="your_password",
        database="billing_system"
    )
```

---

## ▶️ Running the App

Just run the main file:

```bash
python retail_bill_management.py
```

---

## 📂 Project Structure

```bash
├── calculations.py            # All billing and logic operations
├── database.py                # MySQL connection and bill saving/search
├── retail_bill_management.py # GUI layout and main loop
└── README.md
```

---

## 📌 Future Enhancements

* CSV/Excel Export
* Admin login & multi-user access
* Product management dashboard
* Error logging and audit history

---

## 🧑‍💻 Author

Developed by Madhavi
Feel free to reach out via madhavi09307@gmail.com

---

## 📝 License

This project is open-source under the MIT License.