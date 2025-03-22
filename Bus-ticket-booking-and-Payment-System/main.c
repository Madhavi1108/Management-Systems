#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <time.h>

#define MAX_BOOKINGS 100

typedef struct {
    char passengerName[50];
    int age;
    char contactNumber[15];
    char travelDate[15];
    char busType[20];
    float ticketPrice;
    int isCancelled;
} TicketBooking;

typedef struct {
    char paymentMethod[20];
    float amount;
    char transactionID[20];
} Payment;

TicketBooking bookings[MAX_BOOKINGS];
int bookingCount = 0;

float calculateTicketPrice(const char *busType) {
    if (strcmp(busType, "ac") == 0) return 500.0;
    if (strcmp(busType, "non-ac") == 0) return 300.0;
    return 0.0;
}

void toLowerCase(char *str) {
    for (int i = 0; str[i]; i++) {
        str[i] = tolower(str[i]);
    }
}

int isAlpha(const char *str) {
    for (int i = 0; str[i]; i++) {
        if (!isalpha(str[i]) && str[i] != ' ') {
            return 0; // Not all characters are alphabetic
        }
    }
    return 1; // All characters are alphabetic
}

int isValidAge(int age) {
    return age >= 10 && age <= 70; // Valid age range
}

int isInteger(const char *str) {
    // Check if the string represents a valid integer
    for (int i = 0; str[i]; i++) {
        if (!isdigit(str[i])) {
            return 0; // Not a valid integer
        }
    }
    return 1; // Valid integer
}

int isValidDate(const char *date) {
    if (strlen(date) != 10) return 0; // Length must be 10
    if (date[2] != '-' || date[5] != '-') return 0; // Check hyphens

    for (int i = 0; i < 10; i++) {
        if (i == 2 || i == 5) continue; // Skip hyphens
        if (!isdigit(date[i])) return 0; // Not a digit
    }
    return 1; // Valid date format
}

// Function prototype for processPayment
void processPayment(float totalAmount);

