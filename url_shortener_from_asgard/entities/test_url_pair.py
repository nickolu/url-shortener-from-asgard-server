import unittest
from unittest import TestCase

from data_mappers.data_mapper_registry import DataMapperRegistry
from data_mappers.url_pair_data_mapper import UrlPairInMemoryDataMapper
from data_mappers.user_data_mapper import UserInMemoryDataMapper
from data_mappers.available_words_for_source_data_mapper import (
    AvailableWordsForSourceInMemoryDataMapper,
)
from .available_words_for_source import AvailableWordsForSource
from .url_pair import UrlPair
from .user import User


class TestDemo(TestCase):
    def test_nothing(self):
        assert True


class TestUrlPair(TestCase):
    def setUp(self):
        self.url_pair_data_mapper = UrlPairInMemoryDataMapper()
        self.user_data_mapper = UserInMemoryDataMapper()
        self.available_words_for_source_data_mapper = (
            AvailableWordsForSourceInMemoryDataMapper()
        )

        DataMapperRegistry.register(UrlPair, self.url_pair_data_mapper)
        DataMapperRegistry.register(User, self.user_data_mapper)
        DataMapperRegistry.register(
            AvailableWordsForSource, self.available_words_for_source_data_mapper
        )

    def test_should_create_new_url_pair(self):
        user = User.create_new()
        UrlPair.create_new("https://www.google.com", user)

        assert True


if __name__ == "__main__":
    unittest.main()
