from tkinter import *
from calculations import *


# ---------------- Main Window ----------------
root = Tk()
root.title('Retail Billing System')
root.geometry('1270x685')
root.config(bg='gray20')

# ---------------- Header ----------------
Label(root, text='Retail Billing System',
      font=('times new roman', 30, 'bold'),
      bg='gray20', fg='gold', bd=12, relief=GROOVE).pack(fill=X)

# ---------------- Customer Details Frame ----------------
customer_details_frame = LabelFrame(root, text='Customer Details',
                                    font=('times new roman', 15, 'bold'),
                                    bg='gray20', fg='gold', bd=8, relief=GROOVE)
customer_details_frame.pack(fill=X, pady=5)

def create_label_entry(frame, text, row, column):
    Label(frame, text=text, font=('times new roman', 15, 'bold'),
          bg='gray20', fg='white', bd=8, relief=GROOVE).grid(row=row, column=column, padx=10)
    entry = Entry(frame, font=('times new roman', 15), bd=7, width=18)
    entry.grid(row=row, column=column+1, padx=5)
    return entry

name_entry = create_label_entry(customer_details_frame, 'Name', 0, 0)
phone_entry = create_label_entry(customer_details_frame, 'Phone Number', 0, 2)
bill_entry = create_label_entry(customer_details_frame, 'Bill No.', 0, 4)


Button(customer_details_frame, text='SEARCH', font=('Arial', 12, 'bold'),
       bd=7, width=10).grid(row=0, column=6, padx=20, pady=5)

# ---------------- Product Frames ----------------
productsFrame = Frame(root, bg='gray20')
productsFrame.pack(pady=5)

def create_product_frame(parent, title, items, row, column):
    frame = LabelFrame(parent, text=title,
                       font=('times new roman', 15, 'bold'),
                       bg='gray20', fg='gold', bd=8, relief=GROOVE)
    frame.grid(row=row, column=column, padx=10)
    entries = {}
    for i, item in enumerate(items):
        Label(frame, text=item, font=('times new roman', 15, 'bold'),
              bg='gray20', fg='white').grid(row=i, column=0, pady=5, padx=5)
        entry = Entry(frame, font=('times new roman', 15), width=10, bd=5)
        entry.grid(row=i, column=1, pady=5, padx=5)
        entry.insert(0,0)
        entries[item] = entry
    return entries

cosmetic_items = ['Bath Soap', 'Face Cream', 'Face Wash', 'Hair Spray', 'Hair Gel', 'Baby Lotion']
grocery_items = ['Rice', 'Oil', 'Daal', 'Wheat', 'Sugar', 'Tea']
colddrinks_items = ['Maaza', 'Pepsi', 'Sprite', 'Dew', 'Frooti', 'Coca Cola']

cosmetic_entries = create_product_frame(productsFrame, "Cosmetics", cosmetic_items, 0, 0)
grocery_entries = create_product_frame(productsFrame, "Grocery", grocery_items, 0, 1)
colddrinks_entries = create_product_frame(productsFrame, "Cold Drinks", colddrinks_items, 0, 2)

# ---------------- Bill Area ----------------
billframe = Frame(productsFrame, bd=8, relief=GROOVE)
billframe.grid(row=0, column=3, padx=10)

Label(billframe, text='Bill Area', font=('times new roman', 15, 'bold'),
      bd=7, relief=GROOVE).pack(fill=X)

scrollbar = Scrollbar(billframe, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

textarea = Text(billframe, height=15, width=50, yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

# ---------------- Bill Menu ----------------
billmenuframe = LabelFrame(root, text="Bill Menu",
                           font=('times new roman', 15, 'bold'),
                           bg='gray20', fg='gold', bd=8, relief=GROOVE)
billmenuframe.pack(fill=X, pady=5)

def create_bill_field(frame, text, row, column):
    Label(frame, text=text, font=('times new roman', 15, 'bold'),
          bg='gray20', fg='white').grid(row=row, column=column, padx=10, pady=5, sticky=W)
    entry = Entry(frame, font=('times new roman', 15, 'bold'), width=10, bd=5)
    entry.grid(row=row, column=column+1, padx=10, pady=5)
    return entry

cosmeticpriceEntry = create_bill_field(billmenuframe, "Cosmetic Price", 0, 0)
grocerypriceEntry = create_bill_field(billmenuframe, "Grocery Price", 1, 0)
drinkspriceEntry = create_bill_field(billmenuframe, "Cold Drink Price", 2, 0)

cosmetictaxEntry = create_bill_field(billmenuframe, "Cosmetic Tax", 0, 2)
grocerytaxEntry = create_bill_field(billmenuframe, "Grocery Tax", 1, 2)
colddrinkstaxEntry = create_bill_field(billmenuframe, "Cold Drink Tax", 2, 2)

s = Calculations(cosmetic_entries, grocery_entries, colddrinks_entries,
                 cosmeticpriceEntry, cosmetictaxEntry,
                 grocerypriceEntry, grocerytaxEntry,
                 drinkspriceEntry, colddrinkstaxEntry,
                 name_entry, phone_entry, textarea)


# ---------------- Action Buttons ----------------
buttonFrame = Frame(billmenuframe, bd=8, relief=GROOVE)
buttonFrame.grid(row=0, column=4, rowspan=3, padx=10)

commands = {
    'Total': s.total,
    'Bill': s.generate_bill,
    'Email': s.send_email,
    'Print': s.print_bill,
    'Clear': s.clear_fields
}

# Create buttons with commands
buttons = ['Total', 'Bill', 'Email', 'Print', 'Clear']
for idx, label in enumerate(buttons):
    Button(buttonFrame, text=label, font=('arial', 16, 'bold'),
           bg='gray20', fg='white', bd=5, width=8, pady=10,
           command=commands[label]).grid(row=0, column=idx, padx=5, pady=20)

# ---------------- Main Loop ----------------
root.mainloop()


# Map labels to functions
