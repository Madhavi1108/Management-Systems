from tkinter import *

# ---------- Initialize Main Window ----------
root = Tk()
root.title('Retail Billing System')
root.geometry('1270x685')

# ---------- Heading ----------
Label(root, text='Retail Billing System',
      font=('times new roman', 30, 'bold'),
      bg='gray20', fg='gold', bd=12, relief=GROOVE).pack(fill=X)

# ---------- Customer Details Frame ----------
customer_details_frame = LabelFrame(root, text='Customer Details',
                                    font=('times new roman', 15, 'bold'),
                                    bg='gray20', fg='gold', bd=8, relief=GROOVE)
customer_details_frame.pack(fill=X)

# Function to quickly create a label + entry combo in a frame
def create_label_entry(frame, label_text, row, column):
    Label(frame, text=label_text,
          font=('times new roman', 15, 'bold'),
          bg='gray20', fg='white', bd=8, relief=GROOVE).grid(row=row, column=column, padx=20)
    Entry(frame, font=('times new roman', 15), bd=7, width=18).grid(row=row, column=column+1, padx=8)

# Customer Info Fields
create_label_entry(customer_details_frame, 'Name', 0, 0)
create_label_entry(customer_details_frame, 'Phone Number.', 0, 2)
create_label_entry(customer_details_frame, 'Bill', 0, 4)

# Search Button
Button(customer_details_frame, text='SEARCH',
       font=('Arial', 12, 'bold'), bd=7, width=10).grid(row=0, column=6, padx=20, pady=5)

# ---------- Products Frame to Hold All Categories ----------
productsFrame = Frame(root)
productsFrame.pack()

# Function to create a labeled frame with multiple product items and their entry fields
def create_product_frame(parent, title, items, row, column):
    frame = LabelFrame(parent, text=title,
                       font=('times new roman', 15, 'bold'),
                       bg='gray20', fg='gold', bd=8, relief=GROOVE)
    frame.grid(row=row, column=column, padx=10)

    entries = {}  # Dictionary to hold product name and entry widget
    for index, item in enumerate(items):
        Label(frame, text=item, font=('times new roman', 15, 'bold'),
              bg='gray20', fg='white').grid(row=index, column=0, pady=5, padx=10)

        entry = Entry(frame, font=('times new roman', 15), width=10, bd=5)
        entry.grid(row=index, column=1, pady=5, padx=10)
        entries[item] = entry
    return entries

# Define product lists for each category
cosmetic_items = ['Bath Soap', 'Face Cream', 'Face Wash', 'Hair Spray', 'Hair Gel', 'Baby Lotion']
grocery_items = ['Rice', 'Oil', 'Daal', 'Wheat', 'Sugar', 'Tea']
colddrinks_items = ['Maaza', 'Pepsi', 'Sprite', 'Dew', 'Frooti', 'Coca Cola']

# Create labeled frames with entry widgets for each product category
cosmetic_entries = create_product_frame(productsFrame, "Cosmetics", cosmetic_items, row=0, column=0)
grocery_entries = create_product_frame(productsFrame, "Grocery", grocery_items, row=0, column=1)
colddrinks_entries = create_product_frame(productsFrame, "Cold Drinks", colddrinks_items, row=0, column=2)

# ---------- Bill Area Frame ----------
billframe = Frame(productsFrame, bd=8, relief=GROOVE)
billframe.grid(row=0, column=3, padx=10)

Label(billframe, text='Bill Area',
      font=('times new roman', 15, 'bold'), bd=7, relief=GROOVE).pack(fill=X)

# Scrollable text area for displaying the bill
scrollbar = Scrollbar(billframe, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

textarea = Text(billframe, height=15, width=50, yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

# ---------- Bill Menu Frame ----------
billmenuframe = LabelFrame(root, text="Bill Menu",
                           font=('times new roman', 15, 'bold'),
                           bg='gray20', fg='gold', bd=8, relief=GROOVE)
billmenuframe.pack()

# Function to create a label + entry pair in the bill menu section
def create_bill_field(frame, label, row, column):
    Label(frame, text=label,
          font=('times new roman', 15, 'bold'),
          bg='gray20', fg='white').grid(row=row, column=column, pady=5, padx=10, sticky='w')

    entry = Entry(frame, font=('times new roman', 15, 'bold'), width=10, bd=5)
    entry.grid(row=row, column=column+1, pady=5, padx=10)
    return entry

# Price fields for each category
cosmeticpriceEntry = create_bill_field(billmenuframe, "Cosmetic Price", 0, 0)
grocerypriceEntry = create_bill_field(billmenuframe, "Grocery Price", 1, 0)
drinkspriceEntry = create_bill_field(billmenuframe, "Cold Drink Price", 2, 0)

# Tax fields for each category
cosmetictaxEntry = create_bill_field(billmenuframe, "Cosmetic Tax", 0, 2)
grocerytaxEntry = create_bill_field(billmenuframe, "Grocery Tax", 1, 2)
colddrinkstaxEntry = create_bill_field(billmenuframe, "Cold Drink Tax", 2, 2)

buttonFrame = Frame(billmenuframe,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalButton = Button(buttonFrame, text='Total',font=('arial',16,'bold'),bg='gray20',fg='white',
                     bd=5, width=8, pady=10)
totalButton.grid(row=0,column=0, pady=20,padx=5)

billButton = Button(buttonFrame,text='Bill', font=('arial',16,'bold'),bg='gray20',fg='white',
                     bd=5, width=8, pady=10)
billButton.grid(row=0,column=1, pady=20,padx=5)

emailButton = Button(buttonFrame,text='Email', font=('arial',16,'bold'),bg='gray20',fg='white',
                     bd=5, width=8, pady=10)
emailButton.grid(row=0,column=2, pady=20,padx=5)

printButton = Button(buttonFrame,text='Print', font=('arial',16,'bold'),bg='gray20',fg='white',
                     bd=5, width=8, pady=10)
printButton.grid(row=0,column=3, pady=20,padx=5)

clearButton = Button(buttonFrame,text='Email', font=('arial',16,'bold'),bg='gray20',fg='white',
                     bd=5, width=8, pady=10)
clearButton.grid(row=0,column=4, pady=20,padx=5)

# ---------- Run the Application ----------
root.mainloop()
