from pymongo import MongoClient
from url_shortener_from_asgard import settings
from url_shortener_from_asgard.data_mappers.data_mapper import DataMapper

client = MongoClient("localhost", settings.MONGO_PORT)
db = client["urlShortenerFromAsgard"]


class MongoDbDataMapper(DataMapper):
    def __init__(self, collection_name):
        self.collection = db[collection_name]

    def get_all(self):
        results = self.collection.find({})

        return [i for i in results]

