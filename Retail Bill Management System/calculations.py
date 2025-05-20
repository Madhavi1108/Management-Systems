# calculations.py
import random
import smtplib
import re
import os
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from database import *
from tkinter import messagebox
from tkinter import *
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from dotenv import load_dotenv

load_dotenv(dotenv_path="file.env")


class Calculations:
    def __init__(self, cosmetic_entries, grocery_entries, colddrinks_entries,
                 cosmeticpriceEntry, cosmetictaxEntry,
                 grocerypriceEntry, grocerytaxEntry,
                 drinkspriceEntry, colddrinkstaxEntry,
                 name_entry, phone_entry, email_entry, textarea):

        self.cosmetic_entries = cosmetic_entries
        self.grocery_entries = grocery_entries
        self.colddrinks_entries = colddrinks_entries

        self.cosmeticpriceEntry = cosmeticpriceEntry
        self.cosmetictaxEntry = cosmetictaxEntry
        self.grocerypriceEntry = grocerypriceEntry
        self.grocerytaxEntry = grocerytaxEntry
        self.drinkspriceEntry = drinkspriceEntry
        self.colddrinkstaxEntry = colddrinkstaxEntry

        self.name_entry = name_entry
        self.phone_entry = phone_entry
        self.email_entry = email_entry
        self.textarea = textarea

        # Store item info for easy access
        self.cosmetic_items = {
            'Bath Soap': 20,
            'Face Cream': 50,
            'Face Wash': 100,
            'Hair Spray': 150,
            'Hair Gel': 80,
            'Baby Lotion': 60
        }

        self.grocery_items = {
            'Rice': 30,
            'Oil': 100,
            'Daal': 120,
            'Wheat': 50,
            'Sugar': 140,
            'Tea': 80
        }

        self.colddrinks_items = {
            'Maaza': 50,
            'Pepsi': 20,
            'Sprite': 30,
            'Dew': 20,
            'Frooti': 45,
            'Coca Cola': 90
        }

        # For storing current bill details
        self.current_bill_data = None

    def total(self):
        # Cosmetic
        total_cosmetic = sum(int(self.cosmetic_entries[name].get() or 0) * price
                             for name, price in self.cosmetic_items.items())
        self.cosmeticpriceEntry.delete(0, 'end')
        self.cosmeticpriceEntry.insert(0, f'{total_cosmetic} Rs')
        self.cosmetictaxEntry.delete(0, 'end')
        self.cosmetictaxEntry.insert(0, total_cosmetic * 0.12)

        # Grocery
        total_grocery = sum(int(self.grocery_entries[name].get() or 0) * price
                            for name, price in self.grocery_items.items())
        self.grocerypriceEntry.delete(0, 'end')
        self.grocerypriceEntry.insert(0, f'{total_grocery} Rs')
        self.grocerytaxEntry.delete(0, 'end')
        self.grocerytaxEntry.insert(0, total_grocery * 0.05)

        # Cold Drinks
        total_colddrinks = sum(int(self.colddrinks_entries[name].get() or 0) * price
                               for name, price in self.colddrinks_items.items())
        self.drinkspriceEntry.delete(0, 'end')
        self.drinkspriceEntry.insert(0, f'{total_colddrinks} Rs')
        self.colddrinkstaxEntry.delete(0, 'end')
        self.colddrinkstaxEntry.insert(0, total_colddrinks * 0.08)

    def generate_bill(self):
        customer_name = self.name_entry.get().strip()
        customer_phone = self.phone_entry.get().strip()
        customer_email = self.email_entry.get().strip()

        if not customer_phone.isdigit() or len(customer_phone) != 10:
            messagebox.showerror("Error", "Enter a valid 10-digit phone number.")
            return

        if customer_name == '' or customer_phone == '':
            messagebox.showerror("Error", "Customer Details are required")
            return

        bill_no = str(random.randint(1000, 9999))
        self.textarea.delete('1.0', END)
        self.textarea.insert(END, "\n\t*** WELCOME TO THE STORE ***\n")
        self.textarea.insert(END, f"\nBill No      : {bill_no}")
        self.textarea.insert(END, f"\nCustomer Name: {customer_name}")
        self.textarea.insert(END, f"\nPhone Number : {customer_phone}")
        if customer_email:
            self.textarea.insert(END, f"\nEmail        : {customer_email}")
        self.textarea.insert(END, "\n===================================")
        self.textarea.insert(END, "\nProduct\t\tQty\tPrice")
        self.textarea.insert(END, "\n===================================\n")

        # Initialize bill data for saving and access by other methods
        self.current_bill_data = {
            'bill_no': bill_no,
            'name': customer_name,
            'phone': customer_phone,
            'email': customer_email,
            'total': 0,
            'bill_text': '',
            'items': []  # Store all purchased items for better formatting
        }

        def process_items(entries, item_dict):
            total = 0
            for name, price in item_dict.items():
                qty = int(entries[name].get() or 0)
                self.current_bill_data[name] = qty
                if qty > 0:
                    line_total = qty * price
                    total += line_total
                    self.textarea.insert(END, f"{name}\t\t{qty}\t{line_total}\n")
                    # Store item details for PDF and email
                    self.current_bill_data['items'].append({
                        'name': name,
                        'quantity': qty,
                        'price': price,
                        'total': line_total
                    })
            return total

        total_cosmetics = process_items(self.cosmetic_entries, self.cosmetic_items)
        total_grocery = process_items(self.grocery_entries, self.grocery_items)
        total_drinks = process_items(self.colddrinks_entries, self.colddrinks_items)

        cosmetic_tax = total_cosmetics * 0.12
        grocery_tax = total_grocery * 0.05
        drinks_tax = total_drinks * 0.08

        self.textarea.insert(END, "\n-----------------------------------\n")
        self.textarea.insert(END, f"Cosmetic Tax\t\t\t{cosmetic_tax:.2f}")
        self.textarea.insert(END, f"\nGrocery Tax\t\t\t{grocery_tax:.2f}")
        self.textarea.insert(END, f"\nCold Drink Tax\t\t\t{drinks_tax:.2f}")

        grand_total = total_cosmetics + total_grocery + total_drinks + cosmetic_tax + grocery_tax + drinks_tax
        self.textarea.insert(END, "\n===================================\n")
        self.textarea.insert(END, f"Total Amount: {grand_total:.2f} Rs\n")
        self.textarea.insert(END, "===================================\n")

        self.current_bill_data['total'] = grand_total
        self.current_bill_data['cosmetic_tax'] = cosmetic_tax
        self.current_bill_data['grocery_tax'] = grocery_tax
        self.current_bill_data['drinks_tax'] = drinks_tax
        self.current_bill_data['bill_text'] = self.textarea.get('1.0', END)

        save_bill(self.current_bill_data)
        messagebox.showinfo("Success", f"Bill No {bill_no} saved successfully!")

    def send_email(self):
        if not self.current_bill_data:
            bill_content = self.textarea.get('1.0', END).strip()
            if not bill_content:
                messagebox.showwarning("Warning", "No bill to send. Generate the bill first.")
                return

        customer_email = self.email_entry.get().strip()

        if not customer_email:
            messagebox.showerror("Error", "Email address is required to send the bill.")
            return

        if not re.match(r"[^@]+@[^@]+\.[^@]+", customer_email):
            messagebox.showerror("Error", "Invalid email format.")
            return

        try:
            # Generate PDF file first
            filename = self.generate_pdf_file()
            if not filename:
                return  # Error already shown in generate_pdf_file

            # Create a multipart email with HTML content
            msg = MIMEMultipart()
            msg['Subject'] = 'Your Bill from Retail Store'
            msg['From'] = os.getenv('EMAIL_USER')
            msg['To'] = customer_email

            # Create HTML content for the email
            html_content = self.create_html_bill()
            msg.attach(MIMEText(html_content, 'html'))

            # Attach the PDF file
            with open(filename, 'rb') as file:
                attachment = MIMEApplication(file.read(), _subtype="pdf")
                attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(filename))
                msg.attach(attachment)

            # Send the email
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(os.getenv('EMAIL_USER'), os.getenv('EMAIL_PASS'))
            server.send_message(msg)
            server.quit()

            messagebox.showinfo("Email Sent", f"Bill sent to {customer_email} with PDF attachment")
        except Exception as e:
            messagebox.showerror("Email Error", str(e))

    def create_html_bill(self):
        """Create a nicely formatted HTML bill for email"""

        # Get data from current bill or text area
        if self.current_bill_data:
            bill_data = self.current_bill_data
        else:
            # Create basic bill data from text area
            bill_text = self.textarea.get('1.0', END)
            lines = bill_text.splitlines()

            # Extract bill information (basic)
            bill_no = "Unknown"
            customer_name = "Customer"
            for line in lines:
                if "Bill No" in line:
                    bill_no = line.split(":")[1].strip()
                elif "Customer Name" in line:
                    customer_name = line.split(":")[1].strip()

            bill_data = {
                'bill_no': bill_no,
                'name': customer_name,
                'bill_text': bill_text,
                'items': []  # We don't have parsed items in this case
            }

        # Create HTML content
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }}
                .header {{ text-align: center; padding: 10px; background-color: #f5f5f5; margin-bottom: 20px; }}
                .customer-info {{ margin-bottom: 20px; }}
                table {{ width: 100%; border-collapse: collapse; margin-bottom: 20px; }}
                th, td {{ padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }}
                th {{ background-color: #f2f2f2; }}
                .total-row {{ font-weight: bold; }}
                .footer {{ text-align: center; margin-top: 30px; font-size: 12px; color: #666; }}
            </style>
        </head>
        <body>
            <div class="header">
                <h2>*** WELCOME TO THE STORE ***</h2>
                <p>Bill No: {bill_data['bill_no']}</p>
            </div>

            <div class="customer-info">
                <p><strong>Customer Name:</strong> {bill_data['name']}</p>
                <p><strong>Phone Number:</strong> {bill_data.get('phone', 'N/A')}</p>
            </div>
        """

        # Add items table if we have parsed items
        if bill_data['items']:
            html += """
            <table>
                <tr>
                    <th>Product</th>
                    <th>Quantity</th>
                    <th>Unit Price</th>
                    <th>Total</th>
                </tr>
            """

            for item in bill_data['items']:
                html += f"""
                <tr>
                    <td>{item['name']}</td>
                    <td>{item['quantity']}</td>
                    <td>{item['price']} Rs</td>
                    <td>{item['total']} Rs</td>
                </tr>
                """

            # Add tax and total
            if 'cosmetic_tax' in bill_data:
                html += f"""
                <tr>
                    <td colspan="3" style="text-align: right;"><strong>Cosmetic Tax:</strong></td>
                    <td>{bill_data['cosmetic_tax']:.2f} Rs</td>
                </tr>
                <tr>
                    <td colspan="3" style="text-align: right;"><strong>Grocery Tax:</strong></td>
                    <td>{bill_data['grocery_tax']:.2f} Rs</td>
                </tr>
                <tr>
                    <td colspan="3" style="text-align: right;"><strong>Cold Drinks Tax:</strong></td>
                    <td>{bill_data['drinks_tax']:.2f} Rs</td>
                </tr>
                <tr class="total-row">
                    <td colspan="3" style="text-align: right;"><strong>TOTAL:</strong></td>
                    <td>{bill_data['total']:.2f} Rs</td>
                </tr>
                """

            html += "</table>"
        else:
            # If we don't have parsed items, include the raw bill text
            html += f"""
            <pre style="font-family: monospace; white-space: pre-wrap;">
{bill_data['bill_text']}
            </pre>
            """

        # Add footer
        html += """
            <div class="footer">
                <p>Thank you for shopping with us!</p>
                <p>This is a computer-generated bill and does not require a signature.</p>
            </div>
        </body>
        </html>
        """

        return html

    def print_bill(self):
        """Generate a well-formatted PDF bill"""
        filename = self.generate_pdf_file()
        if filename:
            messagebox.showinfo("PDF Saved", f"Bill saved as {filename}")

    def generate_pdf_file(self):
        """Generate PDF file and return the filename"""
        if not self.current_bill_data:
            bill_text = self.textarea.get('1.0', END).strip()
            if not bill_text:
                messagebox.showwarning("Warning", "No bill to print.")
                return None

        try:
            # Get bill number for filename
            if self.current_bill_data:
                bill_no = self.current_bill_data['bill_no']
            else:
                # Try to extract bill number from text
                lines = self.textarea.get('1.0', END).splitlines()
                bill_no_line = next((line for line in lines if "Bill No" in line), None)
                bill_no = bill_no_line.split(":")[1].strip() if bill_no_line else "unknown"

            filename = f"bill_{bill_no}.pdf"
            file_path = os.path.join(os.getcwd(), filename)

            # Create PDF with ReportLab
            doc = SimpleDocTemplate(
                file_path,
                pagesize=letter,
                rightMargin=72,
                leftMargin=72,
                topMargin=72,
                bottomMargin=72
            )

            # Define styles
            styles = getSampleStyleSheet()
            styles.add(ParagraphStyle(
                name='Center',
                parent=styles['Heading1'],
                alignment=1,  # Center alignment
            ))

            # Create content elements
            elements = []

            # Header
            elements.append(Paragraph("*** WELCOME TO THE STORE ***", styles['Center']))
            elements.append(Spacer(1, 0.25 * inch))

            # Bill details
            if self.current_bill_data:
                bill_data = self.current_bill_data
                elements.append(Paragraph(f"Bill No: {bill_data['bill_no']}", styles['Normal']))
                elements.append(Paragraph(f"Customer Name: {bill_data['name']}", styles['Normal']))
                elements.append(Paragraph(f"Phone Number: {bill_data['phone']}", styles['Normal']))
                if bill_data.get('email'):
                    elements.append(Paragraph(f"Email: {bill_data['email']}", styles['Normal']))
            else:
                # Extract from text area - basic version
                lines = self.textarea.get('1.0', END).splitlines()
                for line in lines[:5]:  # First few lines likely contain header info
                    if ":" in line and not "===" in line and not "---" in line:
                        elements.append(Paragraph(line, styles['Normal']))

            elements.append(Spacer(1, 0.25 * inch))

            # Items table
            if self.current_bill_data and self.current_bill_data['items']:
                # Create table data
                data = [['Product', 'Qty', 'Unit Price', 'Total']]

                # Add items to table
                for item in self.current_bill_data['items']:
                    data.append([
                        item['name'],
                        str(item['quantity']),
                        f"{item['price']} Rs",
                        f"{item['total']} Rs"
                    ])

                # Add tax rows
                data.append(['', '', 'Cosmetic Tax:', f"{self.current_bill_data['cosmetic_tax']:.2f} Rs"])
                data.append(['', '', 'Grocery Tax:', f"{self.current_bill_data['grocery_tax']:.2f} Rs"])
                data.append(['', '', 'Cold Drinks Tax:', f"{self.current_bill_data['drinks_tax']:.2f} Rs"])
                data.append(['', '', 'Total Amount:', f"{self.current_bill_data['total']:.2f} Rs"])

                # Create table
                table = Table(data, colWidths=[2 * inch, 0.7 * inch, 1 * inch, 1 * inch])

                # Style the table
                table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                    ('BACKGROUND', (0, 1), (-1, -5), colors.white),
                    ('GRID', (0, 0), (-1, -5), 1, colors.black),
                    ('ALIGN', (1, 1), (-1, -1), 'RIGHT'),
                    ('FONTNAME', (0, -4), (-1, -1), 'Helvetica-Bold'),
                ]))

                elements.append(table)
            else:
                # If we don't have parsed items, just include the raw bill text
                bill_text = self.textarea.get('1.0', END)
                for line in bill_text.splitlines():
                    if line.strip():  # Skip empty lines
                        elements.append(Paragraph(line, styles['Normal']))

            # Add footer
            elements.append(Spacer(1, 0.5 * inch))
            elements.append(Paragraph("Thank you for shopping with us!", styles['Center']))
            elements.append(Paragraph("This is a computer-generated bill and does not require a signature.",
                                      styles['Center']))

            # Build the PDF
            doc.build(elements)
            return file_path

        except Exception as e:
            messagebox.showerror("Error", f"Could not save bill as PDF: {str(e)}")
            return None

    def clear_fields(self):
        for entry_dict in [self.cosmetic_entries, self.grocery_entries, self.colddrinks_entries]:
            for entry in entry_dict.values():
                entry.delete(0, END)

        for field in [self.cosmeticpriceEntry, self.cosmetictaxEntry,
                      self.grocerypriceEntry, self.grocerytaxEntry,
                      self.drinkspriceEntry, self.colddrinkstaxEntry]:
            field.delete(0, END)

        self.name_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.textarea.delete('1.0', END)

        # Clear current bill data
        self.current_bill_data = None