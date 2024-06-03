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
def calculate_days_remaining(day_of_month):
    today = datetime.datetime.today()
    current_year = today.year
    current_month = today.month
    try:
        next_payment_date = datetime.datetime(current_year, current_month, int(day_of_month))
        if next_payment_date < today:
            # If the date is in the past for this month, calculate for the next month
            if current_month == 12:
                next_payment_date = datetime.datetime(current_year + 1, 1, int(day_of_month))
            else:
                next_payment_date = datetime.datetime(current_year, current_month + 1, int(day_of_month))
        days_remaining = (next_payment_date - today).days
    except ValueError:
        days_remaining = "Invalid Date"
    return days_remaining

# Process subscriptions for odd-numbered entries starting from the third entry
def process_subscriptions(subscriptions):
    results = []
    for subscription in subscriptions:
        username = subscription[0]
        for i in range(1, len(subscription), 2):
            if i + 1 < len(subscription):  # Ensure there's a date following the subscription name
                subscription_name = subscription[i]
                payment_day = subscription[i + 1]
                days_remaining = calculate_days_remaining(payment_day)
                results.append([username, subscription_name, payment_day, days_remaining])
    return results

# Print results in a tabular format
def print_results(results):
    headers = ["Username", "Subscription Name", "Payment Day", "Days Remaining"]
    print(tabulate(results, headers, tablefmt='grid'))

# Main function
def main():
    file_path = 'subscriptions.csv'
    subscriptions = read_subscriptions(file_path)
    results = process_subscriptions(subscriptions)
    print_results(results)

if __name__ == "__main__":
    main()
