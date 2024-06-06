'''
Functions related to subscription management (add, update, delete, search).
'''
import csv
import os
from tabulate import tabulate

class Subscriptions:
    def __init__(self, username=None):
        self.username = username
        self.subscriptions = self.load_subscriptions()

    def load_subscriptions(self):
        subscriptions = []
        if os.path.exists('subscriptions.csv'):
            with open('subscriptions.csv', 'r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    subscriptions.append({
                        "username": row[0],
                        "subscription_name": row[1],
                        "payment_day": row[2]
                    })
        return subscriptions

    def add(self, username, subscription_name, payment_day):
        self.subscriptions.append({
            "username": username,
            "subscription_name": subscription_name,
            "payment_day": payment_day
        })
        self.save_subscriptions()

    def update(self, username, old_subscription_name, new_subscription_name, new_payment_day):
        found = False
        for subscription in self.subscriptions:
            if subscription["username"] == username and subscription["subscription_name"] == old_subscription_name:
                subscription["subscription_name"] = new_subscription_name
                subscription["payment_day"] = new_payment_day
                found = True
                break
        if found:
            self.save_subscriptions()
        else:
            print(f"Subscription '{old_subscription_name}' for user '{username}' not found.")

    def delete(self, username, subscription_name):
        found = False
        for subscription in self.subscriptions:
            if subscription["username"] == username and subscription["subscription_name"] == subscription_name:
                self.subscriptions.remove(subscription)
                found = True
                break
        if found:
            self.save_subscriptions()
        else:
            print(f"Subscription '{subscription_name}' for user '{username}' not found.")

    def search(self, username, subscription_name):
        for subscription in self.subscriptions:
            if subscription["username"] == username and subscription["subscription_name"] == subscription_name:
                return True
        return False

    def save_subscriptions(self):
        with open('subscriptions.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for subscription in self.subscriptions:
                writer.writerow([subscription["username"], subscription["subscription_name"], subscription["payment_day"]])

    def display(self):
        if self.subscriptions:
            headers = ["Username", "Subscription Name", "Payment Day"]
            if self.username:
                rows = [[s["username"], s["subscription_name"], s["payment_day"]] for s in self.subscriptions if s["username"] == self.username]
            else:
                rows = [[s["username"], s["subscription_name"], s["payment_day"]] for s in self.subscriptions]
            if rows:
                print(tabulate(rows, headers, tablefmt="grid"))
            else:
                print(f"No subscriptions found for user '{self.username}'.")
        else:
            print("No subscriptions found.")
