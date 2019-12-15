from .mongo_data_mapper import MongoDbDataMapper


class UrlPairMongoDbDataMapper(MongoDbDataMapper):
    def __init__(self):
        super(UrlPairMongoDbDataMapper, self).__init__("url_pairs")

    def create_url_pair(self, url_pair):
        self.collection.insert_one(url_pair._document)

        return url_pair

    def get_by_short_url(self, short_url=""):
        return self.collection.find_one({"short_url": short_url})

    def get_by_long_url(self, long_url=""):
        return self.collection.find_one({"long_url": long_url})

    def get_by_user(self, user):
        return self.collection.find({"created_by": user._document["_id"]})

    def insert(self, url_pair):
        self.collection.insert_one(url_pair._document)

    def increment_number_of_times_accessed(self, url_pair):
        url_pair.times_accessed += 1
        self.collection.update_one(
            url_pair, {"number_of_times_accessed": url_pair.times_accessed}
        )

        return url_pair.times_accessed

    def invalidate_url_pair(self, url_pair, reason):
        self.collection.update_one(url_pair, {"is_valid": False, "reason": reason})
