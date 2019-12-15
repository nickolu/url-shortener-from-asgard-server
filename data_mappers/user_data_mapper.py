from .mongo_data_mapper import MongoDbDataMapper


class UserMongoDbDataMapper(MongoDbDataMapper):
    def __init__(self):
        super(UserMongoDbDataMapper, self).__init__("users")

    def create_user(self, user):
        self.collection.insert_one(user._document)

        return user
