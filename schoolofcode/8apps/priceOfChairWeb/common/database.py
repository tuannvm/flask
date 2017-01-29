''' mongodb chapter '''
from pymongo import MongoClient

class Database(object):
    ''' database class '''
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        ''' initialize database config '''
        client = MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, data):
        ''' insert data to collection '''
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        ''' find data from collection '''
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        ''' find only one line '''
        return Database.DATABASE[collection].find_one(query)
