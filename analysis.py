'''
Functions to calculate total expenses and analyze subscription expenses over time.
'''

import pandas as pd

class Analysis():
    def __init__(self, subscriptions_file, prices_file):
        self.subscriptions_file = subscriptions_file
        self.prices_file = prices_file

    def total_price(self, user_id):
        # Read CSV files using pandas
        subscriptions_df = pd.read_csv(self.subscriptions_file, header=None, names=['user_id', 'subscription_name', 'some_other_value'])
        prices_df = pd.read_csv(self.prices_file)
        
        # Debug: Print the columns of prices_df to check the column names
        # print("Columns in prices_df:", prices_df.columns)
        
        # Ensure column names are correct
        prices_df.columns = [col.strip() for col in prices_df.columns]  # Remove any leading/trailing spaces

        # Extract the user's subscriptions
        user_subscriptions = subscriptions_df[subscriptions_df['user_id'] == user_id]['subscription_name'].tolist()

        # Calculate the total cost
        total_cost = 0
        for subscription in user_subscriptions:
            if subscription in prices_df['subscription_name'].values:
                price = prices_df[prices_df['subscription_name'] == subscription]['price'].values[0]
                total_cost += price

        print(f"{user_id} toplam abonelik ücreti: ₺{total_cost:.2f}")

# Create an instance of the Analysis class
#analysis = Analysis('subscriptions.csv', 'prices.csv')

# Calculate and print the total price for a specific user
#analysis.total_price('user1')
