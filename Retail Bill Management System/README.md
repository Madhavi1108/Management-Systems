# 🧾 Retail Billing System

A feature-rich desktop-based **Retail Billing System** built using **Python**, **Tkinter**, and **MySQL**.
The application is designed to streamline retail store operations by enabling efficient billing, automated tax calculations, invoice generation, PDF exports, email integration, and transaction history management.

---

## ✨ Features

### 🛍️ Product Management

* Manage products across multiple categories:

  * Cosmetics
  * Groceries
  * Cold Drinks
* Support for dynamic quantity selection and itemized billing.

### 🧮 Automated Billing & Tax Calculation

* Automatically calculates:

  * Product-wise totals
  * Category-wise subtotals
  * Applicable taxes (GST)
  * Final payable amount

### 📄 Professional Invoice Generation

* Generates clean and well-structured customer bills.
* Displays complete transaction details in an organized format.

### 🖨️ PDF Invoice Export

* Export bills as high-quality PDF invoices using `reportlab`.
* Suitable for printing and digital record keeping.

### 📧 Email Integration

* Send invoices directly to customer email addresses via SMTP.
* Supports Gmail SMTP integration.

### 🔎 Bill Search & Retrieval

* Retrieve previous bills instantly using the bill number.
* Reload stored transactions from the MySQL database.

### 🔄 Reset & Clear Functionality

* Quickly reset all billing fields to begin a new transaction.

### 🔐 Secure Configuration

* Sensitive credentials are managed securely using environment variables (`.env`).

---

# 🛠️ Tech Stack

| Technology                 | Purpose                         |
| -------------------------- | ------------------------------- |
| **Python 3.x**             | Core Programming Language       |
| **Tkinter**                | Desktop GUI Framework           |
| **MySQL**                  | Database Management             |
| **mysql-connector-python** | MySQL Integration               |
| **reportlab**              | PDF Generation                  |
| **smtplib**                | Email Functionality             |
| **python-dotenv**          | Environment Variable Management |

---

# 📋 Prerequisites

Ensure the following software is installed before running the project:

* **Python 3.x**
  Download: [Python Official Website](https://www.python.org/downloads/?utm_source=chatgpt.com)

* **MySQL Server**
  Download: [MySQL Community Downloads](https://dev.mysql.com/downloads/mysql/?utm_source=chatgpt.com)

* **pip** (Python package installer)

---

# 🚀 Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/retail-billing-system.git
cd retail-billing-system
```

> Replace `yourusername` with your actual GitHub username.

---

## 2️⃣ Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

### Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Create `requirements.txt`

Create a file named `requirements.txt` in the root directory and add the following dependencies:

```txt
mysql-connector-python
reportlab
python-dotenv
```

---

# ⚙️ Configuration

## 1️⃣ Configure MySQL Database

Ensure your MySQL server is running, then execute the following SQL commands:

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

---

## 2️⃣ Configure Environment Variables

Create a `.env` file in the project root directory and add the following configuration:

```env
# MySQL Database Configuration
DB_HOST=localhost
DB_USER=your_mysql_user
DB_PASS=your_mysql_password
DB_NAME=billing_system_db

# Email Configuration
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_gmail_app_password
```

> For Gmail integration, use an **App Password** instead of your actual Gmail password.

---

# ▶️ Running the Application

Run the application using:

```bash
python main.py
```

---

# 📌 Future Enhancements

* Barcode Scanner Integration
* Inventory & Stock Management
* Sales Analytics Dashboard
* Customer Management System
* Multi-user Authentication
* Cloud Database Support

---

# 📜 License

This project is developed for educational and learning purposes.
Feel free to modify and enhance it as needed.

---

# 👨‍💻 Author

Developed with Python and MySQL to simplify retail billing and invoice management.
