# Bank-related functionalities
from database import db_query


class Bank:
    def __init__(self, username, account_number):
        self.username = username
        self.account_number = account_number

    def create_transaction_table(self):
        """Creates a transaction table if it does not exist."""
        db_query('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INT AUTO_INCREMENT PRIMARY KEY,
                account_number VARCHAR(20) NOT NULL,
                transaction_type VARCHAR(10) NOT NULL,
                amount DECIMAL(10, 2) NOT NULL,
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        ''')

    def balance_enquiry(self):
        """Returns the balance of the user's account."""
        temp = db_query("SELECT balance FROM customers WHERE username = %s AND account_number = %s;",
                        (self.username, self.account_number), fetch=True)
        return temp[0][0] if temp else None

    def deposit(self, amount):
        """Deposits an amount into the user's account."""
        try:
            temp = self.balance_enquiry()
            if temp is not None:
                new_balance = temp + amount
                db_query("UPDATE customers SET balance = %s WHERE username = %s AND account_number = %s;",
                         (new_balance, self.username, self.account_number))
                db_query("INSERT INTO transactions (account_number, transaction_type, amount) VALUES (%s, %s, %s);",
                         (self.account_number, 'Deposit', amount))
                print(f"Deposit successful. New balance: {new_balance}")
            else:
                print("Account not found.")
        except Exception as e:
            print(f"An error occurred during deposit: {e}")

    def withdraw(self, amount):
        """Withdraws an amount from the user's account."""
        try:
            temp = self.balance_enquiry()
            if temp is not None and temp >= amount:
                new_balance = temp - amount
                db_query("UPDATE customers SET balance = %s WHERE username = %s AND account_number = %s;",
                         (new_balance, self.username, self.account_number))
                db_query("INSERT INTO transactions (account_number, transaction_type, amount) VALUES (%s, %s, %s);",
                         (self.account_number, 'Withdraw', amount))
                print(f"Withdrawal successful. New balance: {new_balance}")
            else:
                print("Insufficient balance or account not found.")
        except Exception as e:
            print(f"An error occurred during withdrawal: {e}")

    def fund_transfer(self, receiver_account, amount):
        """Transfers an amount from the user's account to another account."""
        try:
            sender_balance = self.balance_enquiry()
            receiver_balance = db_query("SELECT balance FROM customers WHERE account_number = %s;",
                                        (receiver_account,), fetch=True)

            if sender_balance is not None and receiver_balance:
                receiver_balance = receiver_balance[0][0]
                if sender_balance >= amount:
                    new_sender_balance = sender_balance - amount
                    new_receiver_balance = receiver_balance + amount

                    db_query("UPDATE customers SET balance = %s WHERE account_number = %s;",
                             (new_sender_balance, self.account_number))
                    db_query("UPDATE customers SET balance = %s WHERE account_number = %s;",
                             (new_receiver_balance, receiver_account))
                    db_query("INSERT INTO transactions (account_number, transaction_type, amount) VALUES (%s, %s, %s);",
                             (self.account_number, 'Transfer Out', amount))
                    db_query("INSERT INTO transactions (account_number, transaction_type, amount) VALUES (%s, %s, %s);",
                             (receiver_account, 'Transfer In', amount))

                    print("Transfer successful.")
                else:
                    print("Insufficient balance for transfer.")
            else:
                print("Invalid sender or receiver account.")
        except Exception as e:
            print(f"An error occurred during fund transfer: {e}")
