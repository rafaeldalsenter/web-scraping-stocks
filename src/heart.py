import schedule
import time
import datetime
import os
from models.stock import Stock
from scraping import Scraping
from models.quote import Quote
from repo.mongo import Mongo

MINUTES_SCHEDULE = 10

class Heart:

    def __init__(self):
        self.__stocks = None
        self.__scraping = Scraping()
 
    def __scraping_task(self):
        date_now = datetime.datetime.now()
        list_quote = []

        print(f'Initializing capture at {date_now}')

        for stock in self.__stocks:
            print(f'Getting value from {stock.codigo}...')
            value = self.__scraping.get_stock_value(stock)
            list_quote.append(Quote(stock.codigo, date_now, value))

        Mongo().insert_quotes(list_quote)
        print('Values inserted in MongoDB database')

    def __return_stocks_from_environ(self):
        stocks = os.environ['STOCKS'].split(',')
        
        result = []

        for stock in stocks:
            result.append(Stock(stock, None))

        return result

    def play(self):
        print('Robo starting...')
        schedule.every(MINUTES_SCHEDULE).minutes.do(self.__scraping_task)

        print('Capture links from stocks...')
        self.__stocks = self.__return_stocks_from_environ()
        self.__scraping.set_urls(self.__stocks)
        
        print(f'Schedule started! ({MINUTES_SCHEDULE} minutes)')
        while True:
            schedule.run_pending()
            time.sleep(1)

    