void bookTicket() {
    char ticketInput[10]; // Buffer to hold the number of tickets input
    int numberOfTickets;

    // Ask for the number of tickets to book
    while (1) {
        printf("Enter the number of tickets to book (1 to %d): ", MAX_BOOKINGS - bookingCount);
        scanf("%s", ticketInput); // Read input as a string

        if (!isInteger(ticketInput)) {
            printf("Invalid input! Please enter a valid integer number.\n");
            continue; // Prompt again
        }

        numberOfTickets = atoi(ticketInput); // Convert string to integer

        // Validate the number of tickets
        if (numberOfTickets < 1 || numberOfTickets > (MAX_BOOKINGS - bookingCount)) {
            printf("Invalid number of tickets! Please enter a number between 1 and %d.\n", MAX_BOOKINGS - bookingCount);
        } else {
            break; // Valid input received
        }
    }

    float totalAmount = 0.0; // Initialize total amount

    for (int i = 0; i < numberOfTickets; i++) {
        if (bookingCount >= MAX_BOOKINGS) {
            printf("Booking limit reached. Cannot book more tickets.\n");
            break;
        }

        TicketBooking booking;
        do {
            printf("Enter passenger name for ticket %d: ", i + 1);
            getchar(); // Consume leftover newline
            fgets(booking.passengerName, sizeof(booking.passengerName), stdin);
            booking.passengerName[strcspn(booking.passengerName, "\n")] = 0; // Remove newline

            if (!isAlpha(booking.passengerName)) {
                printf("Invalid name! Please enter alphabets only.\n");
            }
        } while (!isAlpha(booking.passengerName));

        char ageInput[10]; // Buffer to hold the age input as a string
        int validInput = 0;

        while (!validInput) {
            printf("Enter age for ticket %d: ", i + 1);
            scanf("%s", ageInput); // Read input as a string

            if (!isInteger(ageInput)) {
                printf("Invalid input! Please enter a valid integer number.\n");
                continue; // Prompt again
            }

            booking.age = atoi(ageInput); // Convert string to integer

            if (!isValidAge(booking.age)) {
                printf("Invalid age! Please enter a valid age between 10 and 70.\n");
            } else {
                validInput = 1; // Valid input received
            }
        }

        do {
            printf("Enter contact number (10 digits) for ticket %d: ", i + 1);
            scanf("%s", booking.contactNumber);
            if (strlen(booking.contactNumber) != 10 || strspn(booking.contactNumber, "0123456789") != 10) {
                printf("Invalid contact number! Please enter exactly 10 digits.\n");
            } else {
                break;
            }
        } while (1);

        // Validate travel date
        do {
            printf("Enter travel date (DD-MM-YYYY) for ticket %d: ", i + 1);
            scanf("%s", booking.travelDate);

            if (!isValidDate(booking.travelDate)) {
                printf("Invalid date format! Please enter the date in DD-MM-YYYY format using digits only.\n");
                continue; // Prompt again
            }

            // Extract day, month, and year
            char dayStr[3] = {booking.travelDate[0], booking.travelDate[1], '\0'};
            char monthStr[3] = {booking.travelDate[3], booking.travelDate[4], '\0'};
            char yearStr[5] = {booking.travelDate[6], booking.travelDate[7], booking.travelDate[8], booking.travelDate[9], '\0'};

            int day = atoi(dayStr);
            int month = atoi(monthStr);
            int year = atoi(yearStr);

            // Get today's date
            time_t t = time(NULL);
            struct tm tm = *localtime(&t);
            int todayDay = tm.tm_mday;
            int todayMonth = tm.tm_mon + 1; // Months are 0-11 in struct tm
            int todayYear = tm.tm_year + 1900; // Years since 1900

            // Check if the input date is less than today's date
            if (year < todayYear || (year == todayYear && month < todayMonth) ||
                (year == todayYear && month == todayMonth && day < todayDay)) {
                printf("Travel date cannot be in the past! Please enter a date that is today or in the future.\n");
                continue; // Prompt again
            }

            // If all checks pass, break out of the loop
            break;

        } while (1);

        printf("Enter bus type (AC/Non-AC) for ticket %d: ", i + 1);
        scanf("%s", booking.busType);
        toLowerCase(booking.busType);

        booking.ticketPrice = calculateTicketPrice(booking.busType);
        if (booking.ticketPrice == 0.0) {
            printf("Invalid bus type! Booking failed for ticket %d.\n", i + 1);
            return;
        }
        if (booking.age >= 60) {
            booking.ticketPrice = booking.ticketPrice - (0.1 * booking.ticketPrice); // 10% discount for seniors
        }

        totalAmount += booking.ticketPrice; // Add to total amount
        booking.isCancelled = 0;
        bookings[bookingCount] = booking; // Store booking
        printf("Booking successful for ticket %d! Ticket Price: %.2f\n", i + 1, booking.ticketPrice);
        printf("Your booking index is: %d\n", bookingCount);
        bookingCount++;
    }

    // Process payment after booking
    processPayment(totalAmount);
}

