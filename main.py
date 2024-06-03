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
    else:
        print("Invalid username or password.")

def sign_up(users):
    username = input("Choose a username: ")
    if username in users:
        print("Username already exists. Please choose a different username.")
        return

    password = input("Choose a password: ")
    users[username] = password
    save_user(username, password)
    print("Sign up successful!")

def main():
    users = load_users()
    choice = input("Do you want to sign in or sign up? (sign in/sign up): ").strip().lower()

    if choice == "sign in":
        sign_in(users)
    elif choice == "sign up":
        sign_up(users)
    else:
        print("Invalid choice. Please choose 'sign in' or 'sign up'.")

if __name__ == "__main__":
    main()




if select == 1:
    Subscriptions.add("Netflix")