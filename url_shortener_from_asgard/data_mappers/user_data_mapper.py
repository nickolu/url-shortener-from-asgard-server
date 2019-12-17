from url_shortener_from_asgard.data_mappers.mongo_data_mapper import MongoDbDataMapper
from url_shortener_from_asgard.data_mappers.in_memory_data_mapper import (
    InMemoryDataMapper,
)
from bson import ObjectId


class UserMongoDbDataMapper(MongoDbDataMapper):
    def __init__(self):
        super(UserMongoDbDataMapper, self).__init__("users")

    def create_user(self, user):
        self.collection.insert_one(user._document)

        return user

    def get_by_id(self, user_id=""):
        return self.collection.find_one({"_id": ObjectId(user_id)})


class UserInMemoryDataMapper(InMemoryDataMapper):
    def create_user(self, user):
        self.insert(user)

    pass
