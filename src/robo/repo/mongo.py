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
    

            
    
    