void processPayment(float totalAmount) {
    int choice;
    char cardNumber[20], cvv[5], expiry[6], upiID[50];

    while (1) {
        printf("\n====== Welcome to Secure Payment Gateway ======\n");
        printf("Total Amount: %.2f\n", totalAmount);
        printf("Select Payment Method:\n");
        printf("1. Credit Card\n2. Debit Card\n3. UPI\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        if (choice == 1 || choice == 2) {
            printf("Enter Card Number (16 digits, no spaces): ");
            scanf("%s", cardNumber);
            if (strlen(cardNumber) != 16 || strspn(cardNumber, "0123456789") != 16) {
                printf("Error: Invalid Card Number. Please try again.\n");
                continue;
            }

            printf("Enter CVV (3 or 4 digits, no spaces): ");
            scanf("%s", cvv);
            if (strlen(cvv) != 3 && strlen(cvv) != 4) {
                printf("Error: Invalid CVV. Please try again.\n");
                continue;
            }

            printf("Enter Expiry Date (MM/YY, no spaces): ");
            scanf("%s", expiry);

            // Get today's date
            time_t t = time(NULL);
            struct tm tm = *localtime(&t);
            int currentMonth = tm.tm_mon + 1; // Months are 0-11 in struct tm
            int currentYear = tm.tm_year % 100; // Get last two digits of the year

            if (strlen(expiry) != 5 || expiry[2] != '/') {
                printf("Error: Invalid expiry date format. Please try again.\n");
                continue;
            }

            // Extract month and year from expiry
            int expiryMonth = (expiry[0] - '0') * 10 + (expiry[1] - '0'); // Convert MM to integer
            int expiryYear = (expiry[3] - '0') * 10 + (expiry[4] - '0'); // Convert YY to integer

            // Check if the card is expired
            if (expiryYear < currentYear || (expiryYear == currentYear && expiryMonth < currentMonth)) {
                printf("Error: Expired card. Please use a valid card.\n");
                continue;
            }

            printf("Payment Successful via Card!\n");
            printf("Transaction Completed. Thank you!\n");
            break;
        } else if (choice == 3) {
            printf("Enter UPI ID (e.g., user@bank): ");
            scanf("%s", upiID);

            // Validate UPI ID
            if (strchr(upiID, '@') == NULL ||
                upiID[0] == '@' ||
                upiID[strlen(upiID) - 1] == '@') {
                printf("Error: Invalid UPI ID. Please try again.\n");
                continue;
            }

            // Check for special characters (except for '@')
            for (int i = 0; i < strlen(upiID); i++) {
                if (!isalnum(upiID[i]) && upiID[i] != '@') {
                    printf("\nError: UPI ID can only contain alphanumeric characters and '@'.\n");
                    continue;
                }
            }

            printf("Payment Successful via UPI!\n");
            printf("Transaction Completed. Thank you!\n");
            break;
        } else {
            printf("Error: Invalid payment method selected. Please try again.\n");
            continue;
        }
    }
}

void cancelBooking(int bookingIndex) {
    if (bookingIndex < 0 || bookingIndex >= bookingCount) {
        printf("Invalid booking index.\n");
        return;
    }
    if (bookings[bookingIndex].isCancelled) {
        printf("This booking has already been cancelled.\n");
        return;
    }

    bookings[bookingIndex].isCancelled = 1;
    printf("Booking for %s has been cancelled.\n", bookings[bookingIndex].passengerName);
}

void displayBooking(int bookingIndex) {
    if (bookingIndex < 0 || bookingIndex >= bookingCount) {
        printf("Invalid booking index.\n");
        return;
    }

    TicketBooking booking = bookings[bookingIndex];
    printf("\n--- Booking Confirmation ---\n");
    printf("Passenger Name: %s\n", booking.passengerName);
    printf("Age: %d\n", booking.age);
    printf("Contact Number: %s\n", booking.contactNumber);
    printf("Travel Date: %s\n", booking.travelDate);
    printf("Bus Type: %s\n", booking.busType);
    printf("Ticket Price: %.2f\n", booking.ticketPrice);
    printf("Booking Status: %s\n", booking.isCancelled ? "Cancelled" : "Confirmed");
}

int main() {
    int choice, index;
    while (1) {
        printf("\n1. Book Ticket\n2. Cancel Booking\n3. Display Booking\n4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                bookTicket();
                break;
            case 2:
                printf("Enter booking index to cancel: ");
                scanf("%d", &index);
                cancelBooking(index);
                break;
            case 3:
                printf("Enter booking index to display: ");
                scanf("%d", &index);
                displayBooking(index);
                break;
            case 4:
                printf("Exiting the program. Thank you!\n");
                return 0;
            default:
                printf("Invalid choice. Try again.\n");
        }
    }
} 
