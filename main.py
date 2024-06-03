'''
Contains the main logic of the application.
Handles user authentication and menu navigation.
'''
import csv
import os

def load_users(filename='users.csv'):
    users = {}
    if os.path.exists(filename):
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:  # Check if row is not empty
                    username, password = row
                    users[username] = password
    return users

def save_user(username, password, filename='users.csv'):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

def sign_in(users):
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username] == password:
        print("Sign in successful!")
        return True
    else:
        print("Invalid username or password.")
        return False

def sign_up(users):
    username = input("Choose a username: ")
    if username in users:
        print("Username already exists. Please choose a different username.")
        return

    password = input("Choose a password: ")
    users[username] = password
    save_user(username, password)
    print("Sign up successful!")

def display_menu():
    while True:
        print("\nMain Menu:")
        print("1. Display")
        print("2. Settings")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ").strip()

        if choice == "1":
            display_submenu()
        elif choice == "2":
            settings_submenu()
        elif choice == "3":
            print("Exiting the menu.")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

def display_submenu():
    while True:
        print("\nDisplay Menu:")
        print("1. Subscription")
        print("2. Payment")
        print("3. Reminder")
        print("4. Expanse Analysis")
        print("5. Back to Main Menu")

        choice = input("Choose an option (1/2/3/4/5): ").strip()

        if choice == "1":
            print("Subscription selected.")
        elif choice == "2":
            print("Payment selected.")
        elif choice == "3":
            print("Reminder selected.")
        elif choice == "4":
            print("Expanse Analysis selected.")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please choose 1, 2, 3, 4, or 5.")

def settings_submenu():
    while True:
        print("\nSettings Menu:")
        print("1. Subscription")
        print("2. Search")
        print("3. Back to Main Menu")

        choice = input("Choose an option (1/2/3): ").strip()

        if choice == "1":
            print("Subscription selected.")
        elif choice == "2":
            print("Search selected.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

def main():
    users = load_users()
    while True:
        choice = input("Do you want to sign in, sign up, or exit? (sign in/sign up/exit): ").strip().lower()

        if choice == "sign in":
            if sign_in(users):
                display_menu()
        elif choice == "sign up":
            sign_up(users)
        elif choice == "exit":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose 'sign in', 'sign up', or 'exit'.")

if __name__ == "__main__":
    main()
