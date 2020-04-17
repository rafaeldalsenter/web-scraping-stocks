from pymongo import MongoClient
import os

class Mongo:

    def __init__(self):
        self.__client = MongoClient(os.environ['MONGODB_CONNECTIONSTRING'])
        self.__db = self.__client.WebScrapingStocks

    def insert_quotes(self, quotes):
        dict_quotes = []

        for quote in quotes:
            dict_quotes.append(quote.__dict__)

        self.__db.quotes.insert_many(dict_quotes)

    def get_quotes(self):
        return self.__db.quotes.find()
          
    def update_quote(self, quote):
        query = { "codigo": quote.codigo, "date": quote.date }
        new_value = {"$set": {"value" : quote.value}}
        self.__db.quotes.update_one(query, new_value)
    
    