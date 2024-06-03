'''
Functions to search for subscriptions by keywords, billing cycle, amount, or payment status.
'''

import csv
import datetime
from tabulate import tabulate

# Reading the CSV file and storing data
def read_subscriptions(file_path):
    subscriptions = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            subscriptions.append(row)
    return subscriptions

# Process subscriptions
def process_subscriptions(subscriptions):
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
def print_results(results):
    headers = ["Username", "Subscription Name", "Payment Day"]
    print(tabulate(results, headers, tablefmt='grid'))

# Search for subscriptions by keyword
def search_by_keyword(subscriptions, keyword):
    results = []
    for subscription in subscriptions:
        username = subscription[0]
        for i in range(1, len(subscription), 2):
            if i + 1 < len(subscription):
                subscription_name = subscription[i]
                payment_day = subscription[i + 1]
                if keyword.lower() in subscription_name.lower():
                    results.append([username, subscription_name, payment_day])
    return results

# Print search results in a tabular format
def print_search_results(results):
    headers = ["Username", "Subscription Name", "Payment Day"]
    print(tabulate(results, headers, tablefmt='grid'))

# Main function
def main():
    file_path = 'subscriptions.csv'
    subscriptions = read_subscriptions(file_path)
    
    # Process and print all subscriptions without days remaining
    print("All Subscriptions:")
    results = process_subscriptions(subscriptions)
    print_results(results)
    
    # Ask user for a keyword to search
    search_type = input("Enter 'keyword' to search for subscriptions by keyword: ")
    if search_type.lower() == 'keyword':
        keyword = input("Enter a keyword to search for subscriptions: ")
        keyword_results = search_by_keyword(subscriptions, keyword)
        # Print search results
        print(f"\nSubscriptions containing '{keyword}':")
        print_search_results(keyword_results)
    else:
        print("Invalid search type. Please enter 'keyword'.")

if __name__ == "__main__":
    main()
