from .mongo_data_mapper import MongoDbDataMapper
from .in_memory_data_mapper import InMemoryDataMapper


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

    def get_by_user_id(self, user_id):
        return self.collection.find({"created_by": user_id})

    def insert(self, url_pair):
        self.collection.insert_one(url_pair._document)

    def update_number_of_times_accessed(self, url_pair, times_accessed):
        mongo_filter = {"short_url": url_pair._document["short_url"]}

        self.collection.update_one(
            mongo_filter, {"$set": {"times_accessed": times_accessed}}
        )

        return times_accessed


class UrlPairInMemoryDataMapper(InMemoryDataMapper):
    def create_url_pair(self, url_pair):
        self.insert(url_pair)

        return url_pair

    def get_by_short_url(self, short_url=""):
        return self.get_one_by_field_name("short_url", short_url)

    def get_by_long_url(self, long_url=""):
        return self.get_one_by_field_name("long_url", long_url)

    def get_by_user_id(self, user_id):
        return self.get_all_by_field_name("user_id", user_id)

    def update_number_of_times_accessed(self, url_pair, times_accessed):
        url_pair._document["times_accessed"] = times_accessed
        self.update(url_pair)

        return times_accessed
