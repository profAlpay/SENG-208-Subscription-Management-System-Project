'''
Functions to search for subscriptions by keywords, billing cycle, amount, or payment status.
'''

import csv
from tabulate import tabulate

class Search:
    # Reading the CSV file and storing data
    def read_subscriptions(self, file_path):
        subscriptions = []
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                subscriptions.append(row)
        return subscriptions

    # Process subscriptions
    def process_subscriptions(self, subscriptions):
        results = []
        for subscription in subscriptions:
            username = subscription[0]
            for i in range(1, len(subscription), 2):
                if i + 1 < len(subscription):  # Ensure there's a date following the subscription name
                    subscription_name = subscription[i]
                    payment_day = subscription[i + 1]
                    results.append([username, subscription_name, payment_day])
        return results

    # Print results in a tabular format
    def print_results(self, results):
        headers = ["Username", "Subscription Name", "Payment Day"]
        print(tabulate(results, headers, tablefmt='grid'))

    # Search for subscriptions by keyword or direct value
    def search_subscriptions(self, subscriptions, search_term):
        results = []
        for subscription in subscriptions:
            username = subscription[0]
            for i in range(1, len(subscription), 2):
                if i + 1 < len(subscription):
                    subscription_name = subscription[i]
                    payment_day = subscription[i + 1]
                    if search_term.lower() in (subscription_name.lower(), payment_day.lower()):
                        results.append([username, subscription_name, payment_day])
        return results

    # Main function
    def main(self):
        file_path = 'subscriptions.csv'
        subscriptions = self.read_subscriptions(file_path)
        
        # Process and print all subscriptions
        print("All Subscriptions:")
        results = self.process_subscriptions(subscriptions)
        self.print_results(results)
        
        # Ask user for a search term
        search_term = input("Enter a keyword or payment day to search for subscriptions: ")
        
        # Search for subscriptions and print results
        print(f"\nSearch Results for '{search_term}':")
        search_results = self.search_subscriptions(subscriptions, search_term)
        if search_results:
            self.print_results(search_results)
        else:
            print("No subscriptions found matching the search term.")
