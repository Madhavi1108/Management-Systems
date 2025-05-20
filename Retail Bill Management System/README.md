# 🧾 Retail Billing System 🛒

A comprehensive desktop-based Retail Billing System developed using Python, Tkinter for the GUI, and MySQL for database management. This application empowers store owners to efficiently generate customer bills, calculate taxes, print professional PDF invoices, send bills via email, and maintain a searchable history of all transactions.

---

## ✨ Key Features

* 🛍️ **Intuitive Product Management**: Easily add and manage products across categories like Cosmetics, Groceries, and Cold Drinks, with support for variable quantities.
* 🧮 **Automated Billing & Tax Calculation**: Automatically calculates sub-totals for each product category, applies relevant taxes (e.g., GST), and computes the final bill amount.
* 📄 **Professional Bill Generation**: Creates well-formatted, itemized bills ready for customers.
* 📧 **Email Integration**: Seamlessly send generated bills directly to customers' email addresses using SMTP.
* 🖨️ **PDF Export**: Save bills as high-quality PDF files for printing or digital archiving, powered by `reportlab`.
* 🔎 **Search & Retrieve Past Bills**: Quickly look up and reload previous bills from the MySQL database using a bill number.
* 🔄 **Clear & Reset**: Easily clear all input fields to start a new billing transaction.
* 🔐 **Secure Configuration**: Uses environment variables for sensitive information like database credentials and email passwords.

---

## 🛠️ Tech Stack

* **Programming Language**: Python 3.x
* **GUI Framework**: Tkinter
* **Database**: MySQL (interfaced with `mysql-connector-python`)
* **PDF Generation**: `reportlab`
* **Email Functionality**: `smtplib` (typically with Gmail SMTP)
* **Environment Management**: `python-dotenv` for managing configuration variables.

---

## 🖼️ Screenshots

*(Placeholder: Add a few screenshots of your application here to showcase its interface and functionality. For example: Main Billing Window, Product Entry, Bill Preview, Search Functionality)*

**Example:**
`![Main Window](link_to_your_screenshot.png)`

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

* **Python 3.x**: Download from [python.org](https://www.python.org/downloads/)
* **MySQL Server**: Download from [MySQL Community Downloads](https://dev.mysql.com/downloads/mysql/)
* **pip** (Python package installer, usually comes with Python)

---

## 🚀 Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/retail-billing-system.git](https://github.com/yourusername/retail-billing-system.git)
    cd retail-billing-system
    ```
    *(Replace `yourusername` with your actual GitHub username)*

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```
    * On Windows, activate it using: `venv\Scripts\activate`
    * On macOS/Linux, activate it using: `source venv/bin/activate`

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(You'll need to create a `requirements.txt` file. See section below)*

4.  **Create `requirements.txt`:**
    Create a file named `requirements.txt` in the root of your project with the following content:
    ```
    mysql-connector-python
    reportlab
    python-dotenv
    ```

---

## ⚙️ Configuration

### 1. Setup MySQL Database

* Ensure your MySQL server is running.
* Connect to your MySQL server using a client (e.g., MySQL Workbench, `mysql` command line).
* Run the following SQL commands to create the necessary database and table:

    ```sql
    CREATE DATABASE IF NOT EXISTS billing_system_db;

    USE billing_system_db;

    CREATE TABLE IF NOT EXISTS bills (
        bill_no VARCHAR(10) PRIMARY KEY,
        customer_name VARCHAR(100) NOT NULL,
        phone VARCHAR(15) NOT NULL,
        email VARCHAR(100),
        bath_soap INT DEFAULT 0,
        face_cream INT DEFAULT 0,
        face_wash INT DEFAULT 0,
        hair_spray INT DEFAULT 0,
        hair_gel INT DEFAULT 0,
        baby_lotion INT DEFAULT 0,
        rice INT DEFAULT 0,
        oil INT DEFAULT 0,
        daal INT DEFAULT 0,
        wheat INT DEFAULT 0,
        sugar INT DEFAULT 0,
        tea INT DEFAULT 0,
        maaza INT DEFAULT 0,
        pepsi INT DEFAULT 0,
        sprite INT DEFAULT 0,
        dew INT DEFAULT 0,
        frooti INT DEFAULT 0,
        coca_cola INT DEFAULT 0,
        total_price FLOAT NOT NULL,
        cosmetic_tax FLOAT,
        grocery_tax FLOAT,
        drinks_tax FLOAT,
        bill_text TEXT NOT NULL,
        bill_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    ```
    *Note: The table structure has been slightly enhanced for clarity and to store more details like individual taxes and bill date.*

### 2. Environment Variables (`.env` file)

Create a file named `.env` (or `file.env` as used in your `calculations.py` and `database.py`) in the root directory of your project. Add your MySQL and Email credentials to this file:

```env
# .env or file.env

# MySQL Database Configuration
DB_HOST=localhost
DB_USER=your_mysql_user
DB_PASS=your_mysql_password
DB_NAME=billing_system_db

# Email Configuration (for Gmail)
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_gmail_app_password