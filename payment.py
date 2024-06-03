'''
Functions to record and manage payment details for subscriptions.
'''

import re

class Payment:
    def _init_(self):
        self.card_details = {}

    def enter_card_details(self):
        name = input("Enter the name on the card (only letters and spaces): ")
        card_number = input("Enter the card number: ")
        expiry_date = input("Enter the expiry date (MM/YY, e.g., 11/24): ")
        cvv = input("Enter the CVV (3 digits): ")

        self.card_details = {
            "name": name,
            "card_number": card_number,
            "expiry_date": expiry_date,
            "cvv": cvv
        }

        if self.validate_card_details():
            print("Payment successful!")
            
        else:
            print("Payment failed! Invalid card details.")

    def validate_card_details(self):
        return (
            self.validate_name(self.card_details["name"]) and
            self.validate_card_number(self.card_details["card_number"]) and
            self.validate_expiry_date(self.card_details["expiry_date"]) and
            self.validate_cvv(self.card_details["cvv"])
        )

    def validate_name(self, name):
        if not name or not all(x.isalpha() or x.isspace() for x in name):
            print("Invalid name on the card. Only letters and spaces are allowed.")
            return False
        return True

    def validate_card_number(self, card_number):
        # Check if the card number is exactly 16 digits in the format 4444 4444 4444 4444
        if not re.fullmatch(r'(\d{4} ){3}\d{4}', card_number):
            print("Invalid card number.")
            return False
        return True

    def validate_expiry_date(self, expiry_date):
        if not re.fullmatch(r'(0[1-9]|1[0-2])/\d{2}', expiry_date):
            print("Invalid expiry date. Use MM/YY format, e.g., 11/24.")
            return False
        return True

    def validate_cvv(self, cvv):
        if not re.fullmatch(r'\d{3}', cvv):
            print("Invalid CVV. It should be exactly 3 digits.")
            return False
        return True

if __name__ == "__main__":
    payment = Payment()
    payment.enter_card_details()