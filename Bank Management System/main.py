from register import signup, login
from bank import Bank
from database import db_query


def main():
    """Main function to handle user input."""
    status = False
    user = None

    while True:
        print("1. Signup\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            signup()
        elif choice == "2":
            user = login()
            if user:
                status = True
                break
        elif choice == "3":
            print("Goodbye!")
            return
        else:
            print("Invalid choice, try again.")

    try:
        account_data = db_query("SELECT account_number FROM customers WHERE username = %s", (user,), fetch=True)
        if account_data:
            account_number = account_data[0][0]
            print(f"Your account number is {account_number}")
        else:
            print("Error retrieving account number.")
            return

        while status:
            try:
                facility = int(input("1. Balance Enquiry\n"
                                     "2. Cash Deposit\n"
                                     "3. Cash Withdraw\n"
                                     "4. Fund Transfer\n"
                                     "5. Exit\n"
                                     "Enter your choice: "))

                bobj = Bank(user, account_number)

                if facility == 1:
                    balance = bobj.balance_enquiry()
                    print(f"The balance in your account is {balance}\n")
                elif facility == 2:
                    amount = float(input("Enter the amount you want to deposit: "))
                    if amount > 0:
                        bobj.deposit(amount)
                    else:
                        print("Enter an amount greater than 0")
                elif facility == 3:
                    amount = float(input("Enter the amount you want to withdraw: "))
                    if amount > 0:
                        bobj.withdraw(amount)
                    else:
                        print("Enter an amount greater than 0")
                elif facility == 4:
                    receiver = int(input("Enter the receiver's Account Number: "))
                    amount = float(input("Enter the amount to transfer: "))
                    if amount > 0:
                        bobj.fund_transfer(receiver, amount)
                    else:
                        print("Enter a valid amount.")
                elif facility == 5:
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice, please try again.")
            except ValueError:
                print("Invalid input! Please enter a number.")
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print("Session ended successfully.")


if __name__ == "__main__":
    main()
