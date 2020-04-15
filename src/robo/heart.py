import schedule
import time
import datetime
from stock import Stock
from scraping import Scraping
from quote import Quote
from repo.mongo import Mongo

class Heart:

    def __init__(self):
        self.__stocks = None
        self.__scraping = Scraping()
 
    def scraping_task(self):
        date_now = datetime.datetime.now()
        list_quote = []

        for stock in self.__stocks:
            value = self.__scraping.get_stock_value(stock)
            list_quote.append(Quote(stock.codigo, date_now, value))

        Mongo().insert_quote(list_quote)

    def play(self):
        schedule.every(10).seconds.do(self.scraping_task)

        self.__stocks = []
        self.__stocks.append(Stock('CEAB3', None))
        self.__stocks.append(Stock('VVAR3', None))

        self.__scraping.set_urls(self.__stocks)
        
        while True:
            schedule.run_pending()
            time.sleep(1)

        

    
