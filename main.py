'''
Contains the main logic of the application.
Handles user authentication and menu navigation.
'''

import csv
import os
from reminder import Reminder # Written by Baran Kara
from subscription import Subscriptions # Written by Umut Akdumanlı 
from analysis import Analysis # Written by Alpay Albayrak
from payment import Payment # Written by Kübra Kalan  
from search import Search # Written by Arda ÇAM

class Application:
    def __init__(self):
        self.users = self.load_users()
        self.username = None
        self.password = None
        
        # Construct all necessary classes
        self.subs = Subscriptions()
        self.reminder = Reminder()
        self.payment = Payment()
        self.analysis = Analysis('subscriptions.csv', 'prices.csv')
        self.search = Search()
        

    def load_users(self, filename='users.csv'):
        users = {}
        if os.path.exists(filename):
            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:  # Check if row is not empty
                        username, password = row
                        users[username] = password
        return users

    def save_user(self, username, password, filename='users.csv'):
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, password])

    def sign_in(self):
        self.username = input("Enter your username: ")
        self.password = input("Enter your password: ")

        if self.username in self.users and self.users[self.username] == self.password:
            print("Sign in successful!")
            return True
        else:
            print("Invalid username or password.")
            return False

    def sign_up(self):
        self.username = input("Choose a username: ")
        if self.username in self.users:
            print("Username already exists. Please choose a different username.")
            return

        self.password = input("Choose a password: ")
        self.users[self.username] = self.password
        self.save_user(self.username, self.password)
        print("Sign up successful!")

    def display_menu(self):
        while True:
            print("\nMain Menu:")
            print("1. Display")
            print("2. Payment")
            print("3. Settings")
            print("4. Exit")

            choice = input("Choose an option (1/2/3/4): ").strip()

            if choice == "1":
                self.display_submenu()
            elif choice == "2":
                print("Payment selected.")
                self.payment.enter_card_details()
            elif choice == "3":
                self.settings_submenu()
            elif choice == "4":
                print("Exiting the menu.")
                break
            else:
                print("Invalid choice. Please choose 1, 2, 3, or 4.")

    def display_submenu(self):
        while True:
            print("\nDisplay Menu:")
            print("1. Subscription")
            print("2. Reminder")
            print("3. Expanse Analysis")
            print("4. Back to Main Menu")

            choice = input("Choose an option (1/2/3/4): ").strip()

            if choice == "1":
                print("Subscription selected.")                
                self.subs.display()
            elif choice == "2":
                print("Reminder selected.")
                self.reminder.main()
            elif choice == "3":
                print("Expanse Analysis selected.")
                self.analysis.total_price(self.username)
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please choose 1, 2, 3, or 4.")

    def settings_submenu(self):
        while True:
            print("\nSettings Menu:")
            print("1. Subscription")
            print("2. Search")
            print("3. Back to Main Menu")

            choice = input("Choose an option (1/2/3): ").strip()

            if choice == "1":
                print("Subscription selected.")

                print("\nSubscriptions Setting Menu:")
                print("1. Add new subscription")
                print("2. Update a subscription")
                print("3. Delete a subscription")

                sub_choice = input("Choose an option (1/2/3): ").strip()
                    
                if sub_choice == "1":
                    print("Add selected")
                    new_subscription_name = input("Enter subscripted applications name: ")
                    new_subscription_payment_date = input("Enter subscripted applications payment day: ")
                    self.subs.add(self.username, new_subscription_name, new_subscription_payment_date)
                                        
                elif sub_choice == "2":
                    print("Update selected.")
                    old_subscription_name = input("Enter the name of the subscription to be replaced: ")
                    new_subscription_name = input("Enter subscripted applications name: ")
                    new_subscription_payment_date = input("Enter subscripted applications payment day: ")
                    self.subs.update(self.username, old_subscription_name, new_subscription_name, new_subscription_payment_date)
                                       
                elif sub_choice == "3":
                    print("Delete selected")
                    subscription_name_to_delete = input("enter subscriptions name to delete: ")
                    self.subs.delete(self.username, subscription_name_to_delete) 
                    
            elif choice == "2":
                print("Search selected.")
                self.search.main()
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please choose 1, 2, or 3.")

    def main(self):
        while True:
            choice = input("Do you want to sign in, sign up, or exit? (sign in/sign up/exit): ").strip().lower()

            if choice == "sign in":
                if self.sign_in():
                    self.display_menu()
            elif choice == "sign up":
                self.sign_up()
            elif choice == "exit":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please choose 'sign in', 'sign up', or 'exit'.")

if __name__ == "__main__":
    app = Application()
    app.main()
