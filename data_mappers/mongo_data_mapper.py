from pymongo import MongoClient
from ..settings import MONGO_PORT
from .data_mapper import DataMapper
from abc import abstractmethod

client = MongoClient("localhost", MONGO_PORT)
db = client["urlShortenerFromAsgard"]


class MongoDbDataMapper(DataMapper):
    def __init__(self, collection_name):
        self.collection = db[collection_name]

    
    
    def get_all(self):
        results = self.collection.find({})

        return [i for i in results]

