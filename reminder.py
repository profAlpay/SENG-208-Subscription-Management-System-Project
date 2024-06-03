'''
Functions to set reminders for upcoming subscription payments.
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

# Calculate days remaining until next payment date
def calculate_days_remaining(subscription):
    today = datetime.datetime.today()
    try:
        next_payment_date = datetime.datetime.strptime(subscription[2], "%Y-%m-%d")
        days_remaining = (next_payment_date - today).days
    except ValueError:
        days_remaining = "Invalid Date"
    return days_remaining

# Process subscriptions for odd-numbered entries starting from the third entry
def process_subscriptions(subscriptions):
    results = []
    for i in range(2, len(subscriptions), 2):
        subscription = subscriptions[i]
        days_remaining = calculate_days_remaining(subscription)
        results.append([subscription[0], subscription[1], subscription[2], days_remaining])
    return results

# Print results in a tabular format
def print_results(results):
    headers = ["Username", "Subscription Name", "Next Payment Date", "Days Remaining"]
    print(tabulate(results, headers, tablefmt='grid'))

# Main function
def main():
    file_path = 'subscriptions.csv'
    subscriptions = read_subscriptions(file_path)
    results = process_subscriptions(subscriptions)
    print_results(results)

if __name__ == "__main__":
    main()
