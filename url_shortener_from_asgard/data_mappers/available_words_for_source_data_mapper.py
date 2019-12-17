import random
from url_shortener_from_asgard.data_mappers.mongo_data_mapper import MongoDbDataMapper
from url_shortener_from_asgard.data_mappers.in_memory_data_mapper import (
    InMemoryDataMapper,
)


class AvailableWordsForSourceMongoDbDataMapper(MongoDbDataMapper):
    def __init__(self):
        super(AvailableWordsForSourceMongoDbDataMapper, self).__init__(
            "available_words_for_source"
        )

    def get_random_available_word_from_source(self, source):
        source = self.collection.find_one({"source": source})

        _id = source["_id"]
        available_words = source["available_words"]

        if not available_words:
            raise NoWordsRemainingInSourceError(source)

        random_word = random.choice(available_words)
        available_words.remove(random_word)
        self.collection.update(
            {"_id": _id}, {"$set": {"available_words": available_words}},
        )

        return random_word

    def get_random_available_asgardian_word(self):
        return self.get_random_available_word_from_source("asgard")


class AvailableWordsForSourceInMemoryDataMapper(InMemoryDataMapper):
    pass


class NoWordsRemainingInSourceError(Exception):
    def __init__(self, source):
        super(NoWordsRemainingInSourceError, self).__init__(
            "All words from {} have been exhausted. Tell the developer to add more words for \
            this source, or to write a better program, because this is really silly".format(
                source
            )
        )

