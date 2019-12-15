import random
import json
from .base import BaseEntity
from .available_words_for_source import AvailableWordsForSource
from ..data_mappers.data_mapper_registry import DataMapperRegistry

MAX_NUMBER_OF_USES_PER_URL = 10


def get_random_available_asgardian_word():
    available_words_for_source_data_mapper = DataMapperRegistry.get(
        AvailableWordsForSource
    )

    return available_words_for_source_data_mapper.get_random_available_asgardian_word()


def get_long_url_by_short_url(shortUrl):
    url_pair_data_mapper = DataMapperRegistry.get(UrlPair)
    return url_pair_data_mapper.get_by_short_url(shortUrl)


def insert_url_pair(url_pair):
    url_pair_data_mapper = DataMapperRegistry.get(UrlPair)
    url_pair_data_mapper.insert(url_pair)


def increment_number_of_times_accessed(url_pair):
    url_pair_data_mapper = DataMapperRegistry.get(UrlPair)
    url_pair_data_mapper.increment_number_of_times_accessed(url_pair)


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

        for key, value in document.iteritems():
            self.key = value

    @property
    def times_accessed(self):
        return self._document["times_accessed"]

    @staticmethod
    def create_new(long_url):
        url_pair = UrlPair(
            {
                "short_url": get_random_available_asgardian_word(),
                "long_url": long_url,
                "times_accessed": 0,
                "is_valid": True,
            }
        )

        insert_url_pair(url_pair)

        return url_pair

    @property
    def access_url(self):
        if self._document["times_accessed"] >= MAX_NUMBER_OF_USES_PER_URL:
            raise MaxNumberOfTimesAccessedReachedError()

        self.increment_number_of_times_accessed()

        return self._document["long_url"]

    def increment_number_of_times_accessed(self):
        self._document["times_accessed"] = increment_number_of_times_accessed()

    def invalidate(self, reason):
        invalidate_url_pair(self._document, reason)
        self._document["is_valid"] = False
        self._document["invalid_reason"] = reason


class MaxNumberOfTimesAccessedReachedError(Exception):
    def __init__(self, url):
        super(MaxNumberOfTimesAccessedReachedError, self).__init__(
            "URL {} has been accessed the max number of times".format(url)
        )
