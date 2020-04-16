import schedule
import time
import datetime
from models.stock import Stock
from scraping import Scraping
from models.quote import Quote
from repo.mongo import Mongo

class Heart:

    def __init__(self):
        self.__stocks = None
        self.__scraping = Scraping()
 
    def scraping_task(self):
        date_now = datetime.datetime.now()
        list_quote = []

        print(f'Initializing capture at {date_now}')

        for stock in self.__stocks:
            print(f'Getting value from {stock.codigo}...')
            value = self.__scraping.get_stock_value(stock)
            list_quote.append(Quote(stock.codigo, date_now, value))

        Mongo().insert_quotes(list_quote)
        print('Values inserted in MongoDB database')

    def play(self):
        schedule.every(1).minutes.do(self.scraping_task)

        self.__stocks = []
        # self.__stocks.append(Stock('CEAB3', None))
        # self.__stocks.append(Stock('VVAR3', None))
        # self.__stocks.append(Stock('GOLL4', None))
        # self.__stocks.append(Stock('POMO4', None))
        # self.__stocks.append(Stock('COGN3', None))
        # self.__stocks.append(Stock('MRFG3', None))
        # self.__stocks.append(Stock('PETR4', None))
        # self.__stocks.append(Stock('SMLS3', None))

        #self.__scraping.set_urls(self.__stocks)

        dict_stocks = Mongo().get_stocks()

        self.__stocks = Stock.create_list(dict_stocks)

        self.__scraping.set_urls(self.__stocks)
        
        while True:
            schedule.run_pending()
            time.sleep(1)

        

    
