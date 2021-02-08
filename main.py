import sys
import datetime
import PIL
from PIL import Image
from matplotlib import pyplot as plt

if __name__ == '__main__':
    print('Args: ', sys.argv)
    file = open('solar_revenue.csv', 'r')
    transactions = file.read().split('\n')
    previous_revenue = [int(tx.split(',')[0]) for tx in transactions if ',' in tx] # gang gang gang
    file.close()
    print(f'Prior Average Solar Revenue: R{round(sum(previous_revenue) / len(previous_revenue), 2)}')

    todays_revenue = input('Enter Amount in Rands: ')

    if (todays_revenue.isnumeric()):
        previous_revenue.append(int(todays_revenue))
        todays_average = round(sum(previous_revenue) / len(previous_revenue), 2)
        print(f'New Average Solar Revenue: R{todays_average}')

        file = open('solar_revenue.csv', 'a')
        file.write(f'\n{todays_revenue},{str(datetime.datetime.now())}')
        file.close()

        if '--plot' in sys.argv:
            plt.plot(previous_revenue)
            plt.xlabel('time')
            plt.ylabel('solar revenue in Rands')
            plt.title(f'Daily Solar Revenue (average=R{todays_average})')
            plt.grid(True)
            plt.savefig('solar_revenue.png', bbox_inches='tight')
            img = Image.open('solar_revenue.png')
            wpercent = (400 / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((400, hsize), PIL.Image.ANTIALIAS)
            img.show()


