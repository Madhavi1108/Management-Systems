# calculations.py
import random
from database import *
from tkinter import messagebox
from tkinter import *

class Calculations:
    def __init__(self, cosmetic_entries, grocery_entries, colddrinks_entries,
                 cosmeticpriceEntry, cosmetictaxEntry,
                 grocerypriceEntry, grocerytaxEntry,
                 drinkspriceEntry, colddrinkstaxEntry,
                 name_entry, phone_entry, textarea):

        self.textarea = textarea
        # Product Entries
        self.cosmetic_entries = cosmetic_entries
        self.grocery_entries = grocery_entries
        self.colddrinks_entries = colddrinks_entries

        # Price and Tax Entries
        self.cosmeticpriceEntry = cosmeticpriceEntry
        self.cosmetictaxEntry = cosmetictaxEntry
        self.grocerypriceEntry = grocerypriceEntry
        self.grocerytaxEntry = grocerytaxEntry
        self.drinkspriceEntry = drinkspriceEntry
        self.colddrinkstaxEntry = colddrinkstaxEntry

        # Customer Details Entries
        self.name_entry = name_entry
        self.phone_entry = phone_entry

    def total(self):
        # Cosmetic
        cosmetic_prices = [20, 50, 100, 150, 80, 60]
        cosmetic_item_names = ['Bath Soap', 'Face Cream', 'Face Wash', 'Hair Spray', 'Hair Gel', 'Baby Lotion']
        total_cosmetic = sum(int(self.cosmetic_entries[name].get() or 0) * price
                             for name, price in zip(cosmetic_item_names, cosmetic_prices))
        self.cosmeticpriceEntry.delete(0, 'end')
        self.cosmeticpriceEntry.insert(0, f'{total_cosmetic} Rs')
        self.cosmetictaxEntry.delete(0, 'end')
        self.cosmetictaxEntry.insert(0, total_cosmetic * 0.12)

        # Grocery
        grocery_prices = [30, 100, 120, 50, 140, 80]
        grocery_item_names = ['Rice', 'Oil', 'Daal', 'Wheat', 'Sugar', 'Tea']
        total_grocery = sum(int(self.grocery_entries[name].get() or 0) * price
                            for name, price in zip(grocery_item_names, grocery_prices))
        self.grocerypriceEntry.delete(0, 'end')
        self.grocerypriceEntry.insert(0, f'{total_grocery} Rs')
        self.grocerytaxEntry.delete(0, 'end')
        self.grocerytaxEntry.insert(0, total_grocery * 0.05)

        # Cold Drinks
        colddrinks_prices = [50, 20, 30, 20, 45, 90]
        colddrinks_item_names = ['Maaza', 'Pepsi', 'Sprite', 'Dew', 'Frooti', 'Coca Cola']
        total_colddrinks = sum(int(self.colddrinks_entries[name].get() or 0) * price
                               for name, price in zip(colddrinks_item_names, colddrinks_prices))
        self.drinkspriceEntry.delete(0, 'end')
        self.drinkspriceEntry.insert(0, f'{total_colddrinks} Rs')
        self.colddrinkstaxEntry.delete(0, 'end')
        self.colddrinkstaxEntry.insert(0, total_colddrinks * 0.08)

    def generate_bill(self):
        customer_name = self.name_entry.get().strip()
        customer_phone = self.phone_entry.get().strip()

        if customer_name == '' or customer_phone == '':
            messagebox.showerror("Error", "Customer Details are required")
            return

        # Generate random bill number
        bill_no = str(random.randint(1000, 9999))

        self.textarea.delete('1.0', END)
        self.textarea.insert(END, "\n\t*** WELCOME TO THE STORE ***\n")
        self.textarea.insert(END, f"\nBill No      : {bill_no}")
        self.textarea.insert(END, f"\nCustomer Name: {customer_name}")
        self.textarea.insert(END, f"\nPhone Number : {customer_phone}")
        self.textarea.insert(END, "\n===================================")
        self.textarea.insert(END, "\nProduct\t\tQty\tPrice")
        self.textarea.insert(END, "\n===================================\n")

        bill_data = {
            'bill_no': bill_no,
            'name': customer_name,
            'phone': customer_phone,
            'total': 0,
            'bill_text': '',
        }

        # Helper function to process items
        def process_items(entries, names, prices):
            total = 0
            for name, price in zip(names, prices):
                qty = int(entries[name].get() or 0)
                bill_data[name] = qty
                if qty > 0:
                    line_total = qty * price
                    total += line_total
                    self.textarea.insert(END, f"{name}\t\t{qty}\t{line_total}\n")
            return total

        # Process each section
        total_cosmetics = process_items(self.cosmetic_entries,
                                        ['Bath Soap', 'Face Cream', 'Face Wash', 'Hair Spray', 'Hair Gel',
                                         'Baby Lotion'],
                                        [20, 50, 100, 150, 80, 60])
        total_grocery = process_items(self.grocery_entries,
                                      ['Rice', 'Oil', 'Daal', 'Wheat', 'Sugar', 'Tea'],
                                      [30, 100, 120, 50, 140, 80])
        total_drinks = process_items(self.colddrinks_entries,
                                     ['Maaza', 'Pepsi', 'Sprite', 'Dew', 'Frooti', 'Coca Cola'],
                                     [50, 20, 30, 20, 45, 90])

        grand_total = total_cosmetics + total_grocery + total_drinks
        self.textarea.insert(END, "\n===================================\n")
        self.textarea.insert(END, f"Total Amount: {grand_total} Rs\n")
        self.textarea.insert(END, "===================================\n")

        # Store final values in bill_data
        bill_data['total'] = grand_total
        bill_data['bill_text'] = self.textarea.get('1.0', END)

        # Save to database
        save_bill(bill_data)
        messagebox.showinfo("Success", f"Bill No {bill_no} saved successfully!")

    def send_email(self):
        pass

    def print_bill(self):
        pass

    def clear_fields(self):
        pass
