import sys
import datetime
from utils import plot_revenue

def fetch_transactions():
    with open('solar_revenue.csv', 'r') as file:
        transactions = file.read().split('\n')
        transaction_amounts = [int(tx.split(',')[0]) for tx in transactions if ',' in tx] # gang gang gang
        return transaction_amounts

# eventually read from/write to db if things get heavy
def write_transaction(amount):
    with open('solar_revenue.csv', 'a') as file:
        file.write(f'\n{todays_revenue},{str(datetime.datetime.now())}')

if __name__ == '__main__':
    previous_revenue = fetch_transactions()
    print(f'Prior Average Solar Revenue: R{round(sum(previous_revenue) / len(previous_revenue), 2)}')

    todays_revenue = input('Enter Amount in Rands: ')

    if (todays_revenue.isnumeric()):
        previous_revenue.append(int(todays_revenue))
        todays_average = round(sum(previous_revenue) / len(previous_revenue), 2)
        print(f'New Average Solar Revenue: R{todays_average}')

        write_transaction(todays_revenue)

        if '--plot' in sys.argv:
            params = {
                'title': f'Daily Solar Revenue (average=R{todays_average})',
                'xlabel': 'time',
                'ylabel': 'solar revenue in rands',
                'image_name': 'solar_revenue.png',
                'grid': True,
                'payload': previous_revenue
            }

            plot_revenue(params)
