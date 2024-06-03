import pandas as pd

class Analysis():
    # CSV dosyalarını okuyun

    def total_price(self, user_id):
        with open('subscriptions.csv', 'r') as file:
            subscriptions_data = file.readlines()

        price_df = pd.read_csv('price.csv', header=None, names=['subscription_name', 'price'])


        # Kullanıcının aboneliklerini alın
        user_subscriptions = []
        for line in subscriptions_data:
            if line.startswith(user_id):
                parts = line.strip().split(',')
                user_subscriptions = parts[1::2]  # Abonelik isimleri her iki elemandan birinde bulunuyor
                break

        # Kullanıcının abonelik fiyatlarını toplayın
        total_cost = 0
        for subscription in user_subscriptions:
            if subscription in price_df['subscription_name'].values:
                price = price_df[price_df['subscription_name'] == subscription]['price'].values[0]
                print(price)
                total_cost += price

        print(f"user toplam abonelik ücreti: ${total_cost:.2f}")


