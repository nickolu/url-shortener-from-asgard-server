import unittest
from unittest import TestCase

from url_shortener_from_asgard.data_mappers.data_mapper_registry import (
    DataMapperRegistry,
)
from url_shortener_from_asgard.data_mappers.url_pair_data_mapper import (
    UrlPairInMemoryDataMapper,
)
from url_shortener_from_asgard.data_mappers.user_data_mapper import (
    UserInMemoryDataMapper,
)
from url_shortener_from_asgard.data_mappers.available_words_for_source_data_mapper import (
    AvailableWordsForSourceInMemoryDataMapper,
)
from url_shortener_from_asgard.entities.available_words_for_source import (
    AvailableWordsForSource,
)
from url_shortener_from_asgard.entities.url_pair import UrlPair
from url_shortener_from_asgard.entities.user import User


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
