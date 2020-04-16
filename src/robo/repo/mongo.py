from pymongo import MongoClient

class Mongo:

    def __init__(self):
        self.__client = MongoClient('mongodb://root:root@localhost:27017')
        self.__db = self.__client.WebScrapingStocks

    def insert_quotes(self, quotes):
        dict_quotes = []

        for quote in quotes:
            dict_quotes.append(quote.__dict__)

        self.__db.quotes.insert_many(dict_quotes)

    def insert_stocks(self, stocks):
        dict_stocks = []

        for stock in stocks:
            dict_stocks.append(stock.__dict__)

        self.__db.stocks.insert_many(dict_stocks)       
    
    def get_stocks(self):
        return self.__db.stocks.find()
          
    def update_stocks(self, stocks):
        
        for stock in stocks:
            query = { "codigo": stock.codigo }
            new_value = {"$set": {"url" : stock.url}}
            self.__db.stocks.update_one(query, new_value)
    
    