# Simple Bus Ticket Booking System (C)

This is a basic command-line bus ticket booking system implemented in C. It allows users to book tickets, cancel existing bookings, and display booking details.

## Overview

The system manages bus ticket bookings with the following features:

* **Booking Tickets:** Allows users to input passenger details (name, age, contact number, travel date, bus type) and book one or more tickets at a time.
* **Bus Types and Pricing:** Supports two bus types: AC (₹500.00) and Non-AC (₹300.00).
* **Senior Citizen Discount:** Applies a 10% discount on the ticket price for passengers aged 60 or older.
* **Input Validation:** Includes validation for passenger name (alphabetic characters only), age (between 10 and 70), contact number (exactly 10 digits), and travel date (DD-MM-YYYY format, future dates only).
* **Payment Processing:** Simulates a secure payment gateway with options for Credit Card, Debit Card, and UPI. Basic format validation is performed for payment details.
* **Cancellation:** Allows users to cancel a booking using a unique booking index.
* **Display Booking:** Enables users to view the details of a booking using its index.
* **Maximum Bookings:** The system can handle a maximum of 100 bookings.

## Getting Started

### Prerequisites

* A C compiler (like GCC) installed on your system.
* A terminal or command prompt to compile and run the program.

### Compilation

1.  Save the provided C code as a `.c` file (e.g., `bus_booking.c`).
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you saved the file.
4.  Compile the code using the GCC compiler:

    ```bash
    gcc bus_booking.c -o bus_booking
    ```

### Running the Program

1.  After successful compilation, run the executable:

    ```bash
    ./bus_booking
    ```

    This will start the bus ticket booking system.

## Usage

Once the program is running, you will see a menu with the following options:

1.  **Book Ticket:** Select this option to book one or more bus tickets. You will be prompted to enter details for each passenger, including name, age, contact number, travel date, and bus type (AC or Non-AC). After entering the details, the system will calculate the price (applying discounts if applicable) and guide you through a simulated payment process. You will receive a booking index for each successful booking.
2.  **Cancel Booking:** Select this option to cancel an existing booking. You will be asked to enter the booking index of the ticket you wish to cancel.
3.  **Display Booking:** Select this option to view the details of a previously made booking. You will need to enter the booking index of the ticket you want to display.
4.  **Exit:** Select this option to close the bus ticket booking system.

Follow the on-screen prompts to interact with the system.

## Data Structures

The program uses the following structures to manage booking information:

* **`TicketBooking`:** Stores details for each ticket booking, including passenger name, age, contact number, travel date, bus type, ticket price, and cancellation status.
* **`Payment`:** Stores payment information, including the payment method, amount, and a transaction ID (currently not fully implemented).

An array `bookings` of type `TicketBooking` with a maximum size of `MAX_BOOKINGS` (100) is used to store all the ticket bookings. `bookingCount` keeps track of the current number of bookings.

## Error Handling and Validation

The system includes basic input validation to ensure data integrity:

* Passenger names must contain only alphabetic characters and spaces.
* Age must be within the range of 10 to 70.
* Contact numbers must be exactly 10 digits.
* Travel dates must be in the DD-MM-YYYY format and cannot be in the past.
* Bus type must be either "AC" or "Non-AC" (case-insensitive).
* Payment details (card number, CVV, expiry, UPI ID) undergo basic format checks.
* Invalid booking indices are handled during cancellation and display operations.

## Limitations

This is a basic implementation and has the following limitations:

* **No persistent data storage:** Booking information is lost when the program exits.
* **Simplified payment processing:** The payment gateway is simulated and does not interact with any real payment systems.
* **Limited error handling:** More robust error handling could be implemented.
* **Single bus route/schedule:** The system does not manage different bus routes or schedules.
* **No seat selection:** Seats are not assigned during booking.

## Potential Enhancements

The system could be enhanced with the following features:

* Implement file-based or database storage to persist booking data.
* Integrate with a real payment gateway.
* Add more detailed error handling and user feedback.
* Implement functionality for managing bus routes, schedules, and seat availability.
* Add a user interface (GUI) for easier interaction.

## License

This project is provided as is and is intended for educational purposes. Feel free to modify and use it according to your needs.
