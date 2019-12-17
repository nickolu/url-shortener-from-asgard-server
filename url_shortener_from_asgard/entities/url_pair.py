import json
import random

from url_shortener_from_asgard.data_mappers.data_mapper_registry import (
    DataMapperRegistry,
)
from url_shortener_from_asgard.entities.available_words_for_source import (
    AvailableWordsForSource,
)
from url_shortener_from_asgard.entities.base import BaseEntity

MAX_NUMBER_OF_USES_PER_URL = 10


def get_random_available_asgardian_word():
    available_words_for_source_data_mapper = DataMapperRegistry.get(
        AvailableWordsForSource
    )

    return available_words_for_source_data_mapper.get_random_available_asgardian_word()


def get_url_pair_by_short_url(shortUrl):
    url_pair_data_mapper = DataMapperRegistry.get(UrlPair)
    document = url_pair_data_mapper.get_by_short_url(shortUrl)

    if document:
        return UrlPair(document)

    return None


def get_url_pair_by_long_url(shortUrl):
    url_pair_data_mapper = DataMapperRegistry.get(UrlPair)
    document = url_pair_data_mapper.get_by_long_url(shortUrl)

    if document:
        return UrlPair(document)

    return None


def get_all_url_pairs_for_user(user_id):
    url_pair_data_mapper = DataMapperRegistry.get(UrlPair)
    documents = url_pair_data_mapper.get_by_user_id(user_id)

    print("DOCUMENTS!!!!")
    print(documents)

    return documents


def insert_url_pair(url_pair):
    url_pair_data_mapper = DataMapperRegistry.get(UrlPair)
    url_pair_data_mapper.insert(url_pair)


def update_number_of_times_accessed_record(url_pair, times_accessed):
    url_pair_data_mapper = DataMapperRegistry.get(UrlPair)
    url_pair_data_mapper.update_number_of_times_accessed(url_pair, times_accessed)


def invalidate_url_pair(url_pair, reason):
    url_pair_data_mapper = DataMapperRegistry.get(UrlPair)
    url_pair_data_mapper.invalidate(url_pair, reason)


class UrlPair(BaseEntity):

    field_mapping = {
        "short_url": "short_url",
        "long_url": "long_url",
        "times_accessed": "times_accessed",
        "created_by": "created_by",
        "is_valid": "is_valid",
        "invalid_reason": "invalid_reason",
    }

    def __init__(self, document):
        self._document = document

        for key, value in document.items():
            self.key = value

    @property
    def times_accessed(self):
        return self._document["times_accessed"]

    @staticmethod
    def create_new(long_url, user):
        url_pair = UrlPair(
            {
                "short_url": get_random_available_asgardian_word(),
                "long_url": long_url,
                "times_accessed": 0,
                "is_valid": True,
                "created_by": user.id,
            }
        )

        insert_url_pair(url_pair)

        return url_pair

    @staticmethod
    def get_url_pairs_by_user(user_id):
        return get_all_url_pairs_for_user(user_id)

    @property
    def times_accessed(self):
        return self._document["times_accessed"]

    @property
    def is_max_access_limit_reached(self):
        return self.times_accessed >= MAX_NUMBER_OF_USES_PER_URL

    def access_url(self):
        if self.is_max_access_limit_reached:
            raise MaxNumberOfTimesAccessedReachedError()

        self.increment_number_of_times_accessed()

        return self._document["long_url"]

    def increment_number_of_times_accessed(self):
        self._document["times_accessed"] += 1
        update_number_of_times_accessed_record(self, self._document["times_accessed"])

    def invalidate(self, reason):
        invalidate_url_pair(self._document, reason)
        self._document["is_valid"] = False
        self._document["invalid_reason"] = reason


class MaxNumberOfTimesAccessedReachedError(Exception):
    def __init__(self, url):
        super(MaxNumberOfTimesAccessedReachedError, self).__init__(
            "URL {} has been accessed the max number of times".format(url)
        )